## 数据来源

千言数据集---**Dureader checklist 阅读理解细粒度评估数据集**

Dureader checklist建立了细粒度的、多维度的评测手段，从词汇理解、短语理解、语义角色理解、逻辑推理等多个维度检测模型的不足之处，从而推动阅读理解评测进入“精细化“时代。该数据集中的样本均来自于实际的应用场景，难度大，考察点丰富，覆盖了真实应用中诸多难以解决的问题。

## 下载地址

https://www.luge.ai/#/luge/dataDetail?id=3

## 推荐任务

Extractive-QA

## 数据集语言

中文

## 数据集说明

关于该数据集的详细介绍，可参考该网站
[https://github.com/PaddlePaddle/Research/tree/master/NLP/DuReader-Checklist-BASELINE](https://github.com/baidu/DuReader/tree/master/DuReader-Checklist)

| 字段         | 描述内容                                     | 字段类型 |
| ------------ | -------------------------------------------- | -------- |
| id           | 文本标识id                                   | string   |
| context      | 文本内容                                     | string   |
| question     | 问题                                         | string   |
| answers      | 回答标志                                     | schema   |
| answer_start | 表示人类注释的答案在原始 "背景 "中的起始位置 | int64    |
| text         | 答案文本                                     | string   |

## 数据集大小

| 数据集名称         | 训练集大小 | 验证集大小 | 测试集大小 |
| ------------------ | ---------- | ---------- | ---------- |
| Dureader checklist | 3000       | 1130       | /          |

