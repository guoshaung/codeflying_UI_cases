# 用例维护说明

## 放哪里

- P0 用例放到 `cases/P0/`
- P1 用例放到 `cases/P1/`
- P2 用例放到 `cases/P2/`

不需要改 suite，不需要维护索引。老郭按目录读取即可。

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
