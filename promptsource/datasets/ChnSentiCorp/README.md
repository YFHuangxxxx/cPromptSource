## 数据来源

[携程网](http://www.ctrip.com/)

**原数据集：** ChnSentiCorp_htl，由 [谭松波](http://people.ucas.ac.cn/~0012244) 老师整理的一份数据集

## 下载地址

[Github](https://github.com/SophonPlus/ChineseNlpCorpus/raw/master/datasets/ChnSentiCorp_htl_all/ChnSentiCorp_htl_all.csv)

## 推荐任务

情感分析（Sentiment Alnalysis）

## 数据集语言

中文

## 数据集模式字段说明

ChnSentiCorp_htl_all.csv

| 字段     | 说明                | 类型     |
| ------ | ----------------- | ------ |
| label  | 1 表示正向评论，0 表示负向评论 | int64  |
| review | 评论内容              | string |

## 数据集大小

均为验证集。

数据量：7k+（5k+正向评论，2k+负向评论）