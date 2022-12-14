## 数据来源

中文医疗信息处理评测基准CBLUE---医疗搜索检索词意图分类（KUAKE-QIC）

数据来源于阿里夸克。在医学搜索中，对搜索问题的意图分类可以极大提升搜索结果的相关性，特别是医学知识具备极强的专业性，对问题意图进行分类也有助于融入医学知识来做增强搜索结果的性能。本任务数据集就是在这样的背景下产生的。

## 下载地址

https://tianchi.aliyun.com/dataset/dataDetail?dataId=95414

## 推荐任务

意图分类（Intent Classification）

## 数据集语言

中文

## 数据集字段说明

| 字段  | 描述内容 | 字段类型 |
| ----- | -------- | -------- |
| id    | 示例id   | string   |
| query | 查询问句 | string   |
| label | 类别名称 | string   |

**说明：**

在本次评测中，医学问题分为 病情诊断(diagnosis）、病因分析(cause)、治疗方案(method)、就医建议(advice)、指标解读(metric_explain)、疾病描述(disease_express)、后果表述(result)、注意事项(attention)、功效作用(effect)、医疗费用(price)、其他(other) 共11种类型，类型说明和示例如下：

- 病情诊断：已知症状，判断可能的原因， 如：
  - 最近早上起来浑身无力是怎么回事？
  - 我家宝宝快五个月了，为什么偶尔会吐清水带？
- 病因分析：已知疾病，解释疾病发生的原因。如：
  - 阴道松弛的原因是什么？
  - 鼻咽癌是如何发生的？
- 治疗方案：已知疾病/症状，给出治疗或缓解的方案（检查/手术/药物/行为）。如：
  - 腰椎间盘突出可以烤电吗
  - 感冒头疼吃什么药好
  - 宝宝感冒眼屎多又黄怎么办
  - 烫伤的疤痕要怎么去除？
- 就医建议：已知症状/疾病，给出就医建议（科室/检查）。如：
  - 糖尿病该做什么检查？
  - 肚子疼去什么科室？
- 指标解读：身高/体重/血压等检查结果的数值范围解读。如：
  - 血常规超敏C反应蛋白偏高说明什么
  - b超检查报告写的检测到盆腔积液是11mm，严重么？
- 疾病描述：疾病属性（eg：能不能治、能不能治好）、症状、表现、图片等相关表述。如：
  - 外痔疮早期症状有哪些呢？
  - 白癜风能不能治愈
- 后果表述：疾病/症状/药品/检查项/食物的危害，疾病恶化不治疗会产生的不良影响或治疗后会产生好的结果。如：
  - 缺乏钾元素会怎么样
  - 乙肝不治疗会怎么样
- 注意事项：病人要注意的事情，以及分析食物的好坏，食物对病人的影响。如：
  - 哮喘应该注意些什么
  - 孕妇能不能吃榴莲
  - 柿子不能和什么一起吃
  - 糖尿病人饮食注意什么啊？
- 功效作用：食品/药物的好处，功效/作用/副作用。如：
  - 乌鸡白凤丸的功效和作用
  - 玫瑰，柠檬，菊花可以一起泡吗？有什么功效
- 医疗费用：疾病/手术/药品/检查/的费用。如：
  - 二甲双瓜要多少钱？
- 其他：无法涵盖在前面分类里的以及低价值/无意义/非医疗、需求不明没讲明白的。如：
  - 玻尿酸丰唇能保持多久
  - 血常规五分类是查什么

## 数据集大小

因要保证数据模式的一致性，我们并没有把测试集放入系统中。

| 数据集名称 | 训练集大小 | 验证集大小 | 测试集大小 |
| ---------- | ---------- | ---------- | ---------- |
| KUAKE-QIC  | 6931       | 1955       | /          |

