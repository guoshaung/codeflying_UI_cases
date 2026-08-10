# CF-P0-PC-023 通过邀请链接注册新用户并验证邀请人积分到账

- 优先级：P0
- 模块：国内主站 / 侧边栏 / 赚取积分
- 平台：国内PC
- 执行方式：可自动化
- 问题类型：产品体验
- 用户类型：免费用户 / 付费用户
- 前置条件：固定邀请人已登录；为本轮生成动态测试手机号，注册前确认该手机号不存在，执行后清理测试被邀请人、邀请关系与奖励记录。若 OTP 已成功收到，不得因页面曾出现滑块就直接判定阻塞，继续完成登录和奖励校验。
- Agent 分组：invite_credit_agent
- 账号类型：fixed_inviter_account + generated_new_phone
- 是否修改数据：yes
- 数据锁：`invitation:{inviter_id}`
- 清理动作：清理测试被邀请人账号、邀请关系与测试奖励记录；清理失败标记 `CLEANUP_FAILED`
- 人工测试原因：无

## 测试步骤

1. 创建邀请人 member/www 独立 Browser Context，加载 `MEMBER_SESSION`，进入“赚取积分”。
2. 记录邀请人当前积分数值或奖励流水，保存 `inviter-before.png`；复制完整邀请链接并确认链接含邀请标识。
3. 生成本轮唯一、未注册的动态手机号。通过 `agent` 调用 `invite_registration_agent`，传入 case 路径、邀请链接、手机号、OTP 脚本路径、`EVIDENCE_DIR`和 `RESULT_DIR`。
4. 子 Agent 在全新 dev Browser Context 打开邀请链接，运行指定脚本发送并读取 OTP，完成新用户注册，保存 `invitee-registered.png`并返回可见的用户标识。
5. 父 Agent 回到步骤 1 的 member/www Context，刷新积分或奖励流水；最多等待 60 秒，每 5 秒检查一次。
6. 记录后值、差值或新增奖励流水，保存 `inviter-after.png`。记录被邀请人手机号、可见用户 ID、邀请标识和奖励标识供后续清理。

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

- OTP/Redis 确认不可达，滑块发码脚本连续两次失败，或必要 session 无效。必须写明阻塞发生的具体阶段。

## 证据要求

- `inviter-before.png`、`invitee-registered.png`、`inviter-after.png`。
- 页面 URL 与关键 DOM 状态。
- 相关业务接口结果；HTTP 200 仍需检查业务码与返回数据。
- 涉及数据变化时，保存变化前后数据及清理结果。

## 备注

- 若当前没有已授权的清理工具，不修改后端代码或数据；保留待清理标识并加注 `CLEANUP_REQUIRED`。
