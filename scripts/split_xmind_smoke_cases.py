#!/usr/bin/env python3
"""Split CodeFlying smoke-test XMind topics into one Markdown file per P0 case."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import zipfile
from collections import Counter
from pathlib import Path


MODULE_SLUGS = (
    ("未登录首页", "guest-home"),
    ("手机号验证码登录", "phone-auth"),
    ("微信登录", "wechat-auth"),
    ("登录", "auth"),
    ("顶部导航", "top-nav"),
    ("应用广场", "app-square"),
    ("我的应用", "my-apps"),
    ("赚取积分", "earn-points"),
    ("我的权益", "entitlements"),
    ("设置和账单", "settings-billing"),
    ("应用预览页", "app-preview"),
    ("复制应用", "copy-app"),
    ("应用创建", "app-create"),
    ("登录后首页", "home"),
    ("工作台", "workspace"),
    ("个人中心", "profile"),
)

MANUAL_KEYWORDS = (
    "用户微信扫码登录成功",
    "手机扫码可正常访问",
    "拉起支付宝",
    "微信h5页面拉起微信支付",
)

STATEFUL_KEYWORDS = (
    "创建",
    "删除",
    "修改",
    "复制",
    "发布",
    "取消发布",
    "邀请",
    "奖励",
    "购买",
    "充值",
    "退出登录",
    "切换",
)


def children(topic: dict) -> list[dict]:
    result: list[dict] = []
    child_map = topic.get("children") or {}
    if isinstance(child_map, dict):
        for kind in ("attached", "detached"):
            values = child_map.get(kind) or []
            if isinstance(values, list):
                result.extend(values)
    return result


def clean_title(value: str) -> str:
    value = value.strip()
    value = re.sub(r"^TC[：:]\s*", "", value)
    return value


def is_tc_title(value: str) -> bool:
    return value.strip().startswith(("TC：", "TC:"))


def case_title(raw_title: str, path: list[str]) -> str:
    """Use every final XMind node as a case.

    Some final nodes are written as parameter/variant leaves below a parent
    ``TC：`` topic (for example ``标准版 3000``).  They are still independent
    final nodes in the logic graph, so keep the parent TC context in the
    generated title instead of dropping them.
    """
    if is_tc_title(raw_title):
        return clean_title(raw_title)
    parent_tc = next(
        (clean_title(item) for item in reversed(path[:-1]) if is_tc_title(item)),
        None,
    )
    return f"{parent_tc} / {raw_title.strip()}" if parent_tc else raw_title.strip()


def case_module_path(path: list[str]) -> str:
    """Return the FM path without the leaf and without a parent TC label."""
    parts = [clean_module(item) for item in path[1:-1] if clean_module(item)]
    parts = [item for item in parts if not is_tc_title(item)]
    return " / ".join(parts) or "通用"


def clean_module(value: str) -> str:
    value = value.strip()
    value = value.replace("F M：", "").replace("FM：", "")
    return re.sub(r"\s+", " ", value).strip()


def module_slug(path_text: str) -> str:
    for keyword, slug in MODULE_SLUGS:
        if keyword in path_text:
            return slug
    return "general"


def platform_info(top_title: str) -> tuple[str, str, str]:
    if "H5" in top_title.upper():
        return "国内H5", "H5", "h5"
    return "国内PC", "PC", "pc"


def execution_mode(title: str) -> tuple[str, str]:
    if any(keyword in title for keyword in MANUAL_KEYWORDS):
        return (
            "真人依赖（自动化完成入口、二维码或跳转检查）",
            "依赖实体手机、微信/支付宝客户端或真实扫码结果。",
        )
    return "可自动化", ""


def agent_for(platform_key: str, path_text: str, title: str) -> str:
    identity_text = f"{path_text} {title}"
    if (
        "登录" in identity_text
        or "邀请新用户" in identity_text
        or "非新用户" in identity_text
        or "验证码" in identity_text
    ):
        return "auth_identity_runner"
    if platform_key == "pc":
        if any(keyword in path_text for keyword in ("应用创建", "应用预览页", "复制应用")):
            return "pc_app_runner"
        if any(keyword in path_text for keyword in ("应用广场", "我的应用", "顶部导航", "在线客服", "语言选择")):
            return "pc_navigation_runner"
        if any(
            keyword in path_text
            for keyword in ("侧边栏", "赚取积分", "我的权益", "设置和账单")
        ):
            return "pc_account_runner"
        return "pc_navigation_runner"
    if any(keyword in path_text for keyword in ("工作台", "个人中心", "应用创建")):
        return "h5_workspace_runner"
    return "h5_browse_runner"


def account_profile(path_text: str, title: str) -> str:
    text = f"{path_text} {title}"
    if "未登录首页" in text:
        return "anonymous（不加载 Playwright session）"
    if "邀请新用户" in text:
        return "fixed-inviter + generated-new-phone"
    if "非新用户" in text:
        return "fixed-inviter + fixed-existing-phone"
    if "手机号" in text or "验证码" in text:
        return "generated-test-phone + mock-otp"
    if "微信登录" in text or "微信扫码登录" in text:
        return "anonymous + manual-wechat"
    if "非会员用户" in text:
        return "free-user-session"
    if "会员用户点击" in text:
        return "paid-user-session"
    return "default-playwright-session"


def user_type(path_text: str, title: str) -> str:
    text = f"{path_text} {title}"
    if "非会员" in text or "免费版" in text:
        return "免费用户"
    if "会员" in text or "购买" in text or "账单" in text:
        return "付费用户"
    return "免费用户 / 付费用户"


def state_metadata(title: str, path_text: str) -> tuple[str, str, str]:
    text = f"{path_text} {title}"
    stateful = any(keyword in text for keyword in STATEFUL_KEYWORDS)
    if "邀请" in text or "奖励" in text:
        return "yes", "invitation:{inviter_id}", "清理测试被邀请人、邀请关系与测试奖励记录"
    if "密钥" in text:
        return "yes" if stateful else "no", "api_key:{account_id}", "删除本轮创建的测试密钥；恢复基线状态"
    if "支付" in text or "购买" in text or "充值" in text or "账单" in text:
        return "yes" if stateful else "no", "payment:{account_id}", "使用 mock/沙箱；不得产生真实扣款"
    if "应用" in text and stateful:
        return "yes", "app:{app_id}", "清理本轮创建的应用或恢复名称、发布状态"
    if "登录" in text or "验证码" in text or "退出登录" in text:
        return "yes" if stateful else "no", "account:{phone}", "清理动态测试账号及登录会话"
    return "yes" if stateful else "no", "none", "无；若产生临时数据则按 test_run_id 清理"


def precondition(path_text: str, title: str, profile: str) -> str:
    text = f"{path_text} {title}"
    if "未登录首页" in text:
        return "新建无登录态 Browser Context，不加载 storageState。"
    if "邀请新用户" in text:
        return "固定邀请人已登录；生成测试手机号并在执行前确保该手机号不存在。"
    if "非新用户" in text:
        return "固定邀请人已登录；使用已经注册过的固定老用户手机号。"
    if "验证码" in text or "手机号" in text:
        return "启用测试环境 mock 验证码；使用测试专用手机号段，禁止向真实号码发送短信。"
    if "微信扫码登录" in text:
        return "未登录；具备微信测试账号和人工扫码条件。"
    if profile == "free-user-session":
        return "加载免费用户 Playwright session。"
    if profile == "paid-user-session":
        return "加载付费会员 Playwright session。"
    return "加载对应端的 Playwright session；需要应用时使用稳定、非转圈的测试应用。"


def original_marker(topic: dict) -> str:
    markers = topic.get("markers") or []
    ids = [m.get("markerId") for m in markers if isinstance(m, dict) and m.get("markerId")]
    return ", ".join(ids) if ids else "无"


def render_case(
    case_id: str,
    title: str,
    platform: str,
    module_path: str,
    agent: str,
    execution: str,
    manual_reason: str,
    profile: str,
    data_change: str,
    data_lock: str,
    cleanup: str,
    marker: str,
) -> str:
    condition = precondition(module_path, title, profile)
    manual_line = manual_reason or "无"
    return f"""# {case_id} {title}

