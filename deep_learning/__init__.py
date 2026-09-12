# Deep Learning Module
# ===================

from .bilstm_crf import BiLSTMCRF
from .framework import Framework, FrameworkType, get_framework
from .pretrained import (
    # BERT-NER (步骤 40)
    BERTNER,
    # BERT-POS (步骤 41)
    BERTPOS,
    CLASSIFICATION_LABELS,
    NER_ENTITY_TYPES,
    NER_LABELS,
    POS_LABEL_NAMES,
    POS_LABELS,
    BERTChineseSegmentor,
    # BERT-文本分类 (步骤 43)
    BERTClassifier,
    # BERT-情感分析 (步骤 42)
    BERTSentiment,
    ClassificationResult,
    FewShotLearner,
    # 步骤 45: 迁移学习框架
    FewShotLearningConfig,
    # 步骤 44: 模型微调接口
    FineTuningConfig,
    FineTuningTrainer,
    # 步骤 49: 模型热加载
    HotLoadConfig,
    HotModelLoader,
    # 步骤 46: 知识蒸馏
    KnowledgeDistillationConfig,
    KnowledgeDistiller,
    LightweightSegmentor,
    ModelCacheConfig,
    ModelComparator,
    ModelManager,
    ModelQuantizer,
    # 步骤 50: 模型管理系统
    ModelVersion,
    NEREntity,
    # 步骤 48: ONNX导出
    ONNXExportConfig,
    ONNXExporter,
    POSResult,
    PreTrainedBERT,
    PreTrainedModelBase,
    PreTrainedModelConfig,
    PreTrainedModelType,
    # 步骤 47: 模型量化
    QuantizationConfig,
    SentimentResult,
    create_bert_classifier,
    create_bert_ner,
    create_bert_pos,
    create_bert_segmentor,
    create_bert_sentiment,
    create_fewshot_learner,
    create_finetuning_config,
    create_hot_loader,
    create_knowledge_distiller,
    create_lightweight_segmentor,
    create_model_manager,
    create_onnx_exporter,
    create_quantizer,
    get_available_pretrained_models,
    get_lightweight_models,
)
from .pytorch_backend import PyTorchBackend
from .tensorflow_backend import TensorFlowBackend

__all__ = [
    # BERT-NER
    'BERTNER',
    # BERT-POS
    'BERTPOS',
    'CLASSIFICATION_LABELS',
    'NER_ENTITY_TYPES',
    'NER_LABELS',
    'POS_LABELS',
    'POS_LABEL_NAMES',
    'BERTChineseSegmentor',
    # BERT-文本分类
    'BERTClassifier',
    # BERT-情感分析
    'BERTSentiment',
    'BiLSTMCRF',
    'ClassificationResult',
    'FewShotLearner',
    # 步骤 45: 迁移学习框架
    'FewShotLearningConfig',
    # 步骤 44: 模型微调接口
    'FineTuningConfig',
    'FineTuningTrainer',
    'Framework',
    'FrameworkType',
    # 步骤 49: 模型热加载
    'HotLoadConfig',
    'HotModelLoader',
    # 步骤 46: 知识蒸馏
    'KnowledgeDistillationConfig',
    'KnowledgeDistiller',
    'LightweightSegmentor',
    'ModelCacheConfig',
    'ModelComparator',
    'ModelManager',
    'ModelQuantizer',
    # 步骤 50: 模型管理系统
    'ModelVersion',
    'NEREntity',
    # 步骤 48: ONNX导出
    'ONNXExportConfig',
    'ONNXExporter',
    'POSResult',
    'PreTrainedBERT',
    'PreTrainedModelBase',
    'PreTrainedModelConfig',
    'PreTrainedModelType',
    'PyTorchBackend',
    # 步骤 47: 模型量化
    'QuantizationConfig',
    'SentimentResult',
    'TensorFlowBackend',
    'create_bert_classifier',
    'create_bert_ner',
    'create_bert_pos',
    'create_bert_segmentor',
    'create_bert_sentiment',
    'create_fewshot_learner',
    'create_finetuning_config',
    'create_hot_loader',
    'create_knowledge_distiller',
    'create_lightweight_segmentor',
    'create_model_manager',
    'create_onnx_exporter',
    'create_quantizer',
    'get_available_pretrained_models',
    'get_framework',
    'get_lightweight_models'
]
