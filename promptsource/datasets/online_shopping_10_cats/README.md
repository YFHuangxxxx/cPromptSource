## 数据来源

各电商平台，具体不详

**原数据集：** [中文情感分析语料](https://download.csdn.net/download/weixin_38395744/10231401)、[中文情感分析语料库](https://download.csdn.net/download/u010097581/9919245)，网上搜集，具体作者、来源不详

## 下载地址

[Github](https://github.com/SophonPlus/ChineseNlpCorpus/raw/master/datasets/online_shopping_10_cats/online_shopping_10_cats.zip)

## 推荐任务

情感分析（Sentiment Alnalysis）

## 数据集语言

中文

## 数据集模式字段说明

online_shopping_10_cats.csv

| 字段     | 说明                | 类型     |
| ------ | ----------------- | ------ |
| label  | 1 表示正向评论，0 表示负向评论 | int64  |
| review | 评论内容              | string |

## 数据集大小

均为训练集。

类别：10（书籍、平板、手机、水果、洗发水、热水器、蒙牛、衣服、计算机、酒店）

数据量：60k+（正、负向评论各约 30k+）