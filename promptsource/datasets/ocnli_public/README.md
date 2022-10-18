## 数据来源

paper:https://arxiv.org/abs/2010.05444

##### CLUE benchmark---[OCNLI 中文原版自然语言推理](https://github.com/cluebenchmark/OCNLI) Original Chinese Natural Language Inference

OCNLI，即原生中文自然语言推理数据集，是第一个非翻译的、使用原生汉语的大型中文自然语言推理数据集。

## 下载地址

https://storage.googleapis.com/cluebenchmark/tasks/ocnli_public.zip

## 推荐任务

文本相似度（Sentence Similarity）/ 转述识别（paraphrase identification）

## 数据集语言

中文

## 数据集字段说明

| 字段               | 描述内容                                                     | 字段类型 |
| ------------------ | ------------------------------------------------------------ | -------- |
| level              | 【难度】: `easy`, `medium`, `hard`分别代表标注人员为某一标签（如entailment）写的第一、第二、第三个假设。我们预计三者难度递增。具体数据收集方式请参考论文。 | string   |
| sentence1          | 【句子1】，即前提。                                          | string   |
| sentence2          | 【句子2】，即假设。                                          | string   |
| label              | 【标签】，即标签0 -- 标签4的majority vote。如果标签为'-'，则此数据应除去，因为5名标注人员没有得出共识，此项设置与SNLI/MNLI相同。 | string   |
| label0` -- `label4 | 【5个标签】，验证集与测试集的数据均有5个标签。训练集仅部分数据有5个标签。 | string   |
| genre              | 【文本类别】，共5类：政府公报、新闻、文学、电视谈话节目、电话转写。 | string   |
| prem_id            | 【前提编号】                                                 | string   |
| id                 | 【总编号】                                                   | string   |

## 数据集大小

| 数据集名称   | 训练集大小 | 验证集大小 | 测试集大小 |
| ------------ | ---------- | ---------- | ---------- |
| ocnli_public | 50486      | 3000       | /          |

