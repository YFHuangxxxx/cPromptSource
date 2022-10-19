# Create prompt for Chinese

### Setup

Requirments

```
"streamlit==0.84.0",
"python==3.7",
"black<=21.12b0",
"datasets>=1.7.0",
"flake8",
"isort==5.8.0",
"pytest",
"pyyaml>=5",
"jinja2",
"plotly",
"requests",
"pandas",
"py7zr",
```

1. 准备环境：`conda create -n cpromptsource(可换成你自己环境的名字) python=3.7`
2. 激活环境：conda activate cpromptsource
3. git clone此项目到你的本地/或者download此项目到本地
4. 数据集准备：有部分数据集过大的数据集，我们将其下载链接放在了[百度网盘](https://pan.baidu.com/s/1a9Fj5u-yZ4pJVFvcdAcjWg?pwd=gnns)中，可将其下载到目录cPromptSource/promptsource/datasets下
5. cd到该项目的根目录下
6. Run `pip install -e .` to install the `promptsource` module

### run this app

```
streamlit run promptsource/app.py
```

### **To start🤗**

注意在编辑以下代码时请以utf-8的encoding编码方式打开：

1.修改promptsource/app.py中的以下路径为所在的系统中所存放数据集根目录的地方:

```python
configs = get_dataset_confs(数据集存放路径/%s % (dataset_key))
...
try:
   if subset_name is None:
      dataset = datasets.load_dataset("数据集存放路径/%s" % (dataset_key))
   else:
      dataset = datasets.load_dataset("数据集存放路径/%s/%s" % (dataset_key, subset_name), subset_name)
```

例如：如果您已经下载了我们的项目并要查看我们项目中的数据集，那么数据集存放路径应为：项目根目录/cPromptSource/promptsource/datasets下

比如：对应的改为：

```python
configs = get_dataset_confs('/data/xx/cPromptSource/promptsource/datasets/%s % (dataset_key))
...
try:
   if subset_name is None:
      dataset = datasets.load_dataset("/data/xx/cPromptSource/promptsource/datasets/%s" % (dataset_key))
   else:
      dataset = datasets.load_dataset("/data/xx/cPromptSource/promptsource/datasets/%s/%s" % (dataset_key, subset_name), subset_name)
```

2.修改promptsource/util.py中的filter_datasets()的路径与前面相同，同样为你所存放数据集目录的地方:

```
dataset_file_path = 数据集存放路径
```

### 为你自己的数据集编写模板

1.如果你想使用自己的数据集，首先需要把数据集对应的训练，测试文件处理成统一的json、csv等形式，具体可参考已经放入系统的数据集文件；

2.将前面一步中promptsource/app.py和promptsource/util.py中的对应路径统一改为你所存放的自己的数据集的路径即可，重新启动app，就可以在创建模板的模式下，选中你自己的数据集及进行模板的编写了。

### To Contribute to us

一旦你保存或修改了任何一个数据集中的模板，repo中templates中目录里面的相应文件就会被修改。要上传它，请遵循以下步骤：

- 将修改后的模板文件（templates下的任何文件）提交到git。
- push到你在GitHub上的fork分支。
- 在cPromptSource repo上针对main打开一个pull request。

### 如何获取使用添加了模板的数据集

```python
dataset_id = "ekar_Chinese"

from datasets import load_dataset
dataset = load_dataset(dataset_id)
example = dataset["train"][0]

# Prompt it
from templates import DatasetTemplates
# Get all prompts
dataset_template = DatasetTemplates(dataset_id)

# Select a prompt by name
prompt = dataset_template["test"]
# Apply the prompt on the example 
result = prompt.apply(example)
print("INPUT: ", result[0])
print("TARGET: ", result[1])
```

**Creating a dataset from the base dataset with all prompts**

```python
from datasets import concatenate_datasets, Dataset, Value

# merge existing splits into big dataset
complete_ds = concatenate_datasets([dataset["train"], dataset["test"]])

# create empty dataset for adding prompts
prompted_ds = Dataset.from_dict({"inputs": [], "targets": []})
prompted_ds.features["inputs"] = Value("string")
prompted_ds.features["targets"] = Value("string")
for prompt in list(dataset_template.name_to_id_mapping.keys()):
    
    def prompt_split(examples):
        prompted_examples = dataset_template[prompt].apply(examples)
        return {"inputs": prompted_examples[0], "targets": prompted_examples[1]}
    # apply the prompt on the complete dataset
    print(f"dataset size before adding new samples: {len(prompted_ds)}")
    prompted_split = complete_ds.map(prompt_split, remove_columns=complete_ds.column_names)
    prompted_ds = concatenate_datasets([prompted_ds, prompted_split])
    print(f"dataset size after adding new samples: {len(prompted_ds)}")
    print(f"latest dataset sample: {prompted_ds[-1]}")    
```

**Push dataset to hub**

Log into HF hub using `notebook_login` or `huggingface-cli login`

```
from huggingface_hub import HfApi,HfFolder

api = HfApi()

user = api.whoami(HfFolder.get_token())
```

```python
dataset_repo_id = f"{user['name']}/ekar_Chinese"

prompted_ds.push_to_hub(dataset_repo_id)

print(f"https://huggingface.co/datasets/{dataset_repo_id}")
```

### 注意

在linux系统下以及windows系统下均可运行，只不过需要修改的路径不同而已。

