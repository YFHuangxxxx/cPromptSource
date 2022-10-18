## 数据来源

台達閱讀理解資料集 Delta Reading Comprehension Dataset (DRCD) 屬於通用領域繁體中文機器閱讀理解資料集。 本資料集期望成為適用於遷移學習之標準中文閱讀理解資料集。 本資料集從2,108篇維基條目中整理出10,014篇段落，並從段落中標註出30,000多個問題

關於資料集之更詳細資訊請洽詢論文： For more information please refer to Paper https://arxiv.org/abs/1806.00920

## 下载地址

https://github.com/DRCKnowledgeTeam/DRCD

## 推荐任务

Extractive-QA

## 数据集语言

中文

## 数据集字段说明

- version : 資料集版本
- data :
  - title : : 文章標題
  - id : : 文章編號
  - paragraphs :
    - id : : 文章編號_段落編號
    - context : : 段落內容
    - qas :
      - question : : 問題內容
      - id : : 文章編號_段落編號_問題編號
      - answers :
        - answer_start : text在文中位置
        - id : : "1"表示為人工標註的答案，"2"以上為人工答題的答案
        - text : : 答案內容

## 数据集大小

| 数据集名称 | 训练集大小 | 验证集大小 | 测试集大小 |
| ---------- | ---------- | ---------- | ---------- |
| DRCD       | 1960       | 383        | 383        |

