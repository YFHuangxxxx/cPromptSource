## 数据来源

##### AFQMC 蚂蚁金融语义相似度 Ant Financial Question Matching Corpus

来源于[CLUE benchmark](https://github.com/CLUEbenchmark/CLUE) 

## 下载地址

https://storage.googleapis.com/cluebenchmark/tasks/afqmc_public.zip

## 推荐任务

文本相似度（Sentence Similarity）/ 转述识别（paraphrase identification）

## 数据集语言

中文

## 数据集字段说明

| 字段        | 描述内容                | 字段类型   |
| --------- | ------------------- | ------ |
| sentence1 | 句子1                 | string |
| sentence2 | 句子2                 | string |
| label     | 表示是否相似，0表示不相似，1表示相似 | int64  |

## 数据集大小

因要保证数据模式的一致性，我们并没有把测试集放入系统中。

| 数据集名称     | 训练集大小 | 验证集大小 | 测试集大小 |
| --------- | ----- | ----- | ----- |
| AFQMC(中文) | 34334 | 4316  | 3861  |

