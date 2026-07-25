# 宝妈指数（Mom Index）

> **公开初版 / Framework v0.1**
> 本仓库提供一个可运行、可扩展的行为金融分析框架。规则、权重和示例数据仅用于演示，实际使用时应结合自己的研究目标、数据质量与回测结果持续完善。

宝妈指数用于观察中文社交平台上大众散户与投资新手的讨论热度、情绪极端程度以及买卖倾向。指数越高，代表相关讨论越集中、情绪越极端；它是一种研究性观察指标，不是交易指令。

## 为什么公开的是框架版

公开版本展示了完整的数据流和扩展接口，但不包含维护者当前使用的私有策略、模型提示词、生产校准逻辑或原始社交平台数据。

- 分析层使用早期关键词规则与固定权重，便于理解和修改。
- 数据文件为脱敏、合成的演示样本，不对应任何真实用户。
- 采集器只提供接口和示例实现；使用者应自行确认平台条款与数据授权。
- 指数公式是研究起点，不代表当前私有版本，也不保证投资有效性。

## 项目结构

```text
mom-index/
├── pipeline.py                  # 采集 → 分析 → 指数 → 数据输出
├── analyzer/
│   ├── llm_analyzer.py         # v0.1 规则型文本分析器（名称沿用历史）
│   └── index_calculator.py     # 初版固定权重计算
├── collectors/
│   ├── guba_collector.py       # 公开网页采集示例
│   ├── xhs_collector.py        # 可选数据源接口
│   └── anti_detection.py       # 历史实验代码
├── data/                        # 脱敏演示数据
├── frontend/
│   ├── dashboard.html          # Chart.js 看板
│   ├── chart.umd.min.js        # 本地依赖，避免 CDN 波动
│   └── server.py               # 本地无缓存服务器
├── .env.example
├── requirements.txt
└── LICENSE
```

## 初版分析思路

框架把文本信号分为四类：

1. 身份与知识求助信号；
2. 追涨、恐慌和决策依赖信号；
3. 买入、卖出与观望意图；
4. 专业术语、风险意识和长期视角等反向信号。

示例综合指数由以下维度组成：

```text
宝妈指数 = 新手讨论占比 × 40%
         + 新手信号强度 × 25%
         + 情绪极端度 × 20%
         + 信号纯度 × 15%
```

这些权重只是 v0.1 的可读基线。建议使用者补充语义模型、置信度评估、数据去偏、时间衰减和历史回测。

## 快速开始

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 运行示例流程
py -3 pipeline.py

# 启动看板
py -3 frontend/server.py 8765
```

浏览器打开 <http://localhost:8765/dashboard.html>。

## 数据安全

仓库中的帖子、时间序列和统计结果均为脱敏演示数据。请勿提交以下内容：

- Cookie、登录状态、浏览器 Profile；
- API Key、访问令牌或 `.env`；
- 未经授权的原始帖子、评论、用户 ID；
- 含真实个人信息的截图、调试页面或日志。

## 如何扩展

- 实现新的 collector，并输出统一的帖子字段；
- 替换 `analyzer/llm_analyzer.py` 为自己的规则或模型；
- 在 `index_calculator.py` 中加入校准、衰减或不同权重；
- 用历史样本建立离线回测和误差评估；
- 为 Dashboard 增加更多板块和指标。

## 关联项目

- [宝爸指数（Dad Index）](https://github.com/mihang123/dad-index)：面向经验型投资者讨论的配套框架。

## 免责声明

本项目仅用于行为金融研究、软件工程演示与科普，不构成任何投资建议。示例指数未经充分实证验证，使用者应独立判断并自行承担风险。

## License

[MIT](LICENSE)
