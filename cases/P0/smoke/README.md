# CodeFlying P0 冒烟测试用例

> 组织方式：一条用例一个 Markdown，按平台和模块分目录。

## 统计

- 用例总数：215
- 国内 PC：68
- 国内 H5：41
- 海外 PC：64
- 海外 H5：42
- 真人依赖：0

## Agent 分组统计

| Agent | 国内PC | 国内H5 | 海外PC | 海外H5 | 合计 |
|---|---|---|---|---|---|
| `auth_access_agent` | 6 | 5 | 5 | 7 | 23 |
| `shell_navigation_agent` | 14 | 0 | 11 | 0 | 25 |
| `invite_credit_agent` | 4 | 0 | 4 | 0 | 8 |
| `membership_credit_agent` | 15 | 5 | 20 | 4 | 44 |
| `api_key_agent` | 4 | 0 | 4 | 0 | 8 |
| `app_lifecycle_agent` | 11 | 10 | 10 | 10 | 41 |
| `app_publish_test_agent` | 11 | 0 | 6 | 0 | 17 |
| `publish_agent` | 0 | 12 | 0 | 12 | 24 |
| `remix_agent` | 3 | 1 | 4 | 1 | 9 |
| `guest_explore_agent` | 0 | 7 | 0 | 7 | 14 |
| `profile_support_agent` | 0 | 1 | 0 | 1 | 2 |

## 国内 H5 执行入口

- 国内 H5 用例必须从真实 H5 地址进入：`https://www.codeflying.net/codeflying_h5/`。
- 不允许只打开 PC 页面再修改浏览器 viewport 充当 H5；viewport 可以设为移动端尺寸，但入口 URL 必须是 H5 路由。
- 工作台/登录后首页的"应用名称后操作按钮"指应用卡片外层名称旁的三点/更多按钮。测试分享、查看对话过程、修改名称、发布、删除时，应先停留在应用列表外层，点击该按钮打开底部半屏菜单；除非用例标题明确要求"进入应用预览页"，不要先点击应用卡片主体。
- 分享链接类用例必须校验复制副作用：点击"复制链接"后读取剪贴板，确认剪贴板为非空 URL，且和弹窗展示的分享链接一致或包含同一分享地址。

## 应用创建/生成请求确认卡片

- 创建应用、输入需求、点击立即开发、进入对话页面等用例，只验证"需求被接收并出现首条有效反馈"，不等待完整应用生成完成。
- 提交需求后如果出现"选择生成类型/你想生成什么类型/网站/小程序/H5/应用"等请求确认卡片，统一选择默认推荐项或第一个可用项，并点击"确认/继续/开始生成/生成应用"。
- 确认卡片处理完成后，只要页面出现非空助手回复、`收到`、`我先想想`、`正在为你生成`、`需求已接收`、生成进度或对话消息之一，即可按对应创建/对话用例判 PASS 或 RETRY_PASS。
- 不得因为应用后续未生成完成、构建仍在排队、未跳转预览页，就把"输入需求/进入对话/收到反馈"类用例判 FAIL。

## 用例索引

