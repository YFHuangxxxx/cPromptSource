## 数据来源

某外卖平台收集的用户评价。

原数据集： [中文短文本情感分析语料 外卖评价](https://download.csdn.net/download/cstkl/10236683)，网上搜集，具体作者、来源不详

进行了以下加工处理：

1. 将原来 2 个文件整合到 1 个文件中
2. 去重

## 下载地址

[Github](https://github.com/SophonPlus/ChineseNlpCorpus/raw/master/datasets/waimai_10k/waimai_10k.csv)

## 推荐任务

情感分析（Sentiment Alnalysis）

## 数据集语言

中文

## 数据集模式字段说明

waimai_10k.csv

| 字段     | 说明                | 类型     |
| ------ | ----------------- | ------ |
| label  | 1 表示正向评论，0 表示负向评论 | int64  |
| review | 评论内容              | string |

## 数据集大小

训练集：正向 4000 条，负向约 8000 条