- 优先级：P0
- 模块：{module_path}
- 平台：{platform}
- 执行方式：{execution}
- 问题类型：产品体验
- 用户类型：{user_type(module_path, title)}
- 前置条件：{condition}
- Agent 分组：{agent}
- 账号类型：{profile}
- 是否修改数据：{data_change}
- 数据锁：`{data_lock}`
- 清理动作：{cleanup}
- 人工测试原因：{manual_line}
- XMind 原始标记：`{marker}`

## 测试步骤

1. 创建独立的 {platform} Browser Context，并按前置条件加载或清除登录态。
2. 进入 FM 路径：`{module_path}`。
3. 执行原始测试点描述的操作：{title}。
4. 记录页面状态、URL、关键 DOM、接口结果和截图。

## 预期结果

1. 原始测试点描述的目标结果正确发生：{title}。
2. 页面无白屏、无未处理报错，相关功能可继续操作。

## 通过标准

- 目标页面、弹窗、状态或数据变化与测试点描述一致。
- 自动化证据完整；若有重试，必须记录首次错误并标记 `RETRY_PASS`。

## 失败条件

- 目标结果未出现、出现错误状态、数据不一致或页面不可继续操作。

## 阻塞条件

- 测试环境、账号、第三方服务或必要测试数据不可用。

