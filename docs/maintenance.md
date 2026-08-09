# 用例维护说明

## 放哪里

- P0 用例放到 `cases/P0/`
- P1 用例放到 `cases/P1/`
- P2 用例放到 `cases/P2/`

P0 冒烟用例放到 `cases/P0/smoke/`，一条 TC 一个 Markdown，并通过同目录的 `README.md` 查看索引。

Agent 能力测评集放到 `suites/demo/`，不要放进 `cases/P0/`。测评集可能与产品冒烟用例覆盖相似场景，分开存放可以避免 runner 递归读取时重复执行。

根目录中的原始 XMind 和提取版 Markdown 只作为来源文件保留，不作为正式自动化输入。XMind 只保留一份，不要复制到 `cases/` 或其他目录。

不需要改 suite。老郭按目录递归读取 Markdown 即可。

## 从 XMind 重新生成

在仓库根目录执行：

```bash
python3 scripts/split_xmind_smoke_cases.py --force
```

生成前先提交或备份人工维护过的 Markdown。`--force` 会重建
`cases/P0/smoke/`，因此只应在明确需要用 XMind 覆盖生成结果时使用。

## 怎么命名

推荐：

```text
TC-001-create-app-lite.md
TC-603-payment-qrcode.md
publish-and-preview.md
```

文件名不强制，但用例 ID 必须在正文里唯一。

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
