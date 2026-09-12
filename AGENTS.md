# AGENTS.md

## Project

AuroraNLP - 专业级中文自然语言处理工具包，纯 Python 标准库实现，覆盖分词到企业级部署。

## Commands

```bash
# 安装
pip install -e ".[all]"

# 测试
pytest -v --cov=AuroraNLP tests/
pytest tests/test_segment.py -v              # 单个模块
pytest -m "not slow"                         # 跳过慢测试

# Lint & Format
ruff check .                                 # 代码检查（0 errors 预期）
ruff check . --fix --unsafe-fixes            # 自动修复
black .                                      # 格式化
black --check .                              # 检查格式（CI 会运行）
```

## Architecture

```
AuroraNLP/                    # 项目根目录 = 包根（非标准布局，见 setup.py package_dir）
├── __init__.py               # 统一聚合所有公开 API（~250 个导出符号）
├── core/                     # 核心工具：tokenizer、batch_processor、performance、benchmark
├── dictionary/               # 词典系统：Trie、Dictionary、UserDictionary、版本管理、领域词典
├── segmentation/             # 分词算法：HMM、CRF、感知器、词格、混合策略、歧义检测
├── ner/                      # 命名实体识别：CRF-NER、实体链接、人名/地名/机构名
├── parsing/                  # 句法分析：依存分析（Arc-Eager）、成分分析（PCFG/CKY）、POS
├── text_analysis/            # 文本分析：关键词提取、相似度、情感分析
├── corpus/                   # 语料工具：构建、标注、主动学习
├── deep_learning/            # 深度学习：BiLSTM-CRF、预训练模型（BERT/ALBERT/DistilBERT）
├── pipeline/                 # Pipeline 系统：组件注册、异步、流式、插件、API Server
├── managers/                 # 统一管理器接口
├── enterprise/               # 企业级：日志、健康检查、Prometheus、限流熔断、灰度发布
├── data/                     # 数据资源：词典、停用词、领域词库、同义词词林
├── tests/                    # 626+ 个测试用例（pytest）
├── examples/                 # 示例代码
├── docs/                     # 文档（快速入门、用户手册、最佳实践、FAQ）
├── setup.py                  # 打包配置（package_dir 映射 AuroraNLP -> .）
├── pyproject.toml            # ruff 配置
├── pytest.ini                # pytest 配置
└── requirements.txt          # 依赖说明
```

## Conventions

### Python Version
- 最低支持 Python 3.8，CI 测试 3.8/3.9/3.10/3.11
- 使用 `from __future__ import annotations` 支持现代类型注解语法（`list[X]`、`X | None`）

### Code Style
- **Black** 格式化，行宽 120
- **isort** 排序导入（`known-first-party = ["AuroraNLP"]`）
- **Ruff** 检查，忽略规则见 `pyproject.toml`（中文全角标点、前向引用等）
- 中文注释和 docstring

### Naming
- 文件名：`snake_case.py`
- 类名：`PascalCase`
- 函数/变量：`snake_case`
- 常量：`UPPER_SNAKE_CASE`
- 模块内私有：`_leading_underscore`

### Type Annotations
- 公开 API 使用类型注解
- 前向引用用字符串 `'ClassName'`（F821 被忽略）
- Optional 参数默认值用 `= None`

### Testing
- 测试文件：`tests/test_<module>.py`
- 测试类：`TestXxx`
- 测试方法：`test_xxx`
- 使用 pytest fixtures（见 `tests/conftest.py`）
- 慢测试标记：`@pytest.mark.slow`

### 非标准布局说明
项目根目录即 Python 包根（`__init__.py` 在根目录）。`setup.py` 通过 `package_dir` 映射：
```python
package_dir = {'AuroraNLP': '.', 'AuroraNLP.core': 'core', ...}
```
因此 `import AuroraNLP` 实际加载根目录的 `__init__.py`。

## CI

- **test**: pytest + coverage，多 OS/Python 矩阵
- **lint**: `ruff check .` + `black --check .`
- PR 合并前必须通过全部检查
