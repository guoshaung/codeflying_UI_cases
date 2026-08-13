# CF-P0-PC-023 通过邀请链接注册新用户并验证邀请人积分到账

- 优先级：P0
- 模块：国内主站 / 侧边栏 / 赚取积分
- 平台：国内PC
- 执行方式：可自动化
- 问题类型：产品体验
- 用户类型：免费用户
- 前置条件：国内免费邀请人的已有 session 可用，禁止现场短信登录邀请人；为被邀请人生成本轮动态测试手机号，注册前确认该手机号不存在，执行后清理测试被邀请人、邀请关系与奖励记录。若 OTP 已成功收到，不得因页面曾出现滑块就直接判定阻塞，继续完成注册和奖励校验。
- Agent 分组：invite_credit_agent
- 账号类型：fixed_inviter_account + generated_new_phone
- 是否修改数据：yes
- 数据锁：`invitation:{inviter_id}`
- 清理动作：清理测试被邀请人账号、邀请关系与测试奖励记录；清理失败标记 `CLEANUP_FAILED`
- 人工测试原因：无

## 测试步骤

1. `invite_credit_agent` 不启动浏览器，立即通过 `agent` 调用 `invite_registration_agent`，传入本 case、`FREE_SESSION`、OTP 脚本、`EVIDENCE_DIR`和 `RESULT_DIR`。
2. 子 Agent 运行 `run_pc023.py`，直接加载已有邀请人 session，进入“赚取积分”，记录邀请人积分或奖励流水前值，保存 `inviter-before.png`，复制包含邀请标识的完整链接；不得为邀请人重新发送验证码。
3. 子 Agent 在隔离 Context 中使用本轮唯一、未注册的动态手机号打开邀请链接，运行指定脚本发送并读取 OTP，完成注册并保存 `invitee-registered.png`。
4. 子 Agent 再次加载免费账户 session，最多等待 60 秒，每 5 秒刷新积分或奖励流水。
5. 子 Agent 记录后值、差值或新增奖励流水，保存 `inviter-after.png`，返回完整结构化结果。父 Agent 只校验证据并写最终结果，不再打开第二个浏览器补测。

## 预期结果

1. 新手机号通过邀请链接完成注册，且邀请标识未丢失。
2. 邀请人积分正确增加，或出现与本次被邀请人对应的新增奖励流水。

## 通过标准

- “新用户注册成功”和“邀请人奖励到账”必须同时成立。
- 证据必须包含 `inviter-before.png`、`invitee-registered.png`、`inviter-after.png`，以及积分前值/后值/差值或新增奖励流水。
- 自动化证据完整；若有重试，必须记录首次错误并标记 `RETRY_PASS`。

## 失败条件

- 新用户注册成功但奖励未下发、奖励下发对象错误、重复下发、接口报错、页面不可继续操作，或清理失败未标记 `CLEANUP_FAILED`。

## 阻塞条件

- OTP/Redis 确认不可达，滑块发码脚本连续两次失败，或必要 session 无效。必须写明阻塞发生的具体阶段；两次失败后禁止手工拖拽或猜测滑块距离。

## 证据要求

- `inviter-before.png`、`invitee-registered.png`、`inviter-after.png`。
- 页面 URL 与关键 DOM 状态。
- 相关业务接口结果；HTTP 200 仍需检查业务码与返回数据。
- 涉及数据变化时，保存变化前后数据及清理结果。

## 备注

- 若当前没有已授权的清理工具，不修改后端代码或数据；保留待清理标识并加注 `CLEANUP_REQUIRED`。
