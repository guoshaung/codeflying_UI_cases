# 用例维护说明

## 放哪里

- P0 用例放到 `cases/P0/`
- P1 用例放到 `cases/P1/`
- P2 用例放到 `cases/P2/`

P0 冒烟用例放到 `cases/P0/smoke/`，一条 TC 一个 Markdown，并通过同目录的 `README.md` 查看索引。

Agent 能力测评集放到 `suites/demo/`，不要放进 `cases/P0/`。测评集可能与产品冒烟用例覆盖相似场景，分开存放可以避免 runner 递归读取时重复执行。

不需要改 suite。老郭按目录递归读取 Markdown 即可。

## 怎么命名

推荐：

```text
TC-001-create-app-lite.md
TC-603-payment-qrcode.md
publish-and-preview.md
```

文件名不强制，但用例 ID 必须在正文里唯一。

## 新增用例放哪里

正式冒烟用例固定放到：

```text
cases/P0/smoke/<市场>-<平台>/<模块>/<CASE_ID>.md
```

目录示例：

- 国内 PC：`cases/P0/smoke/domestic-pc/app-preview/CF-P0-PC-065.md`
- 国内 H5：`cases/P0/smoke/domestic-h5/profile/CF-P0-H5-041.md`
- 海外 PC：`cases/P0/smoke/overseas-pc/auth/CF-P0-INTL-PC-064.md`
- 海外 H5：`cases/P0/smoke/overseas-h5/app-create/CF-P0-INTL-H5-042.md`

每条新增用例必须填写 `Agent 分组`，只能使用：

- `auth_access_agent`
- `guest_explore_agent`
- `shell_navigation_agent`
- `invite_credit_agent`
- `membership_credit_agent`
- `api_key_agent`
- `app_lifecycle_agent`
- `app_publish_test_agent`
- `publish_agent`
- `remix_agent`
- `profile_support_agent`

Web 自动测试每轮开始前会比较 GitHub 新旧提交。新增用例按 `Agent 分组` 放入对应功能 Agent；修改用例覆盖原文件；删除用例同时从功能 Agent 移除。缺少有效分组的新增用例不会执行，也不会由系统猜测归属。

## 什么时候定 P0 / P1 / P2

- P0：核心流程走不下去；支付/计费错误；数据丢失、泄露、越权；商业化受阻。
- P1：流程能绕过，但严重影响体验、效率或转化。
- P2：轻微体验问题、低频边界问题。

拿不准时先往高一级放，后续 review 再降级。

## 自动化注意事项

- 只看到按钮不等于功能成功。
- HTTP 200 不等于业务成功。
- 工具报错后重试成功，记 `RETRY_PASS`，不要直接记普通 `PASS`。
- 阻塞、未验证、未执行都不能计入通过数。
- 报告数量必须守恒：`PASS + RETRY_PASS + FAIL + BLOCKED + NOT_RUN = 实际用例数`。
- `MANUAL_REQUIRED` 要与自动化失败分开统计，不能因为人工依赖而判定自动化 FAIL。
- 涉及账号、应用、支付、邀请、API 密钥的用例必须填写数据锁和清理动作。
