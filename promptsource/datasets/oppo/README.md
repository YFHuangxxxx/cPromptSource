## 数据来源

千言数据集---OPPO小布对话文本语义匹配数据集

采样自智能对话场数据，通过对闲聊、智能客服、影音娱乐、信息查询等多领域真实用户交互语料进行用户信息脱敏、相似度筛选处理得到，数据集主要特点是文本较短、非常口语化、存在文本高度相似而语义不同的难例。该数据集所有标签都有经过人工精标确认。

## 下载地址

https://www.luge.ai/#/luge/dataDetail?id=28

## 推荐任务

文本相似度（Sentence Similarity）/ 转述识别（paraphrase identification）

## 数据集语言

中文

## 数据集字段说明

| 字段    | 描述内容                | 字段类型    |
| ----- | ------------------- | ------- |
| q1    | 句子1                 | string  |
| q2    | 句子2                 | string  |
| label | 表示是否匹配，0表示不匹配，1表示匹配 | float64 |

## 数据集大小

因要保证数据模式的一致性，我们并没有把测试集放入系统中。

| 数据集名称 | 训练集大小 | 开发集大小 | 测试集大小 |
| ----- | ----- | ----- | ----- |
| oppo  | 60002 | 10000 |       |

