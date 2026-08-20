# CF-P0-PC-004 用户输入手机号点击获取验证码，验证码可发送至用户

- 优先级：P0
- 模块：国内主站 / 登录 / 手机号验证码登录
- 平台：国内PC
- 执行方式：可自动化
- 问题类型：产品体验
- 用户类型：免费用户 / 付费用户
- 前置条件：测试环境可访问；固定测试手机号 `17710753306` 已获授权用于验证码登录；老郭环境可访问 `send_launch_code` 和测试 Redis。
- Agent 分组：auth_access_agent
- 账号类型：free-dev-phone (`17710753306`) + mock-otp
- 是否修改数据：no
- 数据锁：`account:{phone}`
- 清理动作：清理动态测试账号及登录会话
- 人工测试原因：无

## 测试步骤

1. 创建独立的 国内PC Browser Context，清除登录态，打开 `https://dev.codeflying.net`。
2. 进入手机号验证码登录页，在手机号输入框填写固定测试号 `17710753306`，记录获取验证码按钮可见证据。
3. 本轮只通过 task 绑定 launcher 派发一次 `CF-P0-PC-004`：

   ```bash
   python3 "<task.execution_contract.launcher.script 绝对路径>" \
     --task-bundle "<task-bundle绝对路径>" \
     --case-ids "CF-P0-PC-004"
   ```

   launcher 会执行 task 中已绑定 path/SHA 的 `get_redis_code.py`：先打开 dev PC 登录页完成滑块并触发浏览器发码，再轮询 Redis key `sms_code:17710753306:login:code`，并生成 execution receipt。禁止用无 captcha token 的 raw `send_launch_code` 请求代替浏览器流程，也禁止直接运行该脚本。
4. 验证脚本返回：Redis 取码成功、TTL 大于 0；接口响应作为独立证据记录，不要求 `send_launch_code` 在滑块场景下业务成功。
5. 记录页面按钮、接口业务响应、Redis key/TTL 和截图；报告不得暴露完整验证码。

## 预期结果

1. 能从测试 Redis 读取到固定手机号对应的有效验证码和 TTL，说明验证码链路可用于自动化登录。
2. `send_launch_code` 的 HTTP/业务响应被记录；若 dev 滑块阻断接口直发，则以 Redis 最终写入作为通过依据。
3. 页面无白屏、无未处理报错，相关功能可继续操作。

## 通过标准

- 目标页面、弹窗、状态或数据变化与测试点描述一致。
- 自动化证据完整；若有重试，必须记录首次错误并标记 `RETRY_PASS`。

## 失败条件

- 目标结果未出现、出现错误状态、数据不一致或页面不可继续操作。
- Redis 在等待窗口内没有产生该手机号验证码。

## 阻塞条件

- 测试环境、账号、第三方服务或必要测试数据不可用。
- 仅当接口或 Redis 确实不可连接时标记 `BLOCKED_MOCK_OTP_UNAVAILABLE`；滑块未处理时应提示人工先过滑块，再读取 Redis 中已写入验证码，不得写成 mock OTP 基础设施不可用。

## 证据要求

- 操作前后截图。
- 页面 URL 与关键 DOM 状态。
- 相关业务接口结果；HTTP 200 仍需检查业务码与返回数据。
- 涉及数据变化时，保存变化前后数据及清理结果。

## 备注

- 固定测试手机号只用于测试环境；全量测试每轮只触发一次验证码，H5-007/008 复用本用例与 PC-005 的证据/session。
- free/dev 测试手机号只用于测试环境；全量测试每轮只触发一次验证码，H5-007/008 复用本用例与 PC-005 的证据/session。
- member 账号手机号 `19113720926` 不能用于 OTP；若 agent 从 session/currentUser 读到该手机号，必须忽略并改用 `17710753306`。
