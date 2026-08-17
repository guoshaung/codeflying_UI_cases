# CodeFlying 海外版 P0 冒烟测试用例

> 来源：`码上飞冒烟测试用例--海外版.md`

- 用例总数：105
- 海外 PC：63
- 海外 H5：42
- 海外 PC/H5 入口：`https://www.codeflying.app/`

| 用例 ID | 平台 | Agent | 标题 |
|---|---|---|---|
| [CF-P0-INTL-PC-001](overseas-pc/guest-home/CF-P0-INTL-PC-001.md) | 海外PC | `auth_access_agent` | 点击登录按钮跳转至登录页 |
| [CF-P0-INTL-PC-002](overseas-pc/guest-home/CF-P0-INTL-PC-002.md) | 海外PC | `auth_access_agent` | 输入文案点击立即开发跳转至登录页 |
| [CF-P0-INTL-PC-003](overseas-pc/auth/CF-P0-INTL-PC-003.md) | 海外PC | `auth_access_agent` | 点击 Google 登录并成功返回海外主站 |
| [CF-P0-INTL-PC-004](overseas-pc/auth/CF-P0-INTL-PC-004.md) | 海外PC | `auth_access_agent` | 用户输入正确邮箱和密码 |
| [CF-P0-INTL-PC-005](overseas-pc/auth/CF-P0-INTL-PC-005.md) | 海外PC | `auth_access_agent` | 邮箱密码登录成功 |
| [CF-P0-INTL-PC-006](overseas-pc/top-nav/CF-P0-INTL-PC-006.md) | 海外PC | `shell_navigation_agent` | 左侧展示码上飞logo 点击进入应用广场页面 |
| [CF-P0-INTL-PC-007](overseas-pc/top-nav/CF-P0-INTL-PC-007.md) | 海外PC | `shell_navigation_agent` | 点击充值会员 弹出购买会员弹窗 |
| [CF-P0-INTL-PC-008](overseas-pc/top-nav/CF-P0-INTL-PC-008.md) | 海外PC | `shell_navigation_agent` | 用户可根据枚举选择语言类型 |
| [CF-P0-INTL-PC-009](overseas-pc/top-nav/CF-P0-INTL-PC-009.md) | 海外PC | `shell_navigation_agent` | 选中语言类型后页面文案随机切换对应语种文案 |
| [CF-P0-INTL-PC-010](overseas-pc/app-square/CF-P0-INTL-PC-010.md) | 海外PC | `shell_navigation_agent` | 点击跳转至应用广场页面 |
| [CF-P0-INTL-PC-011](overseas-pc/app-square/CF-P0-INTL-PC-011.md) | 海外PC | `shell_navigation_agent` | 顶部tab默认展示首位 |
| [CF-P0-INTL-PC-012](overseas-pc/app-square/CF-P0-INTL-PC-012.md) | 海外PC | `shell_navigation_agent` | 切换tab展示对应页面内容 |
| [CF-P0-INTL-PC-013](overseas-pc/my-apps/CF-P0-INTL-PC-013.md) | 海外PC | `shell_navigation_agent` | 点击跳转至应我的应用页面 |
| [CF-P0-INTL-PC-014](overseas-pc/my-apps/CF-P0-INTL-PC-014.md) | 海外PC | `shell_navigation_agent` | 顶部tab默认展示该用户全部应用 |
| [CF-P0-INTL-PC-015](overseas-pc/my-apps/CF-P0-INTL-PC-015.md) | 海外PC | `shell_navigation_agent` | 点击未发布tab展示该用户已创建未发布、创建中的应用 |
| [CF-P0-INTL-PC-016](overseas-pc/my-apps/CF-P0-INTL-PC-016.md) | 海外PC | `shell_navigation_agent` | 点击已发布tab展示该用户已发布的应用 |
| [CF-P0-INTL-PC-017](overseas-pc/earn-points/CF-P0-INTL-PC-017.md) | 海外PC | `invite_credit_agent` | 点击跳转至应赚取积分页面 |
| [CF-P0-INTL-PC-018](overseas-pc/earn-points/CF-P0-INTL-PC-018.md) | 海外PC | `invite_credit_agent` | 点击复制链接按钮可将邀请链接复制至剪切板 |
| [CF-P0-INTL-PC-019](overseas-pc/earn-points/CF-P0-INTL-PC-019.md) | 海外PC | `invite_credit_agent` | 成功邀请新用户登录可正常下发对应积分 |
| [CF-P0-INTL-PC-020](overseas-pc/earn-points/CF-P0-INTL-PC-020.md) | 海外PC | `invite_credit_agent` | 非新用户注册奖励不下发 |
| [CF-P0-INTL-PC-021](overseas-pc/entitlements/CF-P0-INTL-PC-021.md) | 海外PC | `membership_credit_agent` | 每日免费积分展示每日获赠积分数及剩余积分数 / 每日获赠100积分 |
| [CF-P0-INTL-PC-022](overseas-pc/entitlements/CF-P0-INTL-PC-022.md) | 海外PC | `membership_credit_agent` | 会员每月积分展示对应会员等级获赠积分数及当前剩余积分数 / 免费版  0 |
| [CF-P0-INTL-PC-023](overseas-pc/entitlements/CF-P0-INTL-PC-023.md) | 海外PC | `membership_credit_agent` | 会员每月积分展示对应会员等级获赠积分数及当前剩余积分数 / 标准版 3000 |
| [CF-P0-INTL-PC-024](overseas-pc/entitlements/CF-P0-INTL-PC-024.md) | 海外PC | `membership_credit_agent` | 会员每月积分展示对应会员等级获赠积分数及当前剩余积分数 / 进阶版 6600 |
| [CF-P0-INTL-PC-025](overseas-pc/entitlements/CF-P0-INTL-PC-025.md) | 海外PC | `membership_credit_agent` | 会员每月积分展示对应会员等级获赠积分数及当前剩余积分数 / 尊享版 27600 |
| [CF-P0-INTL-PC-026](overseas-pc/entitlements/CF-P0-INTL-PC-026.md) | 海外PC | `membership_credit_agent` | 自购积分包展示用户购买积分数及当前剩余积分数 |
| [CF-P0-INTL-PC-027](overseas-pc/entitlements/CF-P0-INTL-PC-027.md) | 海外PC | `membership_credit_agent` | 剩余可创建应用数展示对应会员等级可创建数量及剩余可创建数量 / 免费版  2 |
| [CF-P0-INTL-PC-028](overseas-pc/entitlements/CF-P0-INTL-PC-028.md) | 海外PC | `membership_credit_agent` | 剩余可创建应用数展示对应会员等级可创建数量及剩余可创建数量 / 标准版 10 |
| [CF-P0-INTL-PC-029](overseas-pc/entitlements/CF-P0-INTL-PC-029.md) | 海外PC | `membership_credit_agent` | 剩余可创建应用数展示对应会员等级可创建数量及剩余可创建数量 / 进阶版 无限 |
| [CF-P0-INTL-PC-030](overseas-pc/entitlements/CF-P0-INTL-PC-030.md) | 海外PC | `membership_credit_agent` | 剩余可创建应用数展示对应会员等级可创建数量及剩余可创建数量 / 尊享版 无限 |
| [CF-P0-INTL-PC-031](overseas-pc/entitlements/CF-P0-INTL-PC-031.md) | 海外PC | `membership_credit_agent` | 展示用户邀请新用户获得的积分及剩余积分 |
| [CF-P0-INTL-PC-032](overseas-pc/entitlements/CF-P0-INTL-PC-032.md) | 海外PC | `membership_credit_agent` | 点击展示积分消耗明细弹窗 |
| [CF-P0-INTL-PC-033](overseas-pc/settings-billing/CF-P0-INTL-PC-033.md) | 海外PC | `membership_credit_agent` | 正常展示用户头像 |
| [CF-P0-INTL-PC-034](overseas-pc/settings-billing/CF-P0-INTL-PC-034.md) | 海外PC | `membership_credit_agent` | 正确展示用户昵称 |
| [CF-P0-INTL-PC-035](overseas-pc/settings-billing/CF-P0-INTL-PC-035.md) | 海外PC | `membership_credit_agent` | 正常展示音色名称 |
| [CF-P0-INTL-PC-036](overseas-pc/settings-billing/CF-P0-INTL-PC-036.md) | 海外PC | `membership_credit_agent` | 倒序展示仅三条支付数据 |
| [CF-P0-INTL-PC-037](overseas-pc/settings-billing/CF-P0-INTL-PC-037.md) | 海外PC | `membership_credit_agent` | 点击后弹窗倒序展示用户所有支付数据 |
| [CF-P0-INTL-PC-038](overseas-pc/settings-billing/CF-P0-INTL-PC-038.md) | 海外PC | `api_key_agent` | 点进入API服务页面 |
| [CF-P0-INTL-PC-039](overseas-pc/settings-billing/CF-P0-INTL-PC-039.md) | 海外PC | `membership_credit_agent` | 点击充值积分弹出购买弹窗 |
| [CF-P0-INTL-PC-040](overseas-pc/settings-billing/CF-P0-INTL-PC-040.md) | 海外PC | `membership_credit_agent` | 剩余积分展示用户当前剩余总积分数 |
| [CF-P0-INTL-PC-041](overseas-pc/settings-billing/CF-P0-INTL-PC-041.md) | 海外PC | `membership_credit_agent` | 本月已用积分展示用户本月已使用积分 |
| [CF-P0-INTL-PC-042](overseas-pc/settings-billing/CF-P0-INTL-PC-042.md) | 海外PC | `api_key_agent` | 点击复制按钮可成功将密钥复制进剪切板 |
| [CF-P0-INTL-PC-043](overseas-pc/settings-billing/CF-P0-INTL-PC-043.md) | 海外PC | `api_key_agent` | 点击删除按钮可成功删除当前密钥 |
| [CF-P0-INTL-PC-044](overseas-pc/settings-billing/CF-P0-INTL-PC-044.md) | 海外PC | `api_key_agent` | 点击创建新密钥 可成功创建新密钥信息 |
| [CF-P0-INTL-PC-045](overseas-pc/app-create/CF-P0-INTL-PC-045.md) | 海外PC | `app_lifecycle_agent` | 点击立即开发按钮进入需求澄清页面 |
| [CF-P0-INTL-PC-046](overseas-pc/app-create/CF-P0-INTL-PC-046.md) | 海外PC | `app_lifecycle_agent` | 进入对话页面 |
| [CF-P0-INTL-PC-047](overseas-pc/app-create/CF-P0-INTL-PC-047.md) | 海外PC | `app_lifecycle_agent` | 提示词文案进入文本输入框 |
| [CF-P0-INTL-PC-048](overseas-pc/app-preview/CF-P0-INTL-PC-048.md) | 海外PC | `app_publish_test_agent` | 应用完成后自动跳转至应用预览页默认展示应用页面 |
| [CF-P0-INTL-PC-049](overseas-pc/app-preview/CF-P0-INTL-PC-049.md) | 海外PC | `app_lifecycle_agent` | 点击管理后台可跳转至应用管理后台页面 |
| [CF-P0-INTL-PC-050](overseas-pc/app-preview/CF-P0-INTL-PC-050.md) | 海外PC | `app_lifecycle_agent` | 点击助手配置可打开助手配置页面 |
| [CF-P0-INTL-PC-051](overseas-pc/app-preview/CF-P0-INTL-PC-051.md) | 海外PC | `app_lifecycle_agent` | 会员用户点击下载按钮用户可将项目代码下载至本地 |
| [CF-P0-INTL-PC-052](overseas-pc/app-preview/CF-P0-INTL-PC-052.md) | 海外PC | `app_publish_test_agent` | 非会员用户点击触发付费弹窗 |
| [CF-P0-INTL-PC-053](overseas-pc/app-preview/CF-P0-INTL-PC-053.md) | 海外PC | `app_lifecycle_agent` | 点击刷新按钮刷新应用展示 |
| [CF-P0-INTL-PC-054](overseas-pc/app-preview/CF-P0-INTL-PC-054.md) | 海外PC | `app_publish_test_agent` | 点击发布按钮展示发布 H5 弹窗 |
| [CF-P0-INTL-PC-055](overseas-pc/app-preview/CF-P0-INTL-PC-055.md) | 海外PC | `app_publish_test_agent` | 手机扫码可正常访问应用h5页面 |
| [CF-P0-INTL-PC-056](overseas-pc/app-preview/CF-P0-INTL-PC-056.md) | 海外PC | `app_publish_test_agent` | 点击复制按钮可将应用分享链接复制进剪切板 |
| [CF-P0-INTL-PC-057](overseas-pc/app-preview/CF-P0-INTL-PC-057.md) | 海外PC | `app_lifecycle_agent` | 会员用户点击“好呀”开启全天候预览 |
| [CF-P0-INTL-PC-058](overseas-pc/app-preview/CF-P0-INTL-PC-058.md) | 海外PC | `app_lifecycle_agent` | 开启全天候预览时不展示剩余时长 |
| [CF-P0-INTL-PC-059](overseas-pc/app-preview/CF-P0-INTL-PC-059.md) | 海外PC | `app_publish_test_agent` | 非会员用户点击升级解锁按钮弹出付费弹窗 |
| [CF-P0-INTL-PC-060](overseas-pc/copy-app/CF-P0-INTL-PC-060.md) | 海外PC | `remix_agent` | 应用广场点击应用，展示应用体验弹窗 |
| [CF-P0-INTL-PC-061](overseas-pc/copy-app/CF-P0-INTL-PC-061.md) | 海外PC | `remix_agent` | 点击查看详情 进入全屏展示 |
| [CF-P0-INTL-PC-062](overseas-pc/copy-app/CF-P0-INTL-PC-062.md) | 海外PC | `remix_agent` | 当前可创建应用数量大于等于1时，可将应用复制在我的应用列表中 |
| [CF-P0-INTL-PC-063](overseas-pc/copy-app/CF-P0-INTL-PC-063.md) | 海外PC | `remix_agent` | 当前无可创建应用数量时，展示付费弹窗 |
| [CF-P0-INTL-PC-064](overseas-pc/app-preview/CF-P0-INTL-PC-064.md) | 海外PC | `app_lifecycle_agent` | 进入应用管理后台后首次登录引导视频不应自动播放 |
| [CF-P0-INTL-H5-001](overseas-h5/guest-home/CF-P0-INTL-H5-001.md) | 海外H5 | `auth_access_agent` | 输入文案点击立即开发，跳转至登录页 |
| [CF-P0-INTL-H5-002](overseas-h5/guest-home/CF-P0-INTL-H5-002.md) | 海外H5 | `guest_explore_agent` | 点击气泡提示词，文案展示在文本输入框 |
| [CF-P0-INTL-H5-003](overseas-h5/guest-home/CF-P0-INTL-H5-003.md) | 海外H5 | `guest_explore_agent` | 应用列表默认展示“最新” |
| [CF-P0-INTL-H5-004](overseas-h5/guest-home/CF-P0-INTL-H5-004.md) | 海外H5 | `guest_explore_agent` | 点击应用进入应用页面 |
| [CF-P0-INTL-H5-005](overseas-h5/guest-home/CF-P0-INTL-H5-005.md) | 海外H5 | `auth_access_agent` | 点击工作台进入登录页面 |
| [CF-P0-INTL-H5-006](overseas-h5/guest-home/CF-P0-INTL-H5-006.md) | 海外H5 | `auth_access_agent` | 点击个人中心进入登录页面 |
| [CF-P0-INTL-H5-007](overseas-h5/auth/CF-P0-INTL-H5-007.md) | 海外H5 | `auth_access_agent` | H5 点击 Google 登录并成功返回 |
| [CF-P0-INTL-H5-008](overseas-h5/auth/CF-P0-INTL-H5-008.md) | 海外H5 | `auth_access_agent` | H5 用户输入正确邮箱和密码 |
| [CF-P0-INTL-H5-009](overseas-h5/auth/CF-P0-INTL-H5-009.md) | 海外H5 | `auth_access_agent` | H5 邮箱密码登录成功 |
| [CF-P0-INTL-H5-010](overseas-h5/auth/CF-P0-INTL-H5-010.md) | 海外H5 | `guest_explore_agent` | 顶部tab默认展示首位 |
| [CF-P0-INTL-H5-011](overseas-h5/auth/CF-P0-INTL-H5-011.md) | 海外H5 | `guest_explore_agent` | 切换tab展示对应页面内容 |
| [CF-P0-INTL-H5-012](overseas-h5/auth/CF-P0-INTL-H5-012.md) | 海外H5 | `guest_explore_agent` | 点击展示半屏弹窗 |
| [CF-P0-INTL-H5-013](overseas-h5/auth/CF-P0-INTL-H5-013.md) | 海外H5 | `guest_explore_agent` | 分享给好友 |
| [CF-P0-INTL-H5-014](overseas-h5/auth/CF-P0-INTL-H5-014.md) | 海外H5 | `remix_agent` | 做同款 |
| [CF-P0-INTL-H5-015](overseas-h5/workspace/CF-P0-INTL-H5-015.md) | 海外H5 | `app_lifecycle_agent` | 默认展示未发布tab应用列表展示用户已完成未发布、开发中的应用 |
| [CF-P0-INTL-H5-016](overseas-h5/workspace/CF-P0-INTL-H5-016.md) | 海外H5 | `app_lifecycle_agent` | 点击应用名称后操作按钮展示操作功能半屏弹窗 |
| [CF-P0-INTL-H5-017](overseas-h5/workspace/CF-P0-INTL-H5-017.md) | 海外H5 | `app_lifecycle_agent` | 点击弹出分享链接弹窗 |
| [CF-P0-INTL-H5-018](overseas-h5/workspace/CF-P0-INTL-H5-018.md) | 海外H5 | `app_lifecycle_agent` | 点击复制链接可将分享链接复制到剪切板 |
| [CF-P0-INTL-H5-019](overseas-h5/workspace/CF-P0-INTL-H5-019.md) | 海外H5 | `app_lifecycle_agent` | 点击跳转至应用对话页面 |
| [CF-P0-INTL-H5-020](overseas-h5/workspace/CF-P0-INTL-H5-020.md) | 海外H5 | `app_lifecycle_agent` | 点击弹出应用名称修改弹窗 |
| [CF-P0-INTL-H5-021](overseas-h5/workspace/CF-P0-INTL-H5-021.md) | 海外H5 | `app_lifecycle_agent` | 点击弹出toast提示 |
| [CF-P0-INTL-H5-022](overseas-h5/workspace/CF-P0-INTL-H5-022.md) | 海外H5 | `app_lifecycle_agent` | 点击弹出二次确认弹窗 |
| [CF-P0-INTL-H5-023](overseas-h5/workspace/CF-P0-INTL-H5-023.md) | 海外H5 | `app_lifecycle_agent` | 展示该用户已发布的应用 |
| [CF-P0-INTL-H5-024](overseas-h5/workspace/CF-P0-INTL-H5-024.md) | 海外H5 | `app_lifecycle_agent` | 点击应用名称后操作按钮展示操作功能半屏弹窗 |
| [CF-P0-INTL-H5-025](overseas-h5/workspace/CF-P0-INTL-H5-025.md) | 海外H5 | `app_lifecycle_agent` | 点击弹出分享链接弹窗 |
| [CF-P0-INTL-H5-026](overseas-h5/workspace/CF-P0-INTL-H5-026.md) | 海外H5 | `app_lifecycle_agent` | 点击复制链接可将分享链接复制到剪切板 |
| [CF-P0-INTL-H5-027](overseas-h5/workspace/CF-P0-INTL-H5-027.md) | 海外H5 | `app_lifecycle_agent` | 点击跳转至应用对话页面 |
| [CF-P0-INTL-H5-028](overseas-h5/workspace/CF-P0-INTL-H5-028.md) | 海外H5 | `app_lifecycle_agent` | 点击查看应用进入应用预览页 |
| [CF-P0-INTL-H5-029](overseas-h5/workspace/CF-P0-INTL-H5-029.md) | 海外H5 | `app_lifecycle_agent` | 点击发布应用弹出toast提示 |
| [CF-P0-INTL-H5-030](overseas-h5/workspace/CF-P0-INTL-H5-030.md) | 海外H5 | `app_lifecycle_agent` | 点击预览应用进入应用预览页 |
| [CF-P0-INTL-H5-031](overseas-h5/workspace/CF-P0-INTL-H5-031.md) | 海外H5 | `app_lifecycle_agent` | 点击发布应用弹出toast提示 |
| [CF-P0-INTL-H5-032](overseas-h5/workspace/CF-P0-INTL-H5-032.md) | 海外H5 | `app_lifecycle_agent` | 点击弹出应用名称修改弹窗 |
| [CF-P0-INTL-H5-033](overseas-h5/workspace/CF-P0-INTL-H5-033.md) | 海外H5 | `app_lifecycle_agent` | 点击结束应用发布状态 |
| [CF-P0-INTL-H5-034](overseas-h5/workspace/CF-P0-INTL-H5-034.md) | 海外H5 | `app_lifecycle_agent` | 点击弹出二次确认弹窗 |
| [CF-P0-INTL-H5-035](overseas-h5/profile/CF-P0-INTL-H5-035.md) | 海外H5 | `membership_credit_agent` | 顶部展示用户信息 |
| [CF-P0-INTL-H5-036](overseas-h5/profile/CF-P0-INTL-H5-036.md) | 海外H5 | `membership_credit_agent` | 展示用户当前会员类型及过期时间 |
| [CF-P0-INTL-H5-037](overseas-h5/profile/CF-P0-INTL-H5-037.md) | 海外H5 | `profile_support_agent` | 点击进入购买会员页面 |
| [CF-P0-INTL-H5-038](overseas-h5/profile/CF-P0-INTL-H5-038.md) | 海外H5 | `membership_credit_agent` | 点击立即购买按钮浏览器环境拉起支付宝 |
| [CF-P0-INTL-H5-039](overseas-h5/profile/CF-P0-INTL-H5-039.md) | 海外H5 | `membership_credit_agent` | 微信h5页面拉起微信支付 |
| [CF-P0-INTL-H5-040](overseas-h5/auth/CF-P0-INTL-H5-040.md) | 海外H5 | `auth_access_agent` | 点击退出登录跳转至未登录首页 |
| [CF-P0-INTL-H5-041](overseas-h5/app-create/CF-P0-INTL-H5-041.md) | 海外H5 | `app_lifecycle_agent` | 点击立即开发按钮进入需求澄清页面 |
| [CF-P0-INTL-H5-042](overseas-h5/app-create/CF-P0-INTL-H5-042.md) | 海外H5 | `app_lifecycle_agent` | 提示词文案进入文本输入框 |
