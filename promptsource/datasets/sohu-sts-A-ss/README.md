## 数据来源

[2021搜狐校园文本匹配大赛算法](https://www.biendata.xyz/competition/sohu_2021)

此任务为短短匹配A类，需要正确判断短文本和短文本是否匹配，且此数据集为A文件中的任务，标准较为宽泛，两段文字是同一个话题便视为匹配。

## 下载地址

https://www.biendata.xyz/competition/sohu_2021/data/

## 推荐任务

文本相似度（Sentence Similarity）/ 转述识别（paraphrase identification）

## 数据集语言

中文

## 数据集字段说明

| 字段     | 描述内容                | 字段类型   |
| ------ | ------------------- | ------ |
| source | 短文本1                | string |
| target | 长文本2                | string |
| labelA | 表示是否匹配，0表示不匹配，1表示匹配 | int64  |

## 数据集大小

因要保证数据模式的一致性，我们并没有把测试集放入系统中。

| 数据集名称         | 训练集大小 | 开发集大小 |
| ------------- | ----- | ----- |
| sohu-sts-A-ss | 9866  | 1644  |

