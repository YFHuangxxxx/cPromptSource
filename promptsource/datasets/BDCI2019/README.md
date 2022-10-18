## 数据来源

2019CCF BDCI 大数据与计算智能大赛---[互联网新闻情感分析](https://www.datafountain.cn/competitions/350)

赛题目标为在庞大的数据集中精准的区分文本的情感极性，情感分为正中负三类。面对浩如烟海的新闻信息，精确识别蕴藏在其中的情感倾向，对舆情有效监控、预警及疏导，对舆情生态系统的良性发展有着重要的意义。

数据来源于互联网线上数据，数据爬取网站包括新闻网、微信、博客、贴吧等，模型需要对新闻数据进行情感极性分类，其中正面情绪对应0，中性情绪对应1以及负面情绪对应2。

## 下载地址

https://www.datafountain.cn/competitions/350/datasets

## 推荐任务

情感分析（Sentiment Alnalysis）

## 数据集语言

中文

## 数据集模式字段说明

all_train.csv

| 字段        | 说明                             | 类型     |
| --------- | ------------------------------ | ------ |
| unnamed:0 |                                |        |
| id        | 新闻ID News ID                   | string |
| title     | 标题内容 Title content             | string |
| content   | 新闻正文内容 Content of news text    | string |
| label     | 新闻情感标签 Emotional label in news | string |

## 数据集大小

训练集：14k+
