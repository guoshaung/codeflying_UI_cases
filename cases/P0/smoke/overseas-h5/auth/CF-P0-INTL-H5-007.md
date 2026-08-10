# CF-P0-INTL-H5-007 H5 点击 Google 登录并成功返回

## 元信息

- 优先级：P0
- 平台：海外H5
- FM 模块：海外H5 / 登录 / Google 登录
- Agent 分组：`auth_access_agent`
- 执行方式：第三方账号依赖（自动化检查入口、授权页和回跳）
- 来源：`码上飞冒烟测试用例--海外版.md`
- 原始 TC：H5 点击 Google 登录并成功返回

## 前置条件

- 海外站入口：`https://www.codeflying.app/`
- 使用专门的海外测试账号或海外 storage state；禁止复用国内站 cookie。

## 测试步骤

1. 使用移动端 viewport 打开海外 H5 首页。
2. 点击 Google 登录并验证授权入口。
3. 使用获准的测试账号完成授权；环境不支持时记录 BLOCKED。

## 预期结果

1. 授权成功后回到海外 H5，并建立登录态。

## 结果记录

- 状态：PASS / FAIL / BLOCKED
- 证据：截图、最终 URL、关键网络响应；不得记录密码、cookie 或 token。
