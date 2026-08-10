# CF-P0-PC-064 无可用额度时做同款展示付费弹窗

- 优先级：P0
- 模块：国内主站 / 应用广场 / 做同款
- 平台：国内PC
- 执行方式：可自动化
- 用户类型：免费用户
- Agent 分组：remix_agent
- 账号类型：`free_account`
- 账号与域名：`FREE_SESSION` + `https://dev.codeflying.net/`
- 是否修改数据：正常路径 no；前置不符时可能误创建应用
- 数据锁：`remix:free_account`
- 清理动作：如果前置不符并误创建应用，只删除本轮新增的 app id

## 前置条件

1. 关闭会员 Browser Context，新建独立免费 Browser Context。
2. 只使用总控传入的 `FREE_SESSION`，在免费 Browser Context 中加载一次；不得使用 `MEMBER_SESSION`。
3. 免费账号当前可创建应用数量必须为 0。
4. 应用广场至少有一个已加载完成、可打开详情的公开应用。

## 测试步骤

1. 打开免费环境的应用广场，打开一个稳定的公开应用详情。
2. 记录点击前“我的应用”的 app id 集合，截图为 `CF-P0-PC-064-before.png`。
3. 点击“做同款”、`Remix`、`Duplicate`、`Copy` 或 `Clone` 中实际可见的等价按钮。
4. 等待付费/升级弹窗出现，记录弹窗标题、主文案、付费或升级按钮和关闭入口，截图为 `CF-P0-PC-064-after.png`。
5. 确认“我的应用”没有新增 app id，然后立即写入独立 `result.json`。

## 通过标准

- 点击做同款后展示付费、升级会员或额度不足弹窗。
- 弹窗至少包含清晰的额度/付费说明、可操作的付费或升级入口和关闭入口。
- 页面未进入新应用路由，“我的应用”没有新增 app id。

## 失败与阻塞

- 确认免费账号额度为 0，但点击后没有弹窗，或绕过额度校验创建了新应用：`FAIL`。
- 免费账号实际仍有额度：`BLOCKED_TEST_DATA`；如果已新增应用，先记录并删除唯一的 `new_app_id`。
- 免费 session 缺失、已失效或被识别为会员账号：`BLOCKED_ACCOUNT_REQUIRED`。
- 应用广场没有可用的公开应用：`BLOCKED_TEST_DATA`。

## 证据要求

- `CF-P0-PC-064-before.png`
- `CF-P0-PC-064-after.png`
- 页面 URL、弹窗标题、主文案、付费/升级按钮和关闭入口的 DOM 状态
- 点击前后 app id 集合；如果前置不符，还要记录 `new_app_id` 和清理结果
