## 数据来源

##### 千言数据集---**ChineseBiomedicalQA**集

ChineseBiomedicalQA旨在利用执业药师和医师的真题或者模拟题来衡量模型的推理能力，评测模型的可解释性以及泛化能力，是首个基于推理的中文医疗问答数据集。

## 下载地址

https://www.luge.ai/#/luge/dataDetail?id=40

## 推荐任务

Multiple-Choice QA（多项选择问答）

## 数据集语言

中文

## 数据集字段说明

| 字段           | 描述内容     | 字段类型 |
| -------------- | ------------ | -------- |
| questionType   | 选择题类型   | string   |
| questionId     | 问题标识符id | string   |
| questionText   | 问题题干     | string   |
| option         | 选项（5个）  | string   |
| year           | 题目提出时间 | string   |
| answer         | 正确答案     | string   |
| subject        | 题目领域分类 | string   |
| backgroundText | 背景         | string   |

## 数据集大小

| 数据集名称              | 训练集大小 | 验证集大小 | 测试集大小 |
| ----------------------- | ---------- | ---------- | ---------- |
| **ChineseBiomedicalQA** | 87786      | 1260       | /          |

