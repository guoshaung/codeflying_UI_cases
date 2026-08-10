# CF-P0-INTL-PC-003 点击 Google 登录并成功返回海外主站

## 元信息

- 优先级：P0
- 平台：海外PC
- FM 模块：海外主站 / 登录 / Google 登录
- Agent 分组：`auth_access_agent`
- 执行方式：第三方账号依赖（自动化检查入口、授权页和回跳）
- 来源：`码上飞冒烟测试用例--海外版.md`
- 原始 TC：点击 Google 登录并成功返回海外主站

## 前置条件

- 海外站入口：`https://www.codeflying.app/`
- 使用专门的海外测试账号或海外 storage state；禁止复用国内站 cookie。

## 测试步骤

1. 使用干净 Browser Context 打开海外主站。
2. 点击 Google 登录按钮，确认进入真实 Google 授权链路。
3. 使用获准的测试账号完成授权；若环境禁止第三方登录，只验证授权入口与回跳地址并记录 BLOCKED。

## 预期结果

1. Google 登录入口可用且授权请求参数完整。
2. 授权成功后返回 codeflying.app，并建立海外站登录态。

## 结果记录

- 状态：PASS / FAIL / BLOCKED
- 证据：截图、最终 URL、关键网络响应；不得记录密码、cookie 或 token。
