# CodeFlying UI Cases

码上飞 UI 产品可用性测试用例库。

这个仓库只做一件事：让测试同学和自动化测试 Agent（老郭）能快速找到、维护、执行用例。

## 最简单的维护方式

新增用例时，直接按优先级放到对应目录：

```text
cases/
├── P0/        # 核心流程、支付/计费、数据安全、商业化阻断
├── P1/        # 严重体验问题，流程可绕过但影响明显
└── P2/        # 一般体验问题、低频边界问题
```

每个用例文件使用 Markdown。可以一份文件写一条用例，也可以一份文件写一组相关用例。

当前核心 10 条 P0 用例在：

- [cases/P0/CodeFlying_10_robust_evaluation_cases.md](cases/P0/CodeFlying_10_robust_evaluation_cases.md)

## 老郭怎么读取

常用提示词：

```text
请读取 GitHub 仓库：
https://github.com/guoshaung/codeflying_UI_cases

本次只执行 cases/P0 下的 Markdown 用例。
不要读取历史旧用例，不要自行扩展额外用例。

测试环境：dev
平台：国内 PC
登录态：已登录，不测试登录

执行完成后输出 Markdown 报告，必须包含：
1. 总共跑了多少条；
2. PASS / RETRY_PASS / FAIL / BLOCKED / NOT_RUN 数量；
3. P0 / P1 / P2 分层结果；
4. 失败、阻塞、未验证明细；
5. 关键证据路径；
6. 是否建议继续回归。
```

如果只想跑某个优先级，把 `cases/P0` 改成 `cases/P1` 或 `cases/P2` 即可。

## 新增用例格式

复制模板：

- [templates/case-template.md](templates/case-template.md)

每条用例至少写清楚：

- 用例 ID
- 标题
- 优先级：P0 / P1 / P2
- 模块
- 平台：国内 PC / 国内 H5 / 海外 PC / 海外 H5
- 执行方式：可自动化 / 真人依赖 / agent 行为评测
- 前置条件
- 测试步骤
- 预期结果
- 通过标准
- 失败条件
- 证据要求

## 几条硬规则

1. 登录可以是前置条件；如果本次不测登录，不要把登录计入用例数。
2. 支付要拆开：二维码生成、mock/沙箱支付、真实扫码支付不是同一件事。
3. 下载源码必须验证文件真实落盘、大小大于 0、文件可读。
4. 二维码必须验证图片资源加载正常；能扫码/能解码时再写“可识别”。
5. P0 有失败、阻塞或证据不足时，报告不能写“全部通过”或“建议上线”。

更多维护说明见：

- [docs/maintenance.md](docs/maintenance.md)
