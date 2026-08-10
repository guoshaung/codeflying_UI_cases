#!/usr/bin/env python3
"""从海外版冒烟大纲生成 P0 case Markdown。

海外版多数检查点沿用国内版业务链路；脚本复用已完善的国内 case 细节，
重新分配海外专属 ID，替换市场和域名，并补充 Google / 邮箱登录专用 case。
生成的 Agent 分组使用当前实际 sub-agent 名称，避免回退到旧 runner 名称。
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PC_SOURCES = [
    "CF-P0-PC-001", "CF-P0-PC-002", None, None, None,
    "CF-P0-PC-008", "CF-P0-PC-009", "CF-P0-PC-013", "CF-P0-PC-014",
    "CF-P0-PC-015", "CF-P0-PC-016", "CF-P0-PC-017",
    "CF-P0-PC-018", "CF-P0-PC-019", "CF-P0-PC-020", "CF-P0-PC-021",
    "CF-P0-PC-022", "CF-P0-PC-023", "CF-P0-PC-024", "CF-P0-PC-025",
    "CF-P0-PC-026", "CF-P0-PC-027", "CF-P0-PC-028", "CF-P0-PC-029",
    "CF-P0-PC-030", "CF-P0-PC-031", "CF-P0-PC-032", "CF-P0-PC-033",
    "CF-P0-PC-034", "CF-P0-PC-035", "CF-P0-PC-036", "CF-P0-PC-037",
    "CF-P0-PC-038", "CF-P0-PC-039", "CF-P0-PC-040", "CF-P0-PC-041",
    "CF-P0-PC-042", "CF-P0-PC-043", "CF-P0-PC-044", "CF-P0-PC-045",
    "CF-P0-PC-046", "CF-P0-PC-047", "CF-P0-PC-048", "CF-P0-PC-049",
    "CF-P0-PC-050", "CF-P0-PC-051", "CF-P0-PC-052",
    "CF-P0-PC-053", "CF-P0-PC-054", "CF-P0-PC-055", "CF-P0-PC-056",
    "CF-P0-PC-057", "CF-P0-PC-058", "CF-P0-PC-059", "CF-P0-PC-060",
    "CF-P0-PC-061", "CF-P0-PC-062", "CF-P0-PC-063", "CF-P0-PC-064",
    "CF-P0-PC-067", "CF-P0-PC-068", "CF-P0-PC-069", "CF-P0-PC-070",
]

H5_SOURCES = [
    "CF-P0-H5-001", "CF-P0-H5-002", "CF-P0-H5-003",
    "CF-P0-H5-004", "CF-P0-H5-005", "CF-P0-H5-006",
    None, None, None,
    "CF-P0-H5-009", "CF-P0-H5-010", "CF-P0-H5-011",
    "CF-P0-H5-012", "CF-P0-H5-013",
    *[f"CF-P0-H5-{number:03d}" for number in range(14, 39)],
    "CF-P0-H5-040", "CF-P0-H5-041", "CF-P0-H5-042",
]

CUSTOM_CASES = {
    ("PC", 3): {
        "title": "点击 Google 登录并成功返回海外主站",
        "module": "海外主站 / 登录 / Google 登录",
        "execution": "第三方账号依赖（自动化检查入口、授权页和回跳）",
        "steps": [
            "使用干净 Browser Context 打开海外主站。",
            "点击 Google 登录按钮，确认进入真实 Google 授权链路。",
            "使用获准的测试账号完成授权；若环境禁止第三方登录，只验证授权入口与回跳地址并记录 BLOCKED。",
        ],
        "expected": [
            "Google 登录入口可用且授权请求参数完整。",
            "授权成功后返回 codeflying.app，并建立海外站登录态。",
        ],
    },
    ("PC", 4): {
        "title": "用户输入正确邮箱和密码",
        "module": "海外主站 / 登录 / 邮箱密码登录",
        "execution": "可自动化",
        "steps": ["打开海外主站邮箱密码登录页。", "输入配置的海外测试邮箱和密码。"],
        "expected": ["表单接受合法邮箱和密码，提交按钮进入可用状态。"],
    },
    ("PC", 5): {
        "title": "邮箱密码登录成功",
        "module": "海外主站 / 登录 / 邮箱密码登录",
        "execution": "可自动化",
        "steps": ["提交正确的海外测试邮箱和密码。", "等待登录请求和页面跳转完成。"],
        "expected": ["登录成功并进入海外站登录后页面。", "刷新页面后登录态仍有效。"],
    },
    ("H5", 7): {
        "title": "H5 点击 Google 登录并成功返回",
        "module": "海外H5 / 登录 / Google 登录",
        "execution": "第三方账号依赖（自动化检查入口、授权页和回跳）",
        "steps": [
            "使用移动端 viewport 打开海外 H5 首页。",
            "点击 Google 登录并验证授权入口。",
            "使用获准的测试账号完成授权；环境不支持时记录 BLOCKED。",
        ],
        "expected": ["授权成功后回到海外 H5，并建立登录态。"],
    },
    ("H5", 8): {
        "title": "H5 用户输入正确邮箱和密码",
        "module": "海外H5 / 登录 / 邮箱密码登录",
        "execution": "可自动化",
        "steps": ["打开海外 H5 邮箱密码登录页。", "输入配置的海外测试邮箱和密码。"],
        "expected": ["表单接受合法邮箱和密码，提交按钮进入可用状态。"],
    },
    ("H5", 9): {
        "title": "H5 邮箱密码登录成功",
        "module": "海外H5 / 登录 / 邮箱密码登录",
        "execution": "可自动化",
        "steps": ["提交正确的海外测试邮箱和密码。", "等待登录请求和页面跳转完成。"],
        "expected": ["登录成功并进入海外 H5 登录后首页。"],
    },
}

TITLE_OVERRIDES = {
    ("PC", 54): "点击发布按钮展示发布 H5 弹窗",
    ("H5", 3): "应用列表默认展示“最新”",
}


def transform_domestic(text: str, old_id: str, new_id: str, platform: str) -> str:
    text = text.replace(old_id, new_id)
    text = text.replace("国内PC", "海外PC").replace("国内 H5", "海外 H5").replace("国内H5", "海外H5")
    text = text.replace("国内主站", "海外主站")
    text = text.replace("https://www.codeflying.net/codeflying_h5/", "https://www.codeflying.app/")
    text = text.replace("https://www.codeflying.net", "https://www.codeflying.app")
    text = text.replace("https://dev.codeflying.net", "https://www.codeflying.app")
    text = text.replace("www_codeflying_net", "www_codeflying_app")
    text = text.replace("dev_codeflying_net", "www_codeflying_app")
    text = text.replace("手机号验证码", "邮箱密码")
    text = text.replace("手机号", "邮箱")
    text = text.replace("{phone}", "{email}")
    text = text.replace("_phone", "_email")
    text = text.replace("微信登录", "Google 登录")
    text = text.replace("义乌专区 / 最新 / 热门", "最新 / 热门")
    text = text.replace("`码上飞冒烟测试用例.xmind`", "`码上飞冒烟测试用例--海外版.md`")
    if platform == "H5":
        text = text.replace("真实 H5 入口", "海外 H5 入口")
    return text


def replace_title(text: str, case_id: str, title: str) -> str:
    lines = text.splitlines()
    if lines:
        lines[0] = f"# {case_id} {title}"
    for index, line in enumerate(lines):
        if line.startswith("- 原始 TC："):
            lines[index] = f"- 原始 TC：{title}"
            break
    return "\n".join(lines).rstrip() + "\n"


def custom_markdown(case_id: str, platform: str, spec: dict) -> str:
    platform_name = "海外PC" if platform == "PC" else "海外H5"
    steps = "\n".join(f"{index}. {step}" for index, step in enumerate(spec["steps"], 1))
    expected = "\n".join(f"{index}. {item}" for index, item in enumerate(spec["expected"], 1))
    return f"""# {case_id} {spec['title']}

