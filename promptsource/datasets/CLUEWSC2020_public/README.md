## 数据来源

CLUE benchmark---CLUEWSC2020: WSC Winograd模式挑战中文版，新版2020-03-25发布

[git项目地址](https://github.com/CLUEbenchmark/CLUEWSC2020)

数据来源：数据有CLUE benchmark提供，从中国现当代作家文学作品中抽取，再经语言专家人工挑选、标注。

## 下载地址

[CLUEWSC2020数据集下载](https://storage.googleapis.com/cluebenchmark/tasks/cluewsc2020_public.zip)

## 推荐任务

Winograd Scheme Challenge（WSC）是一类代词消歧的任务。

即判断句子中的代词指代的是哪个名词。题目以真假判别的方式出现，如：

句子：这时候放在床上枕头旁边的手机响了，我感到奇怪，因为欠费已被停机两个月，现在它突然响了。需要判断“它”指代的是“床”、“枕头”，还是“手机”？

## 数据集语言

中文

## 数据集字段说明

| 字段        | 描述内容                                                     | 字段类型 |
| ----------- | ------------------------------------------------------------ | -------- |
| target      | 分类ID                                                       | int64    |
| span2_index | 包含于target中，指代词下标开始的位置                         | int64    |
| span1_index | 包含于target中，所要判断的名词下标开始的位置                 | string   |
| span1_text  | 包含于target中，所要判断的名词                               | string   |
| span2_text  | 包含于target中，指代词                                       | string   |
| idx         | 示例唯一标识符                                               | string   |
| label       | 表示指代的是否正确，"true"表示代词确实是指代span1_text中的名词的，"false"代表不是。 | string   |
| text        | 段落文本                                                     | string   |

## 数据集大小

| 数据集名称         | 训练集大小 | 验证集大小 | 测试集大小 |
| ------------------ | ---------- | ---------- | ---------- |
| cluewsc2020_public | 1244       | 304        | /          |

