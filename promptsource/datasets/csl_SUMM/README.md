## 数据来源

[CLGE中文生成任务基准测评---CSL 中长文本摘要生成](https://github.com/CLUEbenchmark/CLGE#1-csl-%E4%B8%AD%E9%95%BF%E6%96%87%E6%9C%AC%E6%91%98%E8%A6%81%E7%94%9F%E6%88%90)

数据来源于[中文科学文献数据(CSL)](https://github.com/P01son6415/chinese-scientific-literature-dataset)，选取 10k 条计算机相关领域论文及其标题作为训练集。

## 下载地址

[百度网盘](https://pan.baidu.com/s/1FFG_s8z47r6e7EqoRtfIrw) 提取码: u6mc

## 推荐任务

文本摘要（Summarization）

## 数据集语言

中文

## 数据集字段说明

| 字段  | 描述内容 | 字段类型 |
| ----- | -------- | -------- |
| id    | 文本id   | int64    |
| title | 标题     | string   |
| abst  | 摘要     | string   |

## 数据集大小

包括训练集和验证集。

| 数据集名称 | 训练集大小 | 验证集大小 | 测试集大小 |
| ---------- | ---------- | ---------- | ---------- |
| CSL_SUMM   | 3000       | 500        | /          |