| 用例 ID | 端 | 模块 | Sub Agent | 执行方式 | 标题 |
|---|---|---|---|---|---|
| [CF-P0-H5-001](domestic-h5/guest-home/CF-P0-H5-001.md) | 国内H5 | 国内H5 / 未登录首页 | `auth_access_agent` | 可自动化 | 输入文案点击立即开发，跳转至登录页 |
| [CF-P0-H5-002](domestic-h5/guest-home/CF-P0-H5-002.md) | 国内H5 | 国内H5 / 未登录首页 | `guest_explore_agent` | 可自动化 | 点击气泡提示词，文案展示在文本输入框 |
| [CF-P0-H5-003](domestic-h5/guest-home/CF-P0-H5-003.md) | 国内H5 | 国内H5 / 未登录首页 | `guest_explore_agent` | 可自动化 | 应用列表默认展示“义务专区” |
| [CF-P0-H5-004](domestic-h5/guest-home/CF-P0-H5-004.md) | 国内H5 | 国内H5 / 未登录首页 / 应用卡片 | `guest_explore_agent` | 可自动化 | 点击应用进入应用页面 |
| [CF-P0-H5-005](domestic-h5/guest-home/CF-P0-H5-005.md) | 国内H5 | 国内H5 / 未登录首页 | `auth_access_agent` | 可自动化 | 点击工作台进入登录页面 |
| [CF-P0-H5-006](domestic-h5/guest-home/CF-P0-H5-006.md) | 国内H5 | 国内H5 / 未登录首页 | `auth_access_agent` | 可自动化 | 点击个人中心进入登录页面 |
| [CF-P0-H5-007](domestic-h5/phone-auth/CF-P0-H5-007.md) | 国内H5 | 国内H5 / 登录 / 手机号验证码登录 | `auth_access_agent` | 可自动化 | 用户输入手机号点击获取验证码，验证码可发送至用户 |
| [CF-P0-H5-008](domestic-h5/phone-auth/CF-P0-H5-008.md) | 国内H5 | 国内H5 / 登录 / 手机号验证码登录 | `auth_access_agent` | 可自动化 | 输入正确验证码勾选用户协议，登录成功 |
| [CF-P0-H5-009](domestic-h5/auth/CF-P0-H5-009.md) | 国内H5 | 国内H5 / 登录后首页 | `guest_explore_agent` | 可自动化 | 顶部tab默认展示首位 |
| [CF-P0-H5-010](domestic-h5/auth/CF-P0-H5-010.md) | 国内H5 | 国内H5 / 登录后首页 | `guest_explore_agent` | 可自动化 | 切换tab展示对应页面内容 |
| [CF-P0-H5-011](domestic-h5/auth/CF-P0-H5-011.md) | 国内H5 | 国内H5 / 登录后首页 / 应用名称后操作按钮 | `guest_explore_agent` | 可自动化 | 点击展示半屏弹窗 |
| [CF-P0-H5-012](domestic-h5/auth/CF-P0-H5-012.md) | 国内H5 | 国内H5 / 登录后首页 / 应用名称后操作按钮 | `guest_explore_agent` | 可自动化 | 分享给好友 |
| [CF-P0-H5-013](domestic-h5/auth/CF-P0-H5-013.md) | 国内H5 | 国内H5 / 首页应用广场 / 应用卡片三点菜单 | `remix_agent` | 可自动化 | 做同款 |
| [CF-P0-H5-014](domestic-h5/workspace/CF-P0-H5-014.md) | 国内H5 | 国内H5 / 工作台 / 未发布 | `app_lifecycle_agent` | 可自动化 | 默认展示未发布tab应用列表展示用户已完成未发布、开发中的应用 |
| [CF-P0-H5-015](domestic-h5/workspace/CF-P0-H5-015.md) | 国内H5 | 国内H5 / 工作台 / 未发布 / 应用操作 | `app_lifecycle_agent` | 可自动化 | 点击应用名称后操作按钮展示操作功能半屏弹窗 |
| [CF-P0-H5-016](domestic-h5/workspace/CF-P0-H5-016.md) | 国内H5 | 国内H5 / 工作台 / 未发布 / 应用操作 / 分享应用 | `app_lifecycle_agent` | 可自动化 | 点击弹出分享链接弹窗 |
| [CF-P0-H5-017](domestic-h5/workspace/CF-P0-H5-017.md) | 国内H5 | 国内H5 / 工作台 / 未发布 / 应用操作 / 分享应用 | `app_lifecycle_agent` | 可自动化 | 点击复制链接可将分享链接复制到剪切板 |
| [CF-P0-H5-018](domestic-h5/workspace/CF-P0-H5-018.md) | 国内H5 | 国内H5 / 工作台 / 未发布 / 应用操作 / 查看对话过程 | `app_lifecycle_agent` | 可自动化 | 点击跳转至应用对话页面 |
| [CF-P0-H5-019](domestic-h5/workspace/CF-P0-H5-019.md) | 国内H5 | 国内H5 / 工作台 / 未发布 / 应用操作 / 修改名称 | `app_lifecycle_agent` | 可自动化 | 点击弹出应用名称修改弹窗 |
| [CF-P0-H5-020](domestic-h5/workspace/CF-P0-H5-020.md) | 国内H5 | 国内H5 / 工作台 / 未发布 / 应用操作 / 发布应用 | `app_lifecycle_agent` | 可自动化 | 点击弹出toast提示 |
| [CF-P0-H5-021](domestic-h5/workspace/CF-P0-H5-021.md) | 国内H5 | 国内H5 / 工作台 / 未发布 / 应用操作 / 删除应用 | `app_lifecycle_agent` | 可自动化 | 点击弹出二次确认弹窗 |
| [CF-P0-H5-022](domestic-h5/workspace/CF-P0-H5-022.md) | 国内H5 | 国内H5 / 工作台 / 已发布 | `app_lifecycle_agent` | 可自动化 | 展示该用户已发布的应用 |
| [CF-P0-H5-023](domestic-h5/workspace/CF-P0-H5-023.md) | 国内H5 | 国内H5 / 工作台 / 已发布 / 应用操作 | `app_lifecycle_agent` | 可自动化 | 点击应用名称后操作按钮展示操作功能半屏弹窗 |
| [CF-P0-H5-024](domestic-h5/workspace/CF-P0-H5-024.md) | 国内H5 | 国内H5 / 工作台 / 已发布 / 应用操作 / 分享应用 | `app_lifecycle_agent` | 可自动化 | 点击弹出分享链接弹窗 |
| [CF-P0-H5-025](domestic-h5/workspace/CF-P0-H5-025.md) | 国内H5 | 国内H5 / 工作台 / 已发布 / 应用操作 / 分享应用 | `app_lifecycle_agent` | 可自动化 | 点击复制链接可将分享链接复制到剪切板 |
| [CF-P0-H5-026](domestic-h5/workspace/CF-P0-H5-026.md) | 国内H5 | 国内H5 / 工作台 / 已发布 / 应用操作 / 查看对话过程 | `app_lifecycle_agent` | 可自动化 | 点击跳转至应用对话页面 |
| [CF-P0-H5-027](domestic-h5/workspace/CF-P0-H5-027.md) | 国内H5 | 国内H5 / 工作台 / 已发布 / 应用操作 / 卡片信息 | `app_lifecycle_agent` | 可自动化 | 点击查看应用进入应用预览页 |
| [CF-P0-H5-028](domestic-h5/workspace/CF-P0-H5-028.md) | 国内H5 | 国内H5 / 工作台 / 已发布 / 应用操作 / 卡片信息 | `app_lifecycle_agent` | 可自动化 | 点击发布应用弹出toast提示 |
| [CF-P0-H5-029](domestic-h5/workspace/CF-P0-H5-029.md) | 国内H5 | 国内H5 / 工作台 / 已发布 / 应用操作 / 底部功能按钮 | `app_lifecycle_agent` | 可自动化 | 点击预览应用进入应用预览页 |
| [CF-P0-H5-030](domestic-h5/workspace/CF-P0-H5-030.md) | 国内H5 | 国内H5 / 工作台 / 已发布 / 应用操作 / 底部功能按钮 | `app_lifecycle_agent` | 可自动化 | 点击发布应用弹出toast提示 |
| [CF-P0-H5-031](domestic-h5/workspace/CF-P0-H5-031.md) | 国内H5 | 国内H5 / 工作台 / 已发布 / 应用操作 / 修改名称 | `app_lifecycle_agent` | 可自动化 | 点击弹出应用名称修改弹窗 |
| [CF-P0-H5-032](domestic-h5/workspace/CF-P0-H5-032.md) | 国内H5 | 国内H5 / 工作台 / 已发布 / 应用操作 / 取消发布 | `app_lifecycle_agent` | 可自动化 | 点击结束应用发布状态 |
| [CF-P0-H5-033](domestic-h5/workspace/CF-P0-H5-033.md) | 国内H5 | 国内H5 / 工作台 / 已发布 / 应用操作 / 删除应用 | `app_lifecycle_agent` | 可自动化 | 点击弹出二次确认弹窗 |
| [CF-P0-H5-034](domestic-h5/profile/CF-P0-H5-034.md) | 国内H5 | 国内H5 / 个人中心 | `membership_credit_agent` | 可自动化 | 顶部展示用户信息 |
| [CF-P0-H5-035](domestic-h5/profile/CF-P0-H5-035.md) | 国内H5 | 国内H5 / 个人中心 / 会员类型 | `membership_credit_agent` | 可自动化 | 展示用户当前会员类型及过期时间 |
| [CF-P0-H5-036](domestic-h5/profile/CF-P0-H5-036.md) | 国内H5 | 国内H5 / 个人中心 / 会员类型 / 充值会员 | `membership_credit_agent` | 可自动化 | 点击进入购买会员页面 |
| [CF-P0-H5-037](domestic-h5/profile/CF-P0-H5-037.md) | 国内H5 | 国内H5 / 个人中心 / 在线客服 | `profile_support_agent` | 可自动化 | 点击跳转至在线客服对话页 |
| [CF-P0-H5-039](domestic-h5/app-create/CF-P0-H5-039.md) | 国内H5 | 国内H5 / 应用创建 / 文本框内输入需求文案 | `app_lifecycle_agent` | 可自动化 | 点击立即开发按钮进入需求澄清页面 |
| [CF-P0-H5-040](domestic-h5/app-create/CF-P0-H5-040.md) | 国内H5 | 国内H5 / 应用创建 / 点击提示词气泡 | `app_lifecycle_agent` | 可自动化 | 提示词文案进入文本输入框 |
| [CF-P0-H5-041](domestic-h5/profile/CF-P0-H5-041.md) | 国内H5 | 国内H5 / 个人中心 / 会员类型 / 充值会员 | `membership_credit_agent` | 可自动化 | 点击立即购买按钮浏览器环境拉起支付宝 |
| [CF-P0-H5-042](domestic-h5/profile/CF-P0-H5-042.md) | 国内H5 |  | `membership_credit_agent` | 可自动化 | 国内H5会员购买拉起支付宝支付 |
| [CF-P0-INTL-H5-001](overseas-h5/guest-home/CF-P0-INTL-H5-001.md) | 海外H5 | 海外H5 / 未登录首页 | `auth_access_agent` | 可自动化 | 输入文案点击立即开发，跳转至登录页 |
| [CF-P0-INTL-H5-002](overseas-h5/guest-home/CF-P0-INTL-H5-002.md) | 海外H5 | 海外H5 / 未登录首页 | `guest_explore_agent` | 可自动化 | 点击气泡提示词，文案展示在文本输入框 |
| [CF-P0-INTL-H5-003](overseas-h5/guest-home/CF-P0-INTL-H5-003.md) | 海外H5 | 海外H5 / 未登录首页 | `guest_explore_agent` | 可自动化 | 应用列表默认展示“最新” |
| [CF-P0-INTL-H5-004](overseas-h5/guest-home/CF-P0-INTL-H5-004.md) | 海外H5 | 海外H5 / 未登录首页 / 应用卡片 | `guest_explore_agent` | 可自动化 | 点击应用进入应用页面 |
| [CF-P0-INTL-H5-005](overseas-h5/guest-home/CF-P0-INTL-H5-005.md) | 海外H5 | 海外H5 / 未登录首页 | `auth_access_agent` | 可自动化 | 点击工作台进入登录页面 |
| [CF-P0-INTL-H5-006](overseas-h5/guest-home/CF-P0-INTL-H5-006.md) | 海外H5 | 海外H5 / 未登录首页 | `auth_access_agent` | 可自动化 | 点击个人中心进入登录页面 |
| [CF-P0-INTL-H5-007](overseas-h5/auth/CF-P0-INTL-H5-007.md) | 海外H5 |  | `auth_access_agent` | 第三方账号依赖（自动化检查入口、授权页和回跳） | H5 点击 Google 登录并成功返回 |
| [CF-P0-INTL-H5-008](overseas-h5/auth/CF-P0-INTL-H5-008.md) | 海外H5 |  | `auth_access_agent` | 可自动化 | H5 用户输入正确邮箱和密码 |
| [CF-P0-INTL-H5-009](overseas-h5/auth/CF-P0-INTL-H5-009.md) | 海外H5 |  | `auth_access_agent` | 可自动化 | H5 邮箱密码登录成功 |
| [CF-P0-INTL-H5-010](overseas-h5/auth/CF-P0-INTL-H5-010.md) | 海外H5 | 海外H5 / 登录后首页 | `guest_explore_agent` | 可自动化 | 顶部tab默认展示首位 |
| [CF-P0-INTL-H5-011](overseas-h5/auth/CF-P0-INTL-H5-011.md) | 海外H5 | 海外H5 / 登录后首页 | `guest_explore_agent` | 可自动化 | 切换tab展示对应页面内容 |
| [CF-P0-INTL-H5-012](overseas-h5/auth/CF-P0-INTL-H5-012.md) | 海外H5 | 海外H5 / 登录后首页 / 应用名称后操作按钮 | `guest_explore_agent` | 可自动化 | 点击展示半屏弹窗 |
| [CF-P0-INTL-H5-013](overseas-h5/auth/CF-P0-INTL-H5-013.md) | 海外H5 | 海外H5 / 登录后首页 / 应用名称后操作按钮 | `guest_explore_agent` | 可自动化 | 分享给好友 |
| [CF-P0-INTL-H5-014](overseas-h5/auth/CF-P0-INTL-H5-014.md) | 海外H5 | 海外H5 / 首页应用广场 / 应用卡片三点菜单 | `remix_agent` | 可自动化 | 做同款 |
| [CF-P0-INTL-H5-015](overseas-h5/workspace/CF-P0-INTL-H5-015.md) | 海外H5 | 海外H5 / 工作台 / 未发布 | `app_lifecycle_agent` | 可自动化 | 默认展示未发布tab应用列表展示用户已完成未发布、开发中的应用 |
| [CF-P0-INTL-H5-016](overseas-h5/workspace/CF-P0-INTL-H5-016.md) | 海外H5 | 海外H5 / 工作台 / 未发布 / 应用操作 | `app_lifecycle_agent` | 可自动化 | 点击应用名称后操作按钮展示操作功能半屏弹窗 |
| [CF-P0-INTL-H5-017](overseas-h5/workspace/CF-P0-INTL-H5-017.md) | 海外H5 | 海外H5 / 工作台 / 未发布 / 应用操作 / 分享应用 | `app_lifecycle_agent` | 可自动化 | 点击弹出分享链接弹窗 |
| [CF-P0-INTL-H5-018](overseas-h5/workspace/CF-P0-INTL-H5-018.md) | 海外H5 | 海外H5 / 工作台 / 未发布 / 应用操作 / 分享应用 | `app_lifecycle_agent` | 可自动化 | 点击复制链接可将分享链接复制到剪切板 |
| [CF-P0-INTL-H5-019](overseas-h5/workspace/CF-P0-INTL-H5-019.md) | 海外H5 | 海外H5 / 工作台 / 未发布 / 应用操作 / 查看对话过程 | `app_lifecycle_agent` | 可自动化 | 点击跳转至应用对话页面 |
| [CF-P0-INTL-H5-020](overseas-h5/workspace/CF-P0-INTL-H5-020.md) | 海外H5 | 海外H5 / 工作台 / 未发布 / 应用操作 / 修改名称 | `app_lifecycle_agent` | 可自动化 | 点击弹出应用名称修改弹窗 |
| [CF-P0-INTL-H5-021](overseas-h5/workspace/CF-P0-INTL-H5-021.md) | 海外H5 | 海外H5 / 工作台 / 未发布 / 应用操作 / 发布应用 | `app_lifecycle_agent` | 可自动化 | 点击弹出toast提示 |
| [CF-P0-INTL-H5-022](overseas-h5/workspace/CF-P0-INTL-H5-022.md) | 海外H5 | 海外H5 / 工作台 / 未发布 / 应用操作 / 删除应用 | `app_lifecycle_agent` | 可自动化 | 点击弹出二次确认弹窗 |
| [CF-P0-INTL-H5-023](overseas-h5/workspace/CF-P0-INTL-H5-023.md) | 海外H5 | 海外H5 / 工作台 / 已发布 | `app_lifecycle_agent` | 可自动化 | 展示该用户已发布的应用 |
| [CF-P0-INTL-H5-024](overseas-h5/workspace/CF-P0-INTL-H5-024.md) | 海外H5 | 海外H5 / 工作台 / 已发布 / 应用操作 | `app_lifecycle_agent` | 可自动化 | 点击应用名称后操作按钮展示操作功能半屏弹窗 |
| [CF-P0-INTL-H5-025](overseas-h5/workspace/CF-P0-INTL-H5-025.md) | 海外H5 | 海外H5 / 工作台 / 已发布 / 应用操作 / 分享应用 | `app_lifecycle_agent` | 可自动化 | 点击弹出分享链接弹窗 |
| [CF-P0-INTL-H5-026](overseas-h5/workspace/CF-P0-INTL-H5-026.md) | 海外H5 | 海外H5 / 工作台 / 已发布 / 应用操作 / 分享应用 | `app_lifecycle_agent` | 可自动化 | 点击复制链接可将分享链接复制到剪切板 |
| [CF-P0-INTL-H5-027](overseas-h5/workspace/CF-P0-INTL-H5-027.md) | 海外H5 | 海外H5 / 工作台 / 已发布 / 应用操作 / 查看对话过程 | `app_lifecycle_agent` | 可自动化 | 点击跳转至应用对话页面 |
| [CF-P0-INTL-H5-028](overseas-h5/workspace/CF-P0-INTL-H5-028.md) | 海外H5 | 海外H5 / 工作台 / 已发布 / 应用操作 / 查看对话过程 / 卡片信息 | `app_lifecycle_agent` | 可自动化 | 点击查看应用进入应用预览页 |
| [CF-P0-INTL-H5-029](overseas-h5/workspace/CF-P0-INTL-H5-029.md) | 海外H5 | 海外H5 / 工作台 / 已发布 / 应用操作 / 查看对话过程 / 卡片信息 | `app_lifecycle_agent` | 可自动化 | 点击发布应用弹出toast提示 |
| [CF-P0-INTL-H5-030](overseas-h5/workspace/CF-P0-INTL-H5-030.md) | 海外H5 | 海外H5 / 工作台 / 已发布 / 应用操作 / 查看对话过程 / 底部功能按钮 | `app_lifecycle_agent` | 可自动化 | 点击预览应用进入应用预览页 |
| [CF-P0-INTL-H5-031](overseas-h5/workspace/CF-P0-INTL-H5-031.md) | 海外H5 | 海外H5 / 工作台 / 已发布 / 应用操作 / 查看对话过程 / 底部功能按钮 | `app_lifecycle_agent` | 可自动化 | 点击发布应用弹出toast提示 |
| [CF-P0-INTL-H5-032](overseas-h5/workspace/CF-P0-INTL-H5-032.md) | 海外H5 | 海外H5 / 工作台 / 已发布 / 应用操作 / 修改名称 | `app_lifecycle_agent` | 可自动化 | 点击弹出应用名称修改弹窗 |
| [CF-P0-INTL-H5-033](overseas-h5/workspace/CF-P0-INTL-H5-033.md) | 海外H5 | 海外H5 / 工作台 / 已发布 / 应用操作 / 取消发布 | `app_lifecycle_agent` | 可自动化 | 点击结束应用发布状态 |
| [CF-P0-INTL-H5-034](overseas-h5/workspace/CF-P0-INTL-H5-034.md) | 海外H5 | 海外H5 / 工作台 / 已发布 / 应用操作 / 删除应用 | `app_lifecycle_agent` | 可自动化 | 点击弹出二次确认弹窗 |
| [CF-P0-INTL-H5-035](overseas-h5/profile/CF-P0-INTL-H5-035.md) | 海外H5 | 海外H5 / 个人中心 | `membership_credit_agent` | 可自动化 | 顶部展示用户信息 |
| [CF-P0-INTL-H5-036](overseas-h5/profile/CF-P0-INTL-H5-036.md) | 海外H5 | 海外H5 / 个人中心 / 会员类型 | `membership_credit_agent` | 可自动化 | 展示用户当前会员类型及过期时间 |
| [CF-P0-INTL-H5-037](overseas-h5/profile/CF-P0-INTL-H5-037.md) | 海外H5 | 海外H5 / 个人中心 / 会员类型 / 充值会员 | `profile_support_agent` | 可自动化 | 点击进入购买会员页面 |
| [CF-P0-INTL-H5-038](overseas-h5/profile/CF-P0-INTL-H5-038.md) | 海外H5 | 海外H5 / 个人中心 / 会员类型 / 充值会员 | `membership_credit_agent` | 可自动化（本轮以支付二维码/支付弹窗出现为通过标准；真实拉起支付宝暂不纳入自动化） | 点击立即购买按钮浏览器环境拉起支付宝 |
| [CF-P0-INTL-H5-039](overseas-h5/profile/CF-P0-INTL-H5-039.md) | 海外H5 | 海外H5 / 个人中心 / 会员类型 / 充值会员 | `membership_credit_agent` | 可自动化（本轮以微信支付二维码/支付弹窗出现为通过标准；真实微信 H5 支付暂不纳入自动化） | 微信h5页面拉起微信支付 |
| [CF-P0-INTL-H5-040](overseas-h5/auth/CF-P0-INTL-H5-040.md) | 海外H5 | 海外H5 / 个人中心 / 退出登录 | `auth_access_agent` | 可自动化 | 点击退出登录跳转至未登录首页 |
| [CF-P0-INTL-H5-041](overseas-h5/app-create/CF-P0-INTL-H5-041.md) | 海外H5 | 海外H5 / 应用创建 / 文本框内输入需求文案 | `app_lifecycle_agent` | 可自动化 | 点击立即开发按钮进入需求澄清页面 |
| [CF-P0-INTL-H5-042](overseas-h5/app-create/CF-P0-INTL-H5-042.md) | 海外H5 | 海外H5 / 应用创建 / 点击提示词气泡 | `app_lifecycle_agent` | 可自动化 | 提示词文案进入文本输入框 |
| [CF-P0-INTL-PC-001](overseas-pc/guest-home/CF-P0-INTL-PC-001.md) | 海外PC | 海外主站 / 未登录首页 | `auth_access_agent` | 可自动化 | 点击登录按钮跳转至登录页 |
| [CF-P0-INTL-PC-002](overseas-pc/guest-home/CF-P0-INTL-PC-002.md) | 海外PC | 海外主站 / 未登录首页 | `auth_access_agent` | 可自动化 | 输入文案点击立即开发跳转至登录页 |
| [CF-P0-INTL-PC-003](overseas-pc/auth/CF-P0-INTL-PC-003.md) | 海外PC |  | `auth_access_agent` | 第三方账号依赖（自动化检查入口、授权页和回跳） | 点击 Google 登录并成功返回海外主站 |
| [CF-P0-INTL-PC-004](overseas-pc/auth/CF-P0-INTL-PC-004.md) | 海外PC |  | `auth_access_agent` | 可自动化 | 用户输入正确邮箱和密码 |
| [CF-P0-INTL-PC-005](overseas-pc/auth/CF-P0-INTL-PC-005.md) | 海外PC |  | `auth_access_agent` | 可自动化 | 邮箱密码登录成功 |
| [CF-P0-INTL-PC-006](overseas-pc/top-nav/CF-P0-INTL-PC-006.md) | 海外PC | 海外主站 / 顶部导航 | `shell_navigation_agent` | 可自动化 | 左侧展示码上飞logo 点击进入应用广场页面 |
| [CF-P0-INTL-PC-007](overseas-pc/top-nav/CF-P0-INTL-PC-007.md) | 海外PC | 海外主站 / 顶部导航 | `shell_navigation_agent` | 可自动化 | 点击充值会员 弹出购买会员弹窗 |
| [CF-P0-INTL-PC-008](overseas-pc/top-nav/CF-P0-INTL-PC-008.md) | 海外PC | 海外主站 / 顶部导航 / 语言选择 | `shell_navigation_agent` | 可自动化 | 用户可根据枚举选择语言类型 |
| [CF-P0-INTL-PC-009](overseas-pc/top-nav/CF-P0-INTL-PC-009.md) | 海外PC | 海外主站 / 顶部导航 / 语言选择 | `shell_navigation_agent` | 可自动化 | 选中语言类型后页面文案随机切换对应语种文案 |
| [CF-P0-INTL-PC-010](overseas-pc/app-square/CF-P0-INTL-PC-010.md) | 海外PC | 海外主站 / 侧边栏 / 应用广场 | `shell_navigation_agent` | 可自动化 | 点击跳转至应用广场页面 |
| [CF-P0-INTL-PC-011](overseas-pc/app-square/CF-P0-INTL-PC-011.md) | 海外PC | 海外主站 / 侧边栏 / 应用广场 | `shell_navigation_agent` | 可自动化 | 顶部tab默认展示首位 |
| [CF-P0-INTL-PC-012](overseas-pc/app-square/CF-P0-INTL-PC-012.md) | 海外PC | 海外主站 / 侧边栏 / 应用广场 | `shell_navigation_agent` | 可自动化 | 切换tab展示对应页面内容 |
| [CF-P0-INTL-PC-013](overseas-pc/my-apps/CF-P0-INTL-PC-013.md) | 海外PC | 海外主站 / 侧边栏 / 我的应用 | `shell_navigation_agent` | 可自动化 | 点击跳转至应我的应用页面 |
| [CF-P0-INTL-PC-014](overseas-pc/my-apps/CF-P0-INTL-PC-014.md) | 海外PC | 海外主站 / 侧边栏 / 我的应用 | `shell_navigation_agent` | 可自动化 | 顶部tab默认展示该用户全部应用 |
| [CF-P0-INTL-PC-015](overseas-pc/my-apps/CF-P0-INTL-PC-015.md) | 海外PC | 海外主站 / 侧边栏 / 我的应用 | `shell_navigation_agent` | 可自动化 | 点击未发布tab展示该用户已创建未发布、创建中的应用 |
| [CF-P0-INTL-PC-016](overseas-pc/my-apps/CF-P0-INTL-PC-016.md) | 海外PC | 海外主站 / 侧边栏 / 我的应用 | `shell_navigation_agent` | 可自动化 | 点击已发布tab展示该用户已发布的应用 |
| [CF-P0-INTL-PC-017](overseas-pc/earn-points/CF-P0-INTL-PC-017.md) | 海外PC | 海外主站 / 侧边栏 / 赚取积分 | `invite_credit_agent` | 可自动化 | 点击跳转至应赚取积分页面 |
| [CF-P0-INTL-PC-018](overseas-pc/earn-points/CF-P0-INTL-PC-018.md) | 海外PC | 海外主站 / 侧边栏 / 赚取积分 | `invite_credit_agent` | 可自动化 | 点击复制链接按钮可将邀请链接复制至剪切板 |
| [CF-P0-INTL-PC-019](overseas-pc/earn-points/CF-P0-INTL-PC-019.md) | 海外PC | 海外主站 / 侧边栏 / 赚取积分 | `invite_credit_agent` | 可自动化 | 成功邀请新用户登录可正常下发对应积分 |
| [CF-P0-INTL-PC-020](overseas-pc/earn-points/CF-P0-INTL-PC-020.md) | 海外PC | 海外主站 / 侧边栏 / 赚取积分 | `invite_credit_agent` | 可自动化 | 非新用户注册奖励不下发 |
| [CF-P0-INTL-PC-021](overseas-pc/entitlements/CF-P0-INTL-PC-021.md) | 海外PC | 海外主站 / 侧边栏 / 我的权益 / 会员权益 | `membership_credit_agent` | 可自动化 | 每日免费积分展示每日获赠积分数及剩余积分数 / 每日获赠100积分 |
| [CF-P0-INTL-PC-022](overseas-pc/entitlements/CF-P0-INTL-PC-022.md) | 海外PC | 海外主站 / 侧边栏 / 我的权益 / 会员权益 | `membership_credit_agent` | 可自动化 | 会员每月积分展示对应会员等级获赠积分数及当前剩余积分数 / 免费版  0 |
| [CF-P0-INTL-PC-023](overseas-pc/entitlements/CF-P0-INTL-PC-023.md) | 海外PC | 海外主站 / 侧边栏 / 我的权益 / 会员权益 | `membership_credit_agent` | 可自动化 | 会员每月积分展示对应会员等级获赠积分数及当前剩余积分数 / 标准版 3000 |
| [CF-P0-INTL-PC-024](overseas-pc/entitlements/CF-P0-INTL-PC-024.md) | 海外PC | 海外主站 / 侧边栏 / 我的权益 / 会员权益 | `membership_credit_agent` | 可自动化 | 会员每月积分展示对应会员等级获赠积分数及当前剩余积分数 / 进阶版 6600 |
| [CF-P0-INTL-PC-025](overseas-pc/entitlements/CF-P0-INTL-PC-025.md) | 海外PC | 海外主站 / 侧边栏 / 我的权益 / 会员权益 | `membership_credit_agent` | 可自动化 | 会员每月积分展示对应会员等级获赠积分数及当前剩余积分数 / 尊享版 27600 |
| [CF-P0-INTL-PC-026](overseas-pc/entitlements/CF-P0-INTL-PC-026.md) | 海外PC | 海外主站 / 侧边栏 / 我的权益 / 会员权益 | `membership_credit_agent` | 可自动化 | 自购积分包展示用户购买积分数及当前剩余积分数 |
| [CF-P0-INTL-PC-027](overseas-pc/entitlements/CF-P0-INTL-PC-027.md) | 海外PC | 海外主站 / 侧边栏 / 我的权益 / 会员权益 | `membership_credit_agent` | 可自动化 | 剩余可创建应用数展示对应会员等级可创建数量及剩余可创建数量 / 免费版  2 |
| [CF-P0-INTL-PC-028](overseas-pc/entitlements/CF-P0-INTL-PC-028.md) | 海外PC | 海外主站 / 侧边栏 / 我的权益 / 会员权益 | `membership_credit_agent` | 可自动化 | 剩余可创建应用数展示对应会员等级可创建数量及剩余可创建数量 / 标准版 10 |
| [CF-P0-INTL-PC-029](overseas-pc/entitlements/CF-P0-INTL-PC-029.md) | 海外PC | 海外主站 / 侧边栏 / 我的权益 / 会员权益 | `membership_credit_agent` | 可自动化 | 剩余可创建应用数展示对应会员等级可创建数量及剩余可创建数量 / 进阶版 无限 |
| [CF-P0-INTL-PC-030](overseas-pc/entitlements/CF-P0-INTL-PC-030.md) | 海外PC | 海外主站 / 侧边栏 / 我的权益 / 会员权益 | `membership_credit_agent` | 可自动化 | 剩余可创建应用数展示对应会员等级可创建数量及剩余可创建数量 / 尊享版 无限 |
| [CF-P0-INTL-PC-031](overseas-pc/entitlements/CF-P0-INTL-PC-031.md) | 海外PC | 海外主站 / 侧边栏 / 我的权益 / 推荐奖励 | `membership_credit_agent` | 可自动化 | 展示用户邀请新用户获得的积分及剩余积分 |
| [CF-P0-INTL-PC-032](overseas-pc/entitlements/CF-P0-INTL-PC-032.md) | 海外PC | 海外主站 / 侧边栏 / 我的权益 / 积分消耗明细 | `membership_credit_agent` | 可自动化 | 点击展示积分消耗明细弹窗 |
| [CF-P0-INTL-PC-033](overseas-pc/settings-billing/CF-P0-INTL-PC-033.md) | 海外PC | 海外主站 / 侧边栏 / 设置和账单 / 设置 / 用户头像 | `membership_credit_agent` | 可自动化 | 正常展示用户头像 |
| [CF-P0-INTL-PC-034](overseas-pc/settings-billing/CF-P0-INTL-PC-034.md) | 海外PC | 海外主站 / 侧边栏 / 设置和账单 / 设置 / 用户昵称 | `membership_credit_agent` | 可自动化 | 正确展示用户昵称 |
| [CF-P0-INTL-PC-035](overseas-pc/settings-billing/CF-P0-INTL-PC-035.md) | 海外PC | 海外主站 / 侧边栏 / 设置和账单 / 设置 / 音色切换 | `membership_credit_agent` | 可自动化 | 正常展示音色名称 |
| [CF-P0-INTL-PC-036](overseas-pc/settings-billing/CF-P0-INTL-PC-036.md) | 海外PC | 海外主站 / 侧边栏 / 设置和账单 / 账单 / 账单列表 | `membership_credit_agent` | 可自动化 | 倒序展示仅三条支付数据 |
| [CF-P0-INTL-PC-037](overseas-pc/settings-billing/CF-P0-INTL-PC-037.md) | 海外PC | 海外主站 / 侧边栏 / 设置和账单 / 账单 / 查看全部账单历史 | `membership_credit_agent` | 可自动化 | 点击后弹窗倒序展示用户所有支付数据 |
| [CF-P0-INTL-PC-038](overseas-pc/settings-billing/CF-P0-INTL-PC-038.md) | 海外PC | 海外主站 / 侧边栏 / 设置和账单 / API服务 | `api_key_agent` | 可自动化 | 点进入API服务页面 |
| [CF-P0-INTL-PC-039](overseas-pc/settings-billing/CF-P0-INTL-PC-039.md) | 海外PC | 海外主站 / 侧边栏 / 设置和账单 / API服务 / 积分消耗情况 | `membership_credit_agent` | 可自动化 | 点击充值积分弹出购买弹窗 |
| [CF-P0-INTL-PC-040](overseas-pc/settings-billing/CF-P0-INTL-PC-040.md) | 海外PC | 海外主站 / 侧边栏 / 设置和账单 / API服务 / 积分消耗情况 | `membership_credit_agent` | 可自动化 | 剩余积分展示用户当前剩余总积分数 |
| [CF-P0-INTL-PC-041](overseas-pc/settings-billing/CF-P0-INTL-PC-041.md) | 海外PC | 海外主站 / 侧边栏 / 设置和账单 / API服务 / 积分消耗情况 | `membership_credit_agent` | 可自动化 | 本月已用积分展示用户本月已使用积分 |
| [CF-P0-INTL-PC-042](overseas-pc/settings-billing/CF-P0-INTL-PC-042.md) | 海外PC | 海外主站 / 侧边栏 / 设置和账单 / API服务 / API密钥 | `api_key_agent` | 可自动化 | 点击复制按钮可成功将密钥复制进剪切板 |
| [CF-P0-INTL-PC-043](overseas-pc/settings-billing/CF-P0-INTL-PC-043.md) | 海外PC | 海外主站 / 侧边栏 / 设置和账单 / API服务 / API密钥 | `api_key_agent` | 可自动化 | 点击删除按钮可成功删除当前密钥 |
| [CF-P0-INTL-PC-044](overseas-pc/settings-billing/CF-P0-INTL-PC-044.md) | 海外PC | 海外主站 / 侧边栏 / 设置和账单 / API服务 / API密钥 | `api_key_agent` | 可自动化 | 点击创建新密钥 可成功创建新密钥信息 |
| [CF-P0-INTL-PC-045](overseas-pc/app-create/CF-P0-INTL-PC-045.md) | 海外PC | 海外主站 / 应用创建 / 文本框内输入需求文案 | `app_lifecycle_agent` | 可自动化 | 点击立即开发按钮进入需求澄清页面 |
| [CF-P0-INTL-PC-046](overseas-pc/app-create/CF-P0-INTL-PC-046.md) | 海外PC | 海外主站 / 应用创建 / 点击对话按钮 | `app_lifecycle_agent` | 可自动化 | 进入对话页面 |
| [CF-P0-INTL-PC-047](overseas-pc/app-create/CF-P0-INTL-PC-047.md) | 海外PC | 海外主站 / 应用创建 / 点击提示词气泡 | `app_lifecycle_agent` | 可自动化 | 提示词文案进入文本输入框 |
| [CF-P0-INTL-PC-048](overseas-pc/app-preview/CF-P0-INTL-PC-048.md) | 海外PC | 海外主站 / 应用预览页 / 应用页面展示 | `app_publish_test_agent` | 可自动化 | 应用完成后自动跳转至应用预览页默认展示应用页面 |
| [CF-P0-INTL-PC-049](overseas-pc/app-preview/CF-P0-INTL-PC-049.md) | 海外PC | 海外主站 / 应用预览页 / 应用页面展示 | `app_lifecycle_agent` | 可自动化 | 点击管理后台可跳转至应用管理后台页面 |
| [CF-P0-INTL-PC-050](overseas-pc/app-preview/CF-P0-INTL-PC-050.md) | 海外PC | 海外主站 / 应用预览页 / 应用页面展示 | `app_lifecycle_agent` | 可自动化 | 点击助手配置可打开助手配置页面 |
| [CF-P0-INTL-PC-051](overseas-pc/app-preview/CF-P0-INTL-PC-051.md) | 海外PC | 海外主站 / 应用预览页 / 顶部功能 | `app_lifecycle_agent` | 可自动化 | 会员用户点击下载按钮用户可将项目代码下载至本地 |
| [CF-P0-INTL-PC-052](overseas-pc/app-preview/CF-P0-INTL-PC-052.md) | 海外PC | 海外主站 / 应用预览页 / 顶部功能 | `app_publish_test_agent` | 可自动化 | 非会员用户点击触发付费弹窗 |
| [CF-P0-INTL-PC-053](overseas-pc/app-preview/CF-P0-INTL-PC-053.md) | 海外PC | 海外主站 / 应用预览页 / 顶部功能 | `app_lifecycle_agent` | 可自动化 | 点击刷新按钮刷新应用展示 |
| [CF-P0-INTL-PC-054](overseas-pc/app-preview/CF-P0-INTL-PC-054.md) | 海外PC | 海外主站 / 应用预览页 / 顶部功能 | `app_publish_test_agent` | 可自动化 | 点击发布按钮展示发布 H5 弹窗 |
| [CF-P0-INTL-PC-055](overseas-pc/app-preview/CF-P0-INTL-PC-055.md) | 海外PC | 海外主站 / 应用预览页 / 预览和分享 / 二维码展示 | `app_publish_test_agent` | 可自动化（本轮以二维码入口出现为通过标准；真实手机扫码访问暂不纳入自动化） | 手机扫码可正常访问应用h5页面 |
| [CF-P0-INTL-PC-056](overseas-pc/app-preview/CF-P0-INTL-PC-056.md) | 海外PC | 海外主站 / 应用预览页 / 预览和分享 / 二维码展示 | `app_publish_test_agent` | 可自动化 | 点击复制按钮可将应用分享链接复制进剪切板 |
| [CF-P0-INTL-PC-057](overseas-pc/app-preview/CF-P0-INTL-PC-057.md) | 海外PC | 海外主站 / 应用预览页 / 预览和分享 / 在线模式剩余时长 | `app_lifecycle_agent` | 可自动化 | 会员用户点击“好呀”开启全天候预览 |
| [CF-P0-INTL-PC-058](overseas-pc/app-preview/CF-P0-INTL-PC-058.md) | 海外PC | 海外主站 / 应用预览页 / 预览和分享 / 在线模式剩余时长 | `app_lifecycle_agent` | 可自动化 | 开启全天候预览时不展示剩余时长 |
| [CF-P0-INTL-PC-059](overseas-pc/app-preview/CF-P0-INTL-PC-059.md) | 海外PC | 海外主站 / 应用预览页 / 预览和分享 / 在线模式剩余时长 | `app_publish_test_agent` | 可自动化 | 非会员用户点击升级解锁按钮弹出付费弹窗 |
| [CF-P0-INTL-PC-060](overseas-pc/copy-app/CF-P0-INTL-PC-060.md) | 海外PC | 海外主站 / 复制应用 | `remix_agent` | 可自动化 | 应用广场点击应用，展示应用体验弹窗 |
| [CF-P0-INTL-PC-061](overseas-pc/copy-app/CF-P0-INTL-PC-061.md) | 海外PC | 海外主站 / 复制应用 | `remix_agent` | 可自动化 | 点击查看详情 进入全屏展示 |
| [CF-P0-INTL-PC-062](overseas-pc/copy-app/CF-P0-INTL-PC-062.md) | 海外PC | 海外主站 / 复制应用 / 做同款 | `remix_agent` | 可自动化 | 当前可创建应用数量大于等于1时，可将应用复制在我的应用列表中 |
| [CF-P0-INTL-PC-063](overseas-pc/copy-app/CF-P0-INTL-PC-063.md) | 海外PC | 海外主站 / 复制应用 / 做同款 | `remix_agent` | 可自动化 | 当前无可创建应用数量时，展示付费弹窗 |
| [CF-P0-INTL-PC-064](overseas-pc/app-preview/CF-P0-INTL-PC-064.md) | 海外PC | 海外主站 / 应用管理后台 / 首次登录引导 | `app_lifecycle_agent` | 可自动化 | 进入应用管理后台后首次登录引导视频不应自动播放 |
| [CF-P0-PC-001](domestic-pc/guest-home/CF-P0-PC-001.md) | 国内PC | 国内主站 / 未登录首页 | `auth_access_agent` | 可自动化 | 点击登录按钮跳转至登录页 |
| [CF-P0-PC-002](domestic-pc/guest-home/CF-P0-PC-002.md) | 国内PC | 国内主站 / 未登录首页 | `auth_access_agent` | 可自动化 | 输入文案点击立即开发跳转至登录页 |
| [CF-P0-PC-003](domestic-pc/wechat-auth/CF-P0-PC-003.md) | 国内PC | 国内主站 / 登录 / 微信登录 | `auth_access_agent` | 可自动化 | 点击微信登录展示登录二维码 |
| [CF-P0-PC-004](domestic-pc/phone-auth/CF-P0-PC-004.md) | 国内PC | 国内主站 / 登录 / 手机号验证码登录 | `auth_access_agent` | 可自动化 | 用户输入手机号点击获取验证码，验证码可发送至用户 |
| [CF-P0-PC-005](domestic-pc/phone-auth/CF-P0-PC-005.md) | 国内PC | 国内主站 / 登录 / 手机号验证码登录 | `auth_access_agent` | 可自动化 | 输入正确验证码，登录成功 |
| [CF-P0-PC-006](domestic-pc/auth/CF-P0-PC-006.md) | 国内PC | 国内主站 / 登录 | `auth_access_agent` | 可自动化 | 登录成功后进入应用创建页面 codeflying.net/develop |
| [CF-P0-PC-007](domestic-pc/top-nav/CF-P0-PC-007.md) | 国内PC | 国内主站 / 顶部导航 | `shell_navigation_agent` | 可自动化 | 左侧展示码上飞logo 点击进入应用广场页面 |
| [CF-P0-PC-008](domestic-pc/top-nav/CF-P0-PC-008.md) | 国内PC | 国内主站 / 顶部导航 | `shell_navigation_agent` | 可自动化 | 点击充值会员 弹出购买会员弹窗 |
| [CF-P0-PC-009](domestic-pc/top-nav/CF-P0-PC-009.md) | 国内PC | 国内主站 / 顶部导航 / 在线客服 | `shell_navigation_agent` | 可自动化 | 点击在线客服 弹出在线客服弹窗 |
| [CF-P0-PC-010](domestic-pc/top-nav/CF-P0-PC-010.md) | 国内PC | 国内主站 / 顶部导航 / 在线客服 | `shell_navigation_agent` | 可自动化 | 用户可输入文案与在线客服对话 |
| [CF-P0-PC-011](domestic-pc/top-nav/CF-P0-PC-011.md) | 国内PC | 国内主站 / 顶部导航 / 在线客服 | `shell_navigation_agent` | 可自动化 | 点击工单按钮展示工单列表弹窗 |
| [CF-P0-PC-012](domestic-pc/top-nav/CF-P0-PC-012.md) | 国内PC | 国内主站 / 顶部导航 / 语言选择 | `shell_navigation_agent` | 可自动化 | 用户可根据枚举选择语言类型 |
| [CF-P0-PC-013](domestic-pc/top-nav/CF-P0-PC-013.md) | 国内PC | 国内主站 / 顶部导航 / 语言选择 | `shell_navigation_agent` | 可自动化 | 切换页面语言并在验证后恢复中文 |
| [CF-P0-PC-014](domestic-pc/app-square/CF-P0-PC-014.md) | 国内PC | 国内主站 / 侧边栏 / 应用广场 | `shell_navigation_agent` | 可自动化 | 点击跳转至应用广场页面 |
| [CF-P0-PC-015](domestic-pc/app-square/CF-P0-PC-015.md) | 国内PC | 国内主站 / 侧边栏 / 应用广场 | `shell_navigation_agent` | 可自动化 | 顶部tab默认展示首位 |
| [CF-P0-PC-016](domestic-pc/app-square/CF-P0-PC-016.md) | 国内PC | 国内主站 / 侧边栏 / 应用广场 | `shell_navigation_agent` | 可自动化 | 切换tab展示对应页面内容 |
| [CF-P0-PC-017](domestic-pc/my-apps/CF-P0-PC-017.md) | 国内PC | 国内主站 / 侧边栏 / 我的应用 | `shell_navigation_agent` | 可自动化 | 点击跳转至应我的应用页面 |
| [CF-P0-PC-018](domestic-pc/my-apps/CF-P0-PC-018.md) | 国内PC | 国内主站 / 侧边栏 / 我的应用 | `shell_navigation_agent` | 可自动化 | 顶部tab默认展示该用户全部应用 |
| [CF-P0-PC-019](domestic-pc/my-apps/CF-P0-PC-019.md) | 国内PC | 国内主站 / 侧边栏 / 我的应用 | `shell_navigation_agent` | 可自动化 | 点击未发布tab展示该用户已创建未发布、创建中的应用 |
| [CF-P0-PC-020](domestic-pc/my-apps/CF-P0-PC-020.md) | 国内PC | 国内主站 / 侧边栏 / 我的应用 | `shell_navigation_agent` | 可自动化 | 点击已发布tab展示该用户已发布的应用 |
| [CF-P0-PC-021](domestic-pc/earn-points/CF-P0-PC-021.md) | 国内PC | 国内主站 / 侧边栏 / 赚取积分 | `invite_credit_agent` | 可自动化 | 点击跳转至应赚取积分页面 |
| [CF-P0-PC-022](domestic-pc/earn-points/CF-P0-PC-022.md) | 国内PC | 国内主站 / 侧边栏 / 赚取积分 | `invite_credit_agent` | 可自动化 | 点击复制链接按钮可将邀请链接复制至剪切板 |
| [CF-P0-PC-023](domestic-pc/earn-points/CF-P0-PC-023.md) | 国内PC | 国内主站 / 侧边栏 / 赚取积分 | `invite_credit_agent` | 可自动化 | 通过邀请链接注册新用户并验证邀请人积分到账 |
| [CF-P0-PC-024](domestic-pc/earn-points/CF-P0-PC-024.md) | 国内PC | 国内主站 / 侧边栏 / 赚取积分 | `invite_credit_agent` | 可自动化 | 非新用户注册奖励不下发 |
| [CF-P0-PC-025](domestic-pc/entitlements/CF-P0-PC-025.md) | 国内PC | 国内主站 / 侧边栏 / 我的权益 / 会员权益 | `membership_credit_agent` | 可自动化 | 每日免费积分展示每日获赠积分数及剩余积分数 / 每日获赠100积分 |
| [CF-P0-PC-026](domestic-pc/entitlements/CF-P0-PC-026.md) | 国内PC | 国内主站 / 侧边栏 / 我的权益 / 会员权益 | `membership_credit_agent` | 可自动化 | 会员每月积分展示对应会员等级获赠积分数及当前剩余积分数 / 免费版  0 |
| [CF-P0-PC-027](domestic-pc/entitlements/CF-P0-PC-027.md) | 国内PC | 国内主站 / 侧边栏 / 我的权益 / 会员权益 | `membership_credit_agent` | 可自动化 | 会员每月积分展示对应会员等级获赠积分数及当前剩余积分数 / 尊享版 27600 |
| [CF-P0-PC-028](domestic-pc/entitlements/CF-P0-PC-028.md) | 国内PC | 国内主站 / 侧边栏 / 我的权益 / 会员权益 | `membership_credit_agent` | 可自动化 | 自购积分包展示用户购买积分数及当前剩余积分数 |
| [CF-P0-PC-029](domestic-pc/entitlements/CF-P0-PC-029.md) | 国内PC | 国内主站 / 侧边栏 / 我的权益 / 会员权益 | `membership_credit_agent` | 可自动化 | 剩余可创建应用数展示对应会员等级可创建数量及剩余可创建数量 / 免费版  2 |
| [CF-P0-PC-030](domestic-pc/entitlements/CF-P0-PC-030.md) | 国内PC | 国内主站 / 侧边栏 / 我的权益 / 会员权益 | `membership_credit_agent` | 可自动化 | 剩余可创建应用数展示对应会员等级可创建数量及剩余可创建数量 / 尊享版 无限 |
| [CF-P0-PC-031](domestic-pc/entitlements/CF-P0-PC-031.md) | 国内PC | 国内主站 / 侧边栏 / 我的权益 / 积分消耗明细 | `membership_credit_agent` | 可自动化 | 点击展示积分消耗明细弹窗 |
| [CF-P0-PC-032](domestic-pc/settings-billing/CF-P0-PC-032.md) | 国内PC | 国内主站 / 侧边栏 / 设置和账单 / 设置 / 用户头像 | `membership_credit_agent` | 可自动化 | 正常展示用户头像 |
| [CF-P0-PC-033](domestic-pc/settings-billing/CF-P0-PC-033.md) | 国内PC | 国内主站 / 侧边栏 / 设置和账单 / 设置 / 用户昵称 | `membership_credit_agent` | 可自动化 | 正确展示用户昵称 |
| [CF-P0-PC-034](domestic-pc/settings-billing/CF-P0-PC-034.md) | 国内PC | 国内主站 / 侧边栏 / 设置和账单 / 设置 / 音色切换 | `membership_credit_agent` | 可自动化 | 正常展示音色名称 |
| [CF-P0-PC-035](domestic-pc/settings-billing/CF-P0-PC-035.md) | 国内PC | 国内主站 / 侧边栏 / 设置和账单 / 账单 / 账单列表 | `membership_credit_agent` | 可自动化 | 倒序展示仅三条支付数据 |
| [CF-P0-PC-036](domestic-pc/settings-billing/CF-P0-PC-036.md) | 国内PC | 国内主站 / 侧边栏 / 设置和账单 / 账单 / 查看全部账单历史 | `membership_credit_agent` | 可自动化 | 点击后弹窗倒序展示用户所有支付数据 |
| [CF-P0-PC-037](domestic-pc/settings-billing/CF-P0-PC-037.md) | 国内PC | 国内主站 / 侧边栏 / 设置和账单 / API服务 | `api_key_agent` | 可自动化 | 点进入API服务页面 |
| [CF-P0-PC-038](domestic-pc/settings-billing/CF-P0-PC-038.md) | 国内PC | 国内主站 / 侧边栏 / 设置和账单 / API服务 / 积分消耗情况 | `membership_credit_agent` | 可自动化 | 点击充值积分弹出购买弹窗 |
| [CF-P0-PC-039](domestic-pc/settings-billing/CF-P0-PC-039.md) | 国内PC | 国内主站 / 侧边栏 / 设置和账单 / API服务 / 积分消耗情况 | `membership_credit_agent` | 可自动化 | 剩余积分展示用户当前剩余总积分数 |
| [CF-P0-PC-040](domestic-pc/settings-billing/CF-P0-PC-040.md) | 国内PC | 国内主站 / 侧边栏 / 设置和账单 / API服务 / 积分消耗情况 | `membership_credit_agent` | 可自动化 | 本月已用积分展示用户本月已使用积分 |
| [CF-P0-PC-041](domestic-pc/settings-billing/CF-P0-PC-041.md) | 国内PC | 国内主站 / 侧边栏 / 设置和账单 / API服务 / API密钥 | `api_key_agent` | 可自动化 | 点击复制按钮可成功将密钥复制进剪切板 |
| [CF-P0-PC-042](domestic-pc/settings-billing/CF-P0-PC-042.md) | 国内PC | 国内主站 / 侧边栏 / 设置和账单 / API服务 / API密钥 | `api_key_agent` | 可自动化 | 点击删除按钮可成功删除当前密钥 |
| [CF-P0-PC-043](domestic-pc/settings-billing/CF-P0-PC-043.md) | 国内PC | 国内主站 / 侧边栏 / 设置和账单 / API服务 / API密钥 | `api_key_agent` | 可自动化 | 点击创建新密钥 可成功创建新密钥信息 |
| [CF-P0-PC-044](domestic-pc/app-create/CF-P0-PC-044.md) | 国内PC | 国内主站 / 应用创建 / 文本框内输入需求文案 | `app_lifecycle_agent` | 可自动化 | 点击立即开发按钮进入需求澄清页面 |
| [CF-P0-PC-045](domestic-pc/app-create/CF-P0-PC-045.md) | 国内PC | 国内主站 / 应用创建 / 点击对话按钮 | `app_lifecycle_agent` | 可自动化 | 进入对话页面 |
| [CF-P0-PC-046](domestic-pc/app-create/CF-P0-PC-046.md) | 国内PC | 国内主站 / 应用创建 / 点击提示词气泡 | `app_lifecycle_agent` | 可自动化 | 提示词文案进入文本输入框 |
| [CF-P0-PC-047](domestic-pc/app-preview/CF-P0-PC-047.md) | 国内PC | 国内主站 / 应用预览页 / 应用页面展示 | `app_publish_test_agent` | 可自动化 | 应用完成后自动跳转至应用预览页默认展示应用页面 |
| [CF-P0-PC-048](domestic-pc/app-preview/CF-P0-PC-048.md) | 国内PC | 国内主站 / 应用预览页 / 应用页面展示 | `app_lifecycle_agent` | 可自动化 | 点击管理后台可跳转至应用管理后台页面 |
| [CF-P0-PC-049](domestic-pc/app-preview/CF-P0-PC-049.md) | 国内PC | 国内主站 / 应用预览页 / 顶部功能 / 更多 | `app_lifecycle_agent` | 可自动化 | 点击更多打开更多页面并默认展示配置助手 |
| [CF-P0-PC-050](domestic-pc/app-preview/CF-P0-PC-050.md) | 国内PC | 国内主站 / 应用预览页 / 顶部功能 | `app_lifecycle_agent` | 可自动化 | 会员用户点击下载按钮用户可将项目代码下载至本地 |
| [CF-P0-PC-051](domestic-pc/app-preview/CF-P0-PC-051.md) | 国内PC | 国内主站 / 应用预览页 / 顶部功能 | `app_publish_test_agent` | 可自动化 | 非会员用户在源码下载页点击下载按钮触发付费弹窗 |
| [CF-P0-PC-052](domestic-pc/app-preview/CF-P0-PC-052.md) | 国内PC | 国内主站 / 应用预览页 / 顶部功能 | `app_lifecycle_agent` | 可自动化 | 点击刷新按钮刷新应用展示 |
| [CF-P0-PC-053](domestic-pc/app-preview/CF-P0-PC-053.md) | 国内PC | 国内主站 / 应用预览页 / 顶部功能 | `app_publish_test_agent` | 可自动化 | 点击发布按钮展示发布应用弹窗并可进入 H5 发布 |
| [CF-P0-PC-054](domestic-pc/app-preview/CF-P0-PC-054.md) | 国内PC | 国内主站 / 应用预览页 / 顶部功能 / 分享 | `app_publish_test_agent` | 可自动化 | 点击分享按钮展示分享海报弹窗 |
| [CF-P0-PC-055](domestic-pc/app-preview/CF-P0-PC-055.md) | 国内PC | 国内主站 / 应用预览页 / 发布 / 网页应用 | `app_publish_test_agent` | 可自动化 | 点击复制按钮可将应用分享链接复制进剪切板 |
| [CF-P0-PC-056](domestic-pc/app-preview/CF-P0-PC-056.md) | 国内PC | 国内主站 / 应用预览页 / 预览和分享 / 在线模式剩余时长 | `app_lifecycle_agent` | 可自动化 | 会员用户通过剩余时长菜单开启永久在线 |
| [CF-P0-PC-057](domestic-pc/app-preview/CF-P0-PC-057.md) | 国内PC | 国内主站 / 应用预览页 / 预览和分享 / 在线模式剩余时长 | `app_lifecycle_agent` | 可自动化 | 开启全天候预览时不展示剩余时长 |
| [CF-P0-PC-058](domestic-pc/app-preview/CF-P0-PC-058.md) | 国内PC | 国内主站 / 应用预览页 / 发布 / 网页应用 | `app_publish_test_agent` | 可自动化 | 非会员用户点击永久在线弹出付费弹窗 |
| [CF-P0-PC-059](domestic-pc/app-preview/CF-P0-PC-059.md) | 国内PC | 国内主站 / 应用预览页 / 预览和分享 / 发布状态 | `app_publish_test_agent` | 可自动化 | 微信小程序展示当前发布状态并可选择发布版本 |
| [CF-P0-PC-060](domestic-pc/app-preview/CF-P0-PC-060.md) | 国内PC | 国内主站 / 应用预览页 / 预览和分享 / 发布状态 | `app_publish_test_agent` | 可自动化 | 发布为其他渠道打开其他渠道弹窗 |
| [CF-P0-PC-061](domestic-pc/copy-app/CF-P0-PC-061.md) | 国内PC | 国内主站 / 复制应用 | `app_lifecycle_agent` | 可自动化 | 应用广场点击应用，展示应用体验弹窗 |
| [CF-P0-PC-062](domestic-pc/copy-app/CF-P0-PC-062.md) | 国内PC | 国内主站 / 应用广场 / 应用详情 | `remix_agent` | 可自动化 | 公开应用点击查看详情后全屏展示 |
| [CF-P0-PC-063](domestic-pc/copy-app/CF-P0-PC-063.md) | 国内PC | 国内主站 / 应用广场 / 做同款 | `remix_agent` | 可自动化 | 有可用额度时做同款并出现在我的应用 |
| [CF-P0-PC-064](domestic-pc/copy-app/CF-P0-PC-064.md) | 国内PC | 国内主站 / 应用广场 / 做同款 | `remix_agent` | 可自动化 | 无可用额度时做同款展示付费弹窗 |
| [CF-P0-PC-065](domestic-pc/app-preview/CF-P0-PC-065.md) | 国内PC | 国内主站 / 应用管理后台 / 首次登录引导 | `app_lifecycle_agent` | 可自动化 | 进入应用管理后台后首次登录引导视频不应自动播放 |
| [CF-P0-PC-066](domestic-pc/app-preview/CF-P0-PC-066.md) | 国内PC | 国内主站 / 应用预览页 / 顶部功能 / 水印管理 | `app_publish_test_agent` | 可自动化 | 点击水印管理进入水印管理页面 |
| [CF-P0-PC-067](domestic-pc/app-preview/CF-P0-PC-067.md) | 国内PC | 国内主站 / 应用预览页 / 顶部功能 / 水印管理 | `app_publish_test_agent` | 可自动化 | 会员用户可关闭应用水印 |
| [CF-P0-PC-068](domestic-pc/app-preview/CF-P0-PC-068.md) | 国内PC | 国内主站 / 应用预览页 / 顶部功能 / 水印管理 | `app_publish_test_agent` | 可自动化 | 非会员用户关闭应用水印时展示付费弹窗 |
