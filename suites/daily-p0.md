# Suite: daily-p0

## 用途

每日 P0 巡检使用。

当前先复用基础稳定 10 条用例，后续可以把更多 P0 Markdown 用例追加到本文件中。

## 执行范围

- [../cases/basic/CodeFlying_10_robust_evaluation_cases.md](../cases/basic/CodeFlying_10_robust_evaluation_cases.md)

## 报告要求

生成 Markdown 日常简报，至少包含：

1. 总用例数；
2. PASS / RETRY_PASS / FAIL / BLOCKED / NOT_RUN 数量；
3. P0 失败和阻塞明细；
4. 与上一轮结果对比；没有历史基线时写“暂无历史基线”；
5. 是否建议继续回归。

