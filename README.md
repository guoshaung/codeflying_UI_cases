# CodeFlying UI Cases

这个仓库用于维护 CodeFlying / 码上飞的 UI 产品可用性测试用例，主要给人工测试和 Playwright 自动化测试 Agent（老郭）使用。

当前版本采用 **Markdown 为主** 的组织方式：Agent 更容易直接阅读完整上下文，也方便测试工程师人工 review。后续如果用例很多，再考虑补充结构化索引。

## 目录结构

```text
.
├── cases/                 # 测试用例正文，Markdown 格式
│   └── basic/             # 基础稳定用例集
├── suites/                # 测试集合说明：告诉老郭本次跑哪份用例
├── templates/             # 新增用例模板
└── docs/                  # 维护规则、执行规则、报告规则
```

## 当前核心用例

当前基础 10 条用例放在：

- [cases/basic/CodeFlying_10_robust_evaluation_cases.md](cases/basic/CodeFlying_10_robust_evaluation_cases.md)

这份用例集适合用于：

- 基础冒烟测试；
- 每日 P0 巡检的初始版本；
- 老郭自动化能力验收。

## Suites 是什么

`suites/` 不是新的用例格式，只是“本次执行范围说明”。

例如：

- [suites/demo-basic-10.md](suites/demo-basic-10.md)：演示和基础回归时，让老郭执行当前 10 条 Markdown 用例。
- [suites/daily-p0.md](suites/daily-p0.md)：每日 P0 巡检时，先复用基础 10 条，后续可以扩展。

这样做的好处是：以后仓库里有多份 Markdown 用例时，可以明确告诉老郭“这次跑哪份”，避免它自己乱选。

## 如何调用老郭

可以把下面这段发给老郭：

```text
请读取 GitHub 仓库中的测试用例：
https://github.com/guoshaung/codeflying_UI_cases

本次执行 suites/demo-basic-10.md。
以该 suite 指定的 Markdown 用例为最高优先级，不要使用其他旧用例。

测试环境：dev。
平台：国内 PC。
登录态：已登录，不测试登录。

执行完成后请生成 Markdown 日常简报，包含：
1. 跑了多少条；
2. PASS / RETRY_PASS / FAIL / BLOCKED / NOT_RUN 数量；
3. P0 / P1 / P2 失败和阻塞明细；
4. 关键证据路径；
5. 是否建议继续回归。
```

上线前测试时，可以改成：

```text
执行完成后请生成 Markdown 上线报告，结论使用：可发布 / 有条件发布 / 阻断 / 建议回滚。
```

## 新增用例怎么写

新增用例建议继续使用 Markdown。可以复制：

- [templates/case-template.md](templates/case-template.md)

最低要求：

- 有唯一用例 ID；
- 有 P0 / P1 / P2；
- 有模块；
- 有平台；
- 有执行方式：可自动化 / 真人依赖 / agent 行为评测；
- 有前置条件、步骤、预期结果、失败条件和证据要求。

## 重要约定

1. 登录可以作为前置条件，不一定纳入用例数量。
2. 支付相关用例需要区分“二维码生成成功”和“真实支付成功”；没有支付沙箱时，真实支付应标记为真人依赖或 BLOCKED。
3. 下载源码必须验证文件真实落盘、非空、类型可读，不能只看按钮点击。
4. 二维码必须验证资源加载正常且可识别，不能只靠肉眼看到。
5. P0 用例失败或阻塞时，不应输出“全部通过”或“建议上线”。

