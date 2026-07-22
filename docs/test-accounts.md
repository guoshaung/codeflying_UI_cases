# 测试账号与 Playwright Session 约定

本仓库不保存手机号、验证码、Cookie、Token 或任何真实凭据，只定义自动化测试需要的账号角色。

## 固定账号角色

| 账号类型 | 用途 | 权益要求 | 缺失时处理 |
| --- | --- | --- | --- |
| `member_account` | 会员下载源码、全天候预览、会员权益展示 | 会员 / 有下载权益 / 有对应会员能力 | 标记 `BLOCKED_ACCOUNT_REQUIRED` |
| `free_account` | 非会员下载触发付费弹窗、升级解锁弹窗 | 免费 / 无下载权益 / 无对应会员能力 | 标记 `BLOCKED_ACCOUNT_REQUIRED` |
| `default-playwright-session` | 普通登录态测试，不关心会员差异 | 稳定可登录 | 标记 `BLOCKED_ACCOUNT_REQUIRED` |
| `anonymous` | 未登录首页、注册、登录入口 | 不加载登录态 | 直接新建无 storageState 的 Browser Context |
| `fixed_inviter_account` | 邀请、赚取积分、推荐奖励 | 固定邀请人，可复制邀请链接 | 标记 `BLOCKED_ACCOUNT_REQUIRED` |
| `generated_new_phone` | 新用户注册奖励链路 | 执行前必须不存在，执行后必须清理 | 标记 `BLOCKED_ACCOUNT_REQUIRED` |
| `fixed_existing_phone` | 非新用户不发奖励链路 | 已注册老用户，不应再次触发新用户奖励 | 标记 `BLOCKED_ACCOUNT_REQUIRED` |

## Session 文件建议

实际执行时由测试环境或老郭工作目录提供 session 文件，建议命名为：

- `member_account_dev_codeflying_net_state.json`
- `free_account_dev_codeflying_net_state.json`
- `default_dev_codeflying_net_state.json`
- `member_account_www_codeflying_net_state.json`
- `free_account_www_codeflying_net_state.json`
- `default_www_codeflying_net_state.json`

如果历史目录里只有 `dev_codeflying_net_state.json`，且该账号是尊享/会员账号，可临时映射为 `member_account`，但必须在测试报告里记录这个映射。

## 执行规则

1. 不建议通过手工改数据库会员状态来制造会员/非会员账号；优先使用固定账号和固定 session。
2. 非会员账号可以通过测试手机号注册一次后固定下来，但注册完成后不要每轮重新创建。
3. 会员/非会员差异用例必须记录本轮实际使用的账号类型，不要把会员账号拿去跑非会员弹窗用例。
4. 如果缺少对应 session，标记 `BLOCKED_ACCOUNT_REQUIRED`，不得判定产品失败。

## 邀请新用户用例

邀请类用例采用“固定邀请人 + 动态新手机号 + 执行后清理”的策略：

1. 使用 `fixed_inviter_account` 登录，进入“赚取积分”页面并复制邀请链接。
2. 为每轮测试生成一个专用手机号，建议使用测试号段或平台 mock 手机号，例如 `199TEST{run_id}` 这种可追踪模式；不得使用真实用户手机号。
3. 注册前必须确认该手机号不存在；如果无法确认，标记 `BLOCKED_ACCOUNT_REQUIRED`。
4. 通过邀请链接完成新用户注册/登录，记录邀请人积分前后变化、被邀请人账号 ID、邀请关系和奖励流水。
5. 用例结束后必须清理测试被邀请人、邀请关系和测试奖励记录；清理失败时报告标记 `CLEANUP_FAILED`，并列出需要人工清理的数据 ID。
6. “非新用户注册奖励不下发”使用 `fixed_existing_phone`，不能用刚生成的新手机号复测。
