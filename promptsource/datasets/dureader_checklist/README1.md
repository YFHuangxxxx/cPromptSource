# DuReader<sub>checklist</sub> Dataset
##Files
>**train.json:** the training set that contains around 3K samples. 

>**dev.json:** the development set that contains around 1.1K samples (including 1k in-domain samples and a few checklist samples). 

>**test.json:** the test set that contains around 50K samples (including 4.5K real test samples, others are fake data).

>**evaluate.py:** the evaluation script.


##Data Format

The data is provided in JSON format as follows:

```
{
    "data": [
        {
            "paragraphs": [
                {
                    "context": "高铁和动车上是可以充电的,充电插头就在座位下边或者是前边。高铁动车上的充电插座排布与车型新旧有关。有些车座位是每排座位两个电源插座,有些新型车比如说“复兴号”是每两个座位有一个电源。祝旅途愉快!", 
                    "qas": [
                        {
                            "question": "高铁站可以充电吗", 
                            "type": "vocab_noun", 
                            "id": "ebbe3fc466f0f04177b8a64d2ee0de69", 
                            "answers": [
                                {
                                    "text": "", 
                                    "answer_start": -1
                                }
                            ], 
                            "is_impossible": true
                        }
                    ], 
                    "title": "高铁和动车上能充电吗? - 知乎"
                },
                {
                    "context": "【皋】字读音既可读gāo,又可读háo。读作gāo时,字义有三种意思,水边的高地或岸;沼泽,湖泊;姓氏。读作háo时,有号呼;呼告的意思。皋读作háo时... 全文", 
                    "qas": [
                        {
                            "question": "皋怎么读", 
                            "type": "in-domain", 
                            "id": "e3ffa587bba2478191e357cd9a56d10b", 
                            "answers": [
                                {
                                    "text": "既可读gāo,又可读háo", 
                                    "answer_start": 6
                                }
                            ], 
                            "is_impossible": false
                        }
                    ], 
                    "title": "皋怎么读 - 懂得"
                },
        }
    ]
}
```

Basically, the data format of DuReader<sub>checklist</sub> dataset is compatible with the one of SQuAD. Here, the field of **"context"** and **"title"** contain the text of the context and title in the given sample. The field of **"question"** contains the text of the question that is asked about the **"context"**. **"id"**, **"type"** are the unique id and the checklist type for each question. **"is_impossible"** marks if the qustion is answerable. The sub-field **"text"** of **"answers"** contains the text of a human annotated answer, and the sub-field **"answer_start"** denotes the start position of the human annotated answer in the origional **"context"**. 




##Submission Requirement

To submit your results and get it shown on the leaderboard, we require the participants to submit their results in JSON format, where the ID and the corresponding extracted answer for each question is a (key, value) pair. A sample is as follows:

```
{
    "d987e6d0fd06d21d7dfca9d90d6b045e": "no answer", 
    "2ac64f7ff83158c12c541d1946173d55": "no answer", 
    "81f02440131728f65a746b7cc74ba6b1": "2月14日", 
    "4b1b2b0f452096ad1f7e672bed9ae08a": "狗狗吃了葱应当立刻对它进行催吐。葱类会导致狗狗出现溶血的情况，并且很快起作用，如果没有及时催吐，狗狗后续可能会出现贫血、精神不振等非常严重的情况。", 
    "e5a43adec238c15fabdbc059ea771395": "有要求", 
    "6d192af7631de699bba5da8c8e3f8260": "no answer", 
    "5208f689000f17c667f54912fa501c6a": "可以一次取完", 
    "37aa8bac010814ea2665191b13067c73": "地瓜不是红薯", 
    "4617ab80cb6a0bf13435dc499aeabe49": "黄色", 
    "15d08c0ca35d728dacfafb061dfd572a": "正常应该是在使用乳液之前", 
    "862b2320b64825ec0715bc30dc31ad72": "可以一起食用", 
    "246dee97fd9a5d048c4b636f28bdce91": "没有必要", 
    "b24f3aa78e7c40e9dc8ef281b33cc2d9": "被活埋而死的", 
    "58b744cea6ac256703b19a633051ba79": "已满十六周岁的人犯罪，应当负刑事责任", 
    "9419d381e75ed24baa2f2ef42017afea": "可以联机", 
    "e3b579df357ec081f9d9f87f702a025c": "no answer"
}
```

