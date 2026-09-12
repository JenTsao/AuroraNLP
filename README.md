# AuroraNLP

**专业级中文自然语言处理工具包**

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-626-passing-brightgreen.svg)](#测试)

AuroraNLP 是一个使用纯 Python 标准库实现的中文 NLP 工具包，覆盖从基础分词到企业级部署的完整链路。

---

## 核心特性

| 功能 | 描述 |
|------|------|
| **分词** | 正向最大匹配、HMM、CRF、感知机、词格、混合策略 |
| **词性标注** | HMM / CRF / 感知机 POS Tagger |
| **命名实体识别** | CRF-NER、嵌套实体识别、知识库链接 |
| **句法分析** | 依存分析（Arc-Eager）、成分分析（PCFG/CKY） |
| **文本分析** | 关键词提取、情感分析、文本相似度 |
| **词典系统** | 用户词典、领域词典、版本管理、热更新 |
| **深度学习** | BiLSTM-CRF、BERT、ALBERT、DistilBERT |
| **企业级** | Pipeline、REST API、gRPC、Docker/K8s |

---

## 快速开始

### 安装

```bash
# 基础安装
pip install .

# 开发模式（含测试/代码检查依赖）
pip install ".[all]"
```

### 基础分词

```python
from AuroraNLP import Segmentor

seg = Segmentor()
words = seg.segment("今天天气真不错，我们去公园散步吧！")
print(words)
# ['今天', '天气', '真不错', '，', '我们', '去', '公园', '散步', '吧', '！']
```

### 命名实体识别

```python
from AuroraNLP import NERRecognizer

ner = NERRecognizer()
text = "阿里巴巴集团的张勇董事长今天在杭州出席了会议"
for entity in ner.recognize(text):
    print(f"{entity.text} ({entity.type}): {entity.start}-{entity.end}")
# 阿里巴巴集团 (ORG): 0-5
# 张勇 (PER): 8-10
# 杭州 (LOC): 16-18
```

### Pipeline 系统

```python
from AuroraNLP import Pipeline, Segmentor, NERRecognizer

nlp = Pipeline()
nlp.add_component(Segmentor())
nlp.add_component(NERRecognizer())

doc = nlp("张三在阿里巴巴位于杭州的总部工作")
print(doc.ents)  # 提取所有实体
```

---

## 项目结构

```
AuroraNLP/
├── __init__.py            # 包入口，统一聚合所有公开 API
├── core/                  # 核心工具（分词器、批处理、性能监控）
├── dictionary/            # 词典系统（Trie、用户词典、领域词典、版本管理）
├── segmentation/          # 分词算法（HMM、CRF、感知机、混合策略）
├── ner/                   # 命名实体识别（CRF-NER、实体链接、人名/地名/机构名）
├── parsing/               # 句法分析（依存分析、成分分析、词性标注）
├── text_analysis/         # 文本分析（关键词、相似度、情感）
├── corpus/                # 语料工具（构建、标注、主动学习）
├── deep_learning/         # 深度学习（BiLSTM-CRF、预训练模型）
├── pipeline/              # Pipeline 系统（组件注册、异步、插件）
├── managers/              # 管理器（字典、分词器、相似度统一接口）
├── enterprise/            # 企业级功能（日志、监控、鉴权、部署）
├── data/                  # 数据资源（词典、停用词、领域词库）
├── tests/                 # 测试套件（626 个测试用例）
├── examples/              # 示例代码
├── docs/                  # 项目文档
├── setup.py               # 打包配置
└── requirements.txt       # 依赖说明
```

---

## 文档

| 文档 | 说明 |
|------|------|
| [快速入门](docs/getting-started.md) | 5 分钟上手 AuroraNLP |
| [用户手册](docs/user-guide.md) | 完整功能详解 |
| [最佳实践](docs/best-practices.md) | 性能优化与生产部署 |
| [FAQ](docs/faq.md) | 常见问题解答 |
| [HMM 分词](docs/HMM.md) | 隐马尔可夫模型详解 |
| [CRF 分词](docs/CRF.md) | 条件随机场详解 |

---

## 开发指南

### 运行测试

```bash
# 运行全部测试
pytest

# 运行特定模块测试
pytest tests/test_segment.py -v

# 生成覆盖率报告
pytest --cov=AuroraNLP tests/
```

### 代码检查

```bash
# 格式化代码
black .
isort .

# 代码检查
ruff check .
```

### 提交 PR

请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解完整的贡献流程。

---

## 相关链接

- **GitHub**: https://github.com/AuroraNLP/AuroraNLP
- **Issues**: https://github.com/AuroraNLP/AuroraNLP/issues
- **PyPI**: https://pypi.org/project/aurora-nlp/

---

## 许可证

本项目基于 [Apache License 2.0](LICENSE) 开源。

---

**AuroraNLP Team** | 2026
