# CF-P0-PC-062 公开应用点击查看详情后全屏展示

- 优先级：P0
- 模块：国内主站 / 应用广场 / 应用详情
- 平台：国内PC
- 执行方式：可自动化
- 用户类型：会员用户
- Agent 分组：remix_agent
- 账号类型：`member_account`
- 账号与域名：`MEMBER_SESSION` + `https://www.codeflying.net/`
- 是否修改数据：no
- 清理动作：无

## 前置条件

1. 只使用总控传入的 `MEMBER_SESSION`，在会员 Browser Context 中加载一次。
2. 应用广场至少有一个已加载完成、非转圈、可点击“查看详情”或“在线体验”的公开应用。
3. 本用例和 `CF-P0-PC-063` 复用同一个会员 Browser Context；不得再次加载 session。

## 测试步骤

1. 打开国内主站的应用广场，等待公开应用卡片加载完成。
2. 选择一个稳定的公开应用，记录应用名称或 app id，截图为 `CF-P0-PC-062-before.png`。
3. 点击该卡片的“查看详情”或“在线体验”入口。
4. 等待详情层加载完成，记录 URL、标题、关闭入口和“做同款”等价按钮状态，截图为 `CF-P0-PC-062-after.png`。
5. 本 case 立即写入独立 `result.json`，保留详情层供 `CF-P0-PC-063` 继续执行。

## 通过标准

- 详情层覆盖页面主要可视区，不是卡片内的小尺寸预览。
- 详情内容已加载，无长时间转圈、白屏或未处理报错。
- 可见关闭入口，且可见“做同款”、`Remix`、`Duplicate`、`Copy` 或 `Clone` 中任一等价按钮。

## 失败与阻塞

- 点击后未打开详情层，或详情层白屏/持续转圈：`FAIL`。
- 会员 session 缺失或已失效：`BLOCKED_ACCOUNT_REQUIRED`。
- 应用广场没有任何可用的公开应用：`BLOCKED_TEST_DATA`。

## 证据要求

- `CF-P0-PC-062-before.png`
- `CF-P0-PC-062-after.png`
- 页面 URL、应用名称或 app id、详情层标题、关闭入口和做同款按钮的 DOM 状态