## 元信息

- 优先级：P0
- 平台：{platform_name}
- FM 模块：{spec['module']}
- Agent 分组：`auth_identity_runner`
- 执行方式：{spec['execution']}
- 来源：`码上飞冒烟测试用例--海外版.md`
- 原始 TC：{spec['title']}

## 前置条件

- 海外站入口：`https://www.codeflying.app/`
- 使用专门的海外测试账号或海外 storage state；禁止复用国内站 cookie。

## 测试步骤

{steps}

## 预期结果

{expected}

## 结果记录

- 状态：PASS / FAIL / BLOCKED
- 证据：截图、最终 URL、关键网络响应；不得记录密码、cookie 或 token。
"""


def find_source(smoke_root: Path, case_id: str) -> Path:
    matches = list(smoke_root.glob(f"domestic-*/**/{case_id}.md"))
    if len(matches) != 1:
        raise RuntimeError(f"{case_id} 应唯一匹配，实际 {len(matches)}")
    return matches[0]


def runner_from_text(text: str) -> str:
    match = re.search(r"Agent 分组：`?([a-z0-9_]+)`?", text)
    if not match:
        raise RuntimeError("case 缺少 Agent 分组")
    return match.group(1)


def assigned_runner(platform: str, number: int) -> str:
    if platform == "PC":
        if 1 <= number <= 5:
            return "auth_access_agent"
        if 6 <= number <= 16:
            return "shell_navigation_agent"
        if 17 <= number <= 20:
            return "invite_credit_agent"
        if 21 <= number <= 37 or 39 <= number <= 41:
            return "membership_credit_agent"
        if number in {38, 42, 43, 44}:
            return "api_key_agent"
        if number in {45, 46, 47, 49, 50, 51, 53, 57, 58}:
            return "app_lifecycle_agent"
        if number in {48, 52, 54, 55, 56, 59}:
            return "app_publish_test_agent"
        if 60 <= number <= 63:
            return "remix_agent"
    if number in {1, 5, 6, 7, 8, 9, 40}:
        return "auth_access_agent"
    if number in {2, 3, 4, 10, 11, 12, 13}:
        return "guest_explore_agent"
    if 15 <= number <= 34 or number in {41, 42}:
        return "app_lifecycle_agent"
    if number == 14:
        return "remix_agent"
    if number in {35, 36, 38, 39}:
        return "membership_credit_agent"
    if number == 37:
        return "profile_support_agent"
    raise RuntimeError(f"未定义海外 {platform}-{number:03d} 的 Agent 归属")


def set_runner(text: str, runner: str) -> str:
    updated, count = re.subn(
        r"(Agent 分组：)`?[a-z0-9_]+`?",
        rf"\1`{runner}`",
        text,
        count=1,
    )
    if count != 1:
        raise RuntimeError("case 缺少可替换的 Agent 分组")
    return updated


def build_platform(smoke_root: Path, platform: str, sources: list[str | None]) -> list[dict]:
    platform_dir = smoke_root / f"overseas-{platform.lower()}"
    rows = []
    for number, source_id in enumerate(sources, 1):
        case_id = f"CF-P0-INTL-{platform}-{number:03d}"
        custom = CUSTOM_CASES.get((platform, number))
        if custom:
            text = custom_markdown(case_id, platform, custom)
            module_dir = "auth"
        else:
            source = find_source(smoke_root, source_id)
            text = transform_domestic(source.read_text(encoding="utf-8"), source_id, case_id, platform)
            module_dir = source.parent.name
        title = TITLE_OVERRIDES.get((platform, number))
        if title:
            text = replace_title(text, case_id, title)
        if (platform, number) == ("H5", 3):
            text = text.replace("“义务专区/义乌专区”", "“最新”")
            text = text.replace("“义务专区”", "“最新”").replace("“义乌专区”", "“最新”")
        text = set_runner(text, assigned_runner(platform, number))
        output = platform_dir / module_dir / f"{case_id}.md"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text, encoding="utf-8")
        heading = text.splitlines()[0]
        rows.append({
            "case_id": case_id,
            "platform": "海外PC" if platform == "PC" else "海外H5",
            "runner": runner_from_text(text),
            "title": heading.split(" ", 2)[2],
            "path": output.relative_to(smoke_root),
        })
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke-root", default="/Users/codeflying-ui-cases/cases/P0/smoke")
    args = parser.parse_args()
    smoke_root = Path(args.smoke_root).resolve()

    rows = build_platform(smoke_root, "PC", PC_SOURCES)
    rows.extend(build_platform(smoke_root, "H5", H5_SOURCES))
    index = [
        "# CodeFlying 海外版 P0 冒烟测试用例",
        "",
        "> 来源：`码上飞冒烟测试用例--海外版.md`",
        "",
        f"- 用例总数：{len(rows)}",
        f"- 海外 PC：{sum(row['platform'] == '海外PC' for row in rows)}",
        f"- 海外 H5：{sum(row['platform'] == '海外H5' for row in rows)}",
        "- 海外 PC/H5 入口：`https://www.codeflying.app/`",
        "",
        "| 用例 ID | 平台 | Agent | 标题 |",
        "|---|---|---|---|",
    ]
    for row in rows:
        index.append(
            f"| [{row['case_id']}]({row['path']}) | {row['platform']} | "
            f"`{row['runner']}` | {row['title']} |"
        )
    (smoke_root / "OVERSEAS.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    print(f"generated={len(rows)} pc={len(PC_SOURCES)} h5={len(H5_SOURCES)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
