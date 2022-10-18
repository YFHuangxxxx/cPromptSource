## 数据来源

千言数据集---**DuReader_QG问题生成数据集**

DuReader robust旨在利用真实应用中的数据样本来衡量阅读理解模型的鲁棒性，评测模型的过敏感性、过稳定性以及泛化能力，是首个中文阅读理解鲁棒性数据集。
DuReader_QG是从DuReader robust中选择的问题生成任务子集

## 下载地址

https://www.luge.ai/#/luge/dataDetail?id=8

## 推荐任务

Extractive-QA

任务描述：给定段落p和答案a，生成自然语言表述的问题q，且该问题符合段落和上下文的限制；
数据规模：训练集约14.5k，开发集约1k，测试集约1k；

## 数据集语言

中文

## 数据集说明

| 字段     | 描述内容 | 字段类型 |
| -------- | -------- | -------- |
| id       | 标识id   | int64    |
| context  | 文本     | string   |
| question | 问题     | string   |
| answer   | 回答     | string   |

## 数据集大小

| 数据集名称  | 训练集大小 | 验证集大小 | 测试集大小 |
| ----------- | ---------- | ---------- | ---------- |
| DuReader_QG | 14520      | 984        | /          |
