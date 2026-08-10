# CF-P0-PC-063 有可用额度时做同款并出现在我的应用

- 优先级：P0
- 模块：国内主站 / 应用广场 / 做同款
- 平台：国内PC
- 执行方式：可自动化
- 用户类型：会员用户
- Agent 分组：remix_agent
- 账号类型：`member_account`
- 账号与域名：`MEMBER_SESSION` + `https://www.codeflying.net/`
- 是否修改数据：yes
- 数据锁：`remix:member_account`
- 清理动作：只删除本用例新增的 app id

## 前置条件

1. 继续使用 `CF-P0-PC-062` 已加载的会员 Browser Context 和已打开的公开应用详情层；不得重载 session。
2. 会员账号当前至少有 1 个可创建应用额度。
3. 测试前能获取“我的应用”中现有 app id 集合，用于识别本轮新增应用。

## 测试步骤

1. 记录点击前“我的应用”的 app id 集合，截图为 `CF-P0-PC-063-before.png`。
2. 在 `CF-P0-PC-062` 的详情层中，点击“做同款”、`Remix`、`Duplicate`、`Copy` 或 `Clone` 中实际可见的等价按钮。
3. 等待复制接口返回业务成功，或等待页面进入新应用路由。
4. 进入“我的应用”，对比点击前后 app id 集合，得到唯一的 `new_app_id`，截图为 `CF-P0-PC-063-after.png`。
5. 本 case 立即写入独立 `result.json`，其中必须记录 `new_app_id`。
6. 只删除 `new_app_id`，再次核对点击前已存在的 app id 均保留，记录清理结果。

## 通过标准

- 做同款按钮可见且可点击。
- 复制接口业务成功，或页面进入携带新 app id 的新应用路由。
- “我的应用”中出现点击前不存在的唯一 `new_app_id`。
- 本轮新增应用已清理，原有应用未被删除。

## 失败与阻塞

- 按钮明明可见但选择器未命中，或点击后复制业务失败：`FAIL`，不得写 `BLOCKED`。
- 明确出现额度不足或会员升级弹窗：`BLOCKED_TEST_DATA`，表示“可用额度≥1”前置不成立。
- 会员 session 缺失或已失效：`BLOCKED_ACCOUNT_REQUIRED`。
- 新应用删除失败：保留业务断言结果，另加 `CLEANUP_FAILED` 并记录 `new_app_id`。

## 证据要求

- `CF-P0-PC-063-before.png`
- `CF-P0-PC-063-after.png`
- 复制接口的 HTTP 状态和业务码（HTTP 200 不等于业务成功）
- 点击前 app id 集合、`new_app_id`、点击后 app id 集合和清理结果
