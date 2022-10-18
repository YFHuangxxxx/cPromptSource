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

you need to install the repo locally:

1. Download the repo
2. Navigate to the root directory of the repo
3. Run `pip install -e .` to install the `promptsource` module

### run this app

```
streamlit run promptsource/app.py
```

### **To start🤗**

1.修改app.py中的以下路径为你所在的系统中所存放数据集根目录的地方:

```python
configs = get_dataset_confs(数据集存放路径/%s % (dataset_key))
```

例如：我的数据集全部放在路径：/data/xx/createpromptsource/promptsource/datasets下

那么就需要对应的改为：

```python
configs = get_dataset_confs('/data/xx/createpromptsource/promptsource/datasets/%s % (dataset_key))
```

2.修改util.py中的filter_datasets()的路径为你所存放数据集根目录的地方:

```
dataset_file_path = 你自己的数据集存放路径
```

### 为你自己的数据集编写模板

1.如果你想使用自己的数据集，首先需要把数据集对应的训练，测试文件处理成统一的json、csv等形式，具体可参考已经放入系统的数据集文件；

2.将处理好的数据集放入前面统一放所有数据集的路径下即可，重新启动app，就可以在创建模板的模式下，选中你自己的数据集及逆行模板的编写了。

### To Contribute to us

一旦你保存或修改了任何一个数据集中的模板，repo中templates中目录里面的相应文件就会被修改。要上传它，请遵循以下步骤：

- 将修改后的模板文件（templates下的任何文件）提交到git。
- push到你在GitHub上的fork分支。
- 在PromptSource repo上针对main打开一个pull request。

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

在linux系统下运行此项目，会经常出现con'nection error 所以如果可以 我们强烈建议您在windows系统下运行