## 证据要求

- 操作前后截图。
- 页面 URL 与关键 DOM 状态。
- 相关业务接口结果；HTTP 200 仍需检查业务码与返回数据。
- 涉及数据变化时，保存变化前后数据及清理结果。

## 备注

- 本用例由 `码上飞冒烟测试用例.xmind` 自动拆分。
- 首次人工 review 时应补充稳定 DOM 选择器和更精确的页面入口。
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--xmind",
        default="/Users/codeflying-ui-cases/码上飞冒烟测试用例.xmind",
    )
    parser.add_argument(
        "--output",
        default="/Users/codeflying-ui-cases/cases/P0/smoke",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace the previously generated smoke directory only.",
    )
    args = parser.parse_args()

    xmind_path = Path(args.xmind)
    output_root = Path(args.output)
    if output_root.exists() and any(output_root.iterdir()):
        if not args.force or output_root.name != "smoke":
            raise SystemExit(f"Refusing to overwrite non-empty directory: {output_root}")
        shutil.rmtree(output_root)

    with zipfile.ZipFile(xmind_path) as archive:
        sheets = json.loads(archive.read("content.json").decode("utf-8"))

    rows: list[dict] = []
    counters: Counter[str] = Counter()

    def walk(topic: dict, path: list[str], top_title: str) -> None:
        raw_title = str(topic.get("title") or "").strip()
        next_path = path + [raw_title]
        topic_children = children(topic)
        # The XMind contract is: every final node is a test case.  Do not
        # count parent TC topics that have children, and do not discard
        # leaf variants just because their title lacks the "TC：" prefix.
        if not topic_children:
            platform, id_segment, platform_key = platform_info(top_title)
            counters[id_segment] += 1
            case_id = f"CF-P0-{id_segment}-{counters[id_segment]:03d}"
            module_path = case_module_path(next_path)
            path_text = " / ".join(path)
            title = case_title(raw_title, next_path)
            slug = module_slug(path_text)
            execution, manual_reason = execution_mode(title)
            profile = account_profile(path_text, title)
            data_change, data_lock, cleanup = state_metadata(title, path_text)
            agent = agent_for(platform_key, path_text, title)
            target_dir = output_root / ("domestic-pc" if platform_key == "pc" else "domestic-h5") / slug
            target_file = target_dir / f"{case_id}.md"
            rows.append(
                {
                    "id": case_id,
                    "title": title,
                    "platform": platform,
                    "module": module_path,
                    "agent": agent,
                    "execution": execution,
                    "path": target_file,
                    "content": render_case(
                        case_id=case_id,
                        title=title,
                        platform=platform,
                        module_path=module_path,
                        agent=agent,
                        execution=execution,
                        manual_reason=manual_reason,
                        profile=profile,
                        data_change=data_change,
                        data_lock=data_lock,
                        cleanup=cleanup,
                        marker=original_marker(topic),
                    ),
                }
            )
        for child in children(topic):
            walk(child, next_path, top_title)

    for sheet in sheets:
        root = sheet.get("rootTopic") or {}
        for top in children(root):
            top_title = str(top.get("title") or "").strip()
            walk(top, [top_title], top_title)

    for row in rows:
        row["path"].parent.mkdir(parents=True, exist_ok=True)
        row["path"].write_text(row["content"], encoding="utf-8")

    index_lines = [
        "# CodeFlying P0 冒烟测试用例",
        "",
        "> 来源：`码上飞冒烟测试用例.xmind`  ",
        "> 组织方式：一条 TC 一个 Markdown，按端和 FM 模块分目录。",
        "",
        "## 统计",
        "",
        f"- 用例总数：{len(rows)}",
        f"- 国内 PC：{counters['PC']}",
        f"- 国内 H5：{counters['H5']}",
        f"- 真人依赖：{sum('真人依赖' in row['execution'] for row in rows)}",
        "",
        "## 用例索引",
        "",
        "| 用例 ID | 端 | FM 模块 | Agent | 执行方式 | 标题 |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        relative = row["path"].relative_to(output_root)
        index_lines.append(
            f"| [{row['id']}]({relative.as_posix()}) | {row['platform']} | "
            f"{row['module']} | `{row['agent']}` | {row['execution']} | {row['title']} |"
        )
    (output_root / "README.md").write_text(
        "\n".join(index_lines).rstrip() + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "total": len(rows),
                "pc": counters["PC"],
                "h5": counters["H5"],
                "manual": sum("真人依赖" in row["execution"] for row in rows),
                "output": str(output_root),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
