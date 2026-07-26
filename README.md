# CodeFlying UI Cases

码上飞 UI 产品可用性测试用例库。

这个仓库只做一件事：让测试同学和自动化测试 Agent（老郭）能快速找到、维护、执行用例。

## 最简单的维护方式

新增用例时，直接按优先级放到对应目录：

```text
cases/
├── P0/        # 核心流程、支付/计费、数据安全、商业化阻断
├── P1/        # 严重体验问题，流程可绕过但影响明显
└── P2/        # 一般体验问题、低频边界问题
```

每个用例文件使用 Markdown。可以一份文件写一条用例，也可以一份文件写一组相关用例。

当前核心 10 条 P0 用例在：

- [cases/P0/CodeFlying_10_robust_evaluation_cases.md](cases/P0/CodeFlying_10_robust_evaluation_cases.md)

应用生成扩展 10 条在：

- [cases/P0/CodeFlying_app_generation_extra_10.md](cases/P0/CodeFlying_app_generation_extra_10.md)

这两份合起来就是当前 demo 套件的 20 条 Markdown 用例。

从 XMind 拆分出的正式 P0 冒烟用例在：

- [cases/P0/smoke/README.md](cases/P0/smoke/README.md)

`cases/P0/smoke/` 采用“逻辑图最终叶子节点一条一个 Markdown”的方式，当前包含 112 条：国内 PC 70 条、国内 H5 42 条。原始 XMind 和提取版 Markdown 仅作为来源文件保留；自动化 runner 以 `cases/P0/smoke/README.md` 和其中的 112 个 Markdown 文件为准。

注意：不按标题中是否出现 `TC：` 来计数，也不合并相同标题。只要是逻辑图中的最终叶子节点，就保留为独立用例；即使同一功能下有“免费版 / 标准版 / 进阶版”等参数叶子，也分别执行、分别记录结果。

## 老郭怎么读取

常用提示词：

```text
请读取 GitHub 仓库：
https://github.com/guoshaung/codeflying_UI_cases

本次只执行 cases/P0 下的 Markdown 用例。
不要读取历史旧用例，不要自行扩展额外用例。

测试环境：dev
平台：国内 PC
登录态：已登录，不测试登录

执行完成后输出 Markdown 报告，必须包含：
1. 总共跑了多少条；
2. PASS / RETRY_PASS / FAIL / BLOCKED / NOT_RUN 数量；
3. P0 / P1 / P2 分层结果；
4. 失败、阻塞、未验证明细；
5. 关键证据路径；
6. 是否建议继续回归。
```

如果只想跑某个优先级，把 `cases/P0` 改成 `cases/P1` 或 `cases/P2` 即可。

如果只想跑正式冒烟用例，请指定：

```text
本次只执行 cases/P0/smoke/ 下的 Markdown 用例。
按文件中的 Agent 分组、账号类型、数据锁和人工测试原因执行。
```

## 新增用例格式

复制模板：

- [templates/case-template.md](templates/case-template.md)

每条用例至少写清楚：

- 用例 ID
- 标题
- 优先级：P0 / P1 / P2
- 模块
- 平台：国内 PC / 国内 H5 / 海外 PC / 海外 H5
- 执行方式：可自动化 / 真人依赖 / agent 行为评测
- 前置条件
- 测试步骤
- 预期结果
- 通过标准
- 失败条件
- 证据要求

## 几条硬规则

1. 登录可以是前置条件；如果本次不测登录，不要把登录计入用例数。
   手机号验证码登录专项可自动化，口径是“测试环境 mock 验证码”：点击获取验证码后，用老郭登录技能的 `get_redis_code.py` 从测试 Redis/mock 服务读取验证码再登录。Redis/mock 不可用时标记 `BLOCKED_MOCK_OTP_UNAVAILABLE`，不要写成“登录类没有 mock 能力”。
   一轮全量/冒烟测试中 mock OTP 登录只执行一次；执行成功后保存并复用本轮 session，其他业务 runner 必须跳过登录。
2. 支付要拆开：二维码生成、mock/沙箱支付、真实扫码支付不是同一件事。
   当前 P0 冒烟阶段，会员/积分/购买类用例统一复用一个稳定的已登录测试账号；
   能打开购买入口并弹出二维码或 mock 支付弹窗即可通过，真实扫码和扣款不在自动化门禁内。
3. 下载源码入口是图标按钮，不能只搜可见文案。必须优先检查 DOM：`.download-button`、`[class*="download"]`、`[title*="下载"]`、`[aria-label*="下载"]`、`aria-describedby` 关联 tooltip；hover 后 tooltip 为“下载源码”也算找到入口。找到入口后仍必须验证文件真实落盘、大小大于 0、文件可读。
4. 列表类用例不要绑定动态内容。比如“应用列表默认展示义乌专区/义务专区”按 Tab/栏目元素是否存在和默认激活来判定，不要求具体应用卡片内容固定。
5. 国内 H5 必须使用真实 H5 入口 `https://www.codeflying.net/codeflying_h5/`，不能只打开 PC 站后调整浏览器分辨率。工作台应用操作类用例要在 H5 外层应用卡片上测试：先找到稳定、非转圈的应用卡片，再点击应用名称旁的三点/更多操作按钮，验证底部半屏菜单中的“分享应用 / 查看对话过程 / 修改名称 / 发布应用 / 删除应用”等入口。除非用例明确要求进入预览页，不要先点击应用卡片主体。
6. 分享给好友、分享应用、做同款等依赖系统分享面板、账号额度或复制副作用的用例，自动化优先验证入口、弹窗/跳转、关键接口触发；其中“复制链接”必须点击复制按钮后读取剪贴板，确认剪贴板内容为非空 URL 且与弹窗展示链接一致或包含同一分享地址。若后续依赖真实系统分享、外部 App 或不可控额度，标记 `BLOCKED` / `MANUAL_REQUIRED`，不得硬判失败。
7. 应用创建/生成类用例只验证产品是否接收需求并给出首条有效反馈。发送生成请求后，如果前端出现“你想生成什么类型/选择应用类型/网站/小程序/H5/应用”等请求确认卡片，统一选择默认推荐项或第一个可用项并点击“确认/继续/开始生成/生成应用”。确认后只要出现“收到/我先想想/正在为你生成/需求已接收/非空助手回复”等有效反馈即可通过；不要等待完整应用生成完成。
8. 二维码必须验证图片资源加载正常；能扫码/能解码时再写“可识别”。
9. P0 有失败、阻塞或证据不足时，报告不能写“全部通过”或“建议上线”。

更多维护说明见：

- [docs/maintenance.md](docs/maintenance.md)
- [docs/test-accounts.md](docs/test-accounts.md)
