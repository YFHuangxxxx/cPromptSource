## 数据来源

huggingface数据集

- **Homepage:** https://jiangjiechen.github.io/publication/ekar/
- **Repository:** https://github.com/jiangjiechen/E-KAR
- **Paper:** [E-KAR: A Benchmark for Rationalizing Natural Language Analogical Reasoning](https://arxiv.org/abs/2203.08480)
- **Leaderboard:** https://ekar-leaderboard.github.io
- **Point of Contact:** jjchen19@fudan.edu.cn

本着能够推理的模型应该有正确的理由的信念，数据集的作者提出了一个首创的可解释知识密集型类比推理基准（E-KAR）。基准由1,655个（中文）和1,251个（英文）来自公务员考试的问题组成，这些问题需要密集的背景知识来解决。更重要的是，我们设计了一个自由文本解释方案来解释是否应该进行类比，并为每一个问题和候选答案进行人工注释。经验结果表明，这个基准对一些最先进的解释生成和类比问题回答任务的模型来说是非常具有挑战性的，这就需要在这个领域进行进一步的研究。

### 下载地址

https://huggingface.co/datasets/Jiangjie/ekar_chinese

### 推荐任务

- analogical-QA。该数据集可用于训练类比推理的模型，其形式为multiple-choice QA。
- 解释生成。该数据集可用于生成自由文本解释，使类比推理合理化。

这个数据集支持两种任务模式。EASY模式和HARD模式。

- 简单模式：查询解释可以作为输入的一部分。
- 困难模式：不允许解释作为输入的一部分。

### 语言

此数据集采用的是中文版本，[English version](https://huggingface.co/datasets/Jiangjie/ekar_english).

### 数据集实例

```json
{
  "id": "982f17-en",
  "question": "plant:coal",
  "choices": {
    "label": [
      "A",
      "B",
      "C",
      "D"
    ],
    "text": [
      "white wine:aged vinegar",
      "starch:corn",
      "milk:yogurt",
      "pickled cabbage:cabbage"
    ]
  },
  "answerKey": "C",
  "explanation": [
    "\"plant\" is the raw material of \"coal\".",
    "both \"white wine\" and \"aged vinegar\" are brewed.",
    "\"starch\" is made of \"corn\", and the order of words is inconsistent with the query.",
    "\"yogurt\" is made from \"milk\".",
    "\"pickled cabbage\" is made of \"cabbage\", and the word order is inconsistent with the query."
  ],
  "relation": [
    [["plant", "coal", "R3.7"]],
    [["white wine", "aged vinegar", "R2.4"]],
    [["corn", "starch", "R3.7"]],
    [["milk", "yogurt", "R3.7"]],
    [["cabbage", "pickled cabbage", "R3.7"]]
  ]
}
```

### 数据集字段说明

| 字段        | 描述内容                                               | 字段类型 |
| ----------- | ------------------------------------------------------ | -------- |
| id          | 每个例子的字符串标识符                                 | string   |
| question    | 查询条件                                               | string   |
| choices     | 候选答案术语                                           | string   |
| answerKey   | 正确答案                                               | string   |
| explanation | 对查询（第一）和候选答案（第二-第五）的解释            | string   |
| relation    | 查询（第一）和候选答案（第二至第五）中的术语的注释关系 | string   |

### 数据集大小

| 数据集名称 |训练集大小|验证集大小|测试集大小|
|:-----:|:---:|:--------:|:--:|
|ekar_chinese| 1155 | 165 | 335 |
