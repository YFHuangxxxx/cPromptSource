## 数据来源

科技战疫 大数据公益挑战赛之算法赛道---[疫情期间网民情绪识别](https://www.datafountain.cn/competitions/423)

数据集依据与“新冠肺炎”相关的230个主题关键词进行数据采集，抓取了2020年1月1日—2020年2月20日期间共计100万条微博数据，并对其中10万条数据进行人工标注，标注分为三类，分别为：1（积极），0（中性）和 -1（消极）。

后期加工处理：将原本的100k+的数据处理成了70k+，以免溢出报错

## 下载地址

https://www.datafountain.cn/competitions/423/datasets

## 推荐任务

情感分析（Sentiment Alnalysis）

## 数据集语言

中文

## 数据集模式字段说明

nCoV_100k.labled.csv

| 字段        | 说明     | 类型     |
| --------- | ------ | ------ |
| acount    | 发布人账号  | string |
| content   | 微博中文内容 | string |
| id        | 微博id   | string |
| picture   | 微博图片   | string |
| reference | 情感倾向   | int64  |
| time      | 微博发布时间 | string |
| vedio     | 微博视频   | string |

## 数据集大小

均为训练集。

数据量：70k+
