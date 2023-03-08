import argparse
import textwrap
from multiprocessing import Manager, Pool

import pandas as pd
import plotly.express as px
import streamlit as st
import datasets
from datasets import get_dataset_infos
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import DjangoLexer
from templates import INCLUDED_USERS
import pkg_resources

from session import _get_state
from templates import DatasetTemplates, Template, TemplateCollection
from util import (
    get_dataset,
    get_dataset_confs,
    list_datasets,
    removeHyphen,
    renameDatasetColumn,
    render_features,
)
import os
DATASET_FOLDER_PATH = pkg_resources.resource_filename(__name__, "datasets")
# add an argument for read-only
parser = argparse.ArgumentParser(description="run app.py with args")
parser.add_argument("-r", "--read-only", action="store_true", help="whether to run it as read-only mode")

args = parser.parse_args()
if args.read_only:
    select_options = ["首页", "数据集预览"]
    side_bar_title_prefix = "Promptsource (Read only)"
else:
    select_options = ["首页", "数据集预览", "创建模板"]
    side_bar_title_prefix = "Promptsource"

#
# Cache functions
#
get_dataset = st.cache(allow_output_mutation=True)(get_dataset)
get_dataset_confs = st.cache(get_dataset_confs)
list_datasets = st.cache(list_datasets)


def reset_template_state():
    state.template_name = None
    state.jinja = None
    state.reference = None


#
# Loads session state
#
state = _get_state()

#
# Initial page setup
#
st.set_page_config(page_title="cPromptsource", layout="wide")
st.sidebar.markdown(
    "<center>Promptsource\n\n</a></center>",
    unsafe_allow_html=True,
)
mode = st.sidebar.selectbox(
    label="选择一个模式",
    options=select_options,
    index=0,
    key="mode_select",
)
st.sidebar.title(f"{side_bar_title_prefix} 🐾 - {mode}")

#
# Adds pygments styles to the page.
#
st.markdown(
    "<style>" + HtmlFormatter(style="friendly").get_style_defs(".highlight") + "</style>", unsafe_allow_html=True
)

WIDTH = 140


def show_jinja(t, width=WIDTH):
    def replace_linebreaks(t):
        """
        st.write does not handle double breaklines very well. When it encounters `\n\n`, it exit the curent <div> block.
        Explicitely replacing all `\n` with their html equivalent to bypass this issue.
        Also stripping the trailing `\n` first.
        """
        return t.strip("\n").replace("\n", "<br/>")

    wrap = textwrap.fill(t, width=width, replace_whitespace=False)
    out = highlight(wrap, DjangoLexer(), HtmlFormatter())
    out = replace_linebreaks(out)
    st.write(out, unsafe_allow_html=True)


def show_text(t, width=WIDTH, with_markdown=False):
    wrap = [textwrap.fill(subt, width=width, replace_whitespace=False) for subt in t.split("\n")]
    wrap = "\n".join(wrap)
    if with_markdown:
        st.write(wrap, unsafe_allow_html=True)
    else:
        st.text(wrap)


if mode == "首页":
    st.title("cPromptSource")
    st.write(':wink:')
    st.write(
        "如果你想对我们的数据集做出贡献，请跳转到："
        + "[github](https://github.com/Phoebe731178/createprompt_test/README.md)."
    )
    st.write(
        "如果你想为你自己的数据集创建模板，请跳转到："
        + "[github](https://github.com/Phoebe731178/createprompt_test/README.md)."
    )

    try:
        template_collection = TemplateCollection()
    except FileNotFoundError:
        st.error(
            "无法找到Prompt文件夹!\n\n"
            "我们希望该文件夹在工作目录中。"
            "你可能需要在 repo 的根目录下重新启动应用程序。"
        )
        st.stop()

    #
    # Global metrics
    #
    counts = template_collection.get_templates_count()
    nb_prompted_datasets = len(counts)
    st.write(f"## *编写了模板的数据集*的数量: `{nb_prompted_datasets}`")
    nb_prompts = sum(counts.values())
    st.write(f"## *模板*的数量: `{nb_prompts}`")



else:
    assert mode in ["数据集预览", "创建模板"], ValueError(
        f"`mode` ({mode}) 应该在 `[首页, 数据集预览, 创建模板]`"
    )

    #
    # Loads dataset information
    #

    dataset_list = list_datasets()
    example_index = dataset_list.index("AFQMC-public")

    #
    # Select a dataset
    #
    dataset_key = st.sidebar.selectbox(
        "数据集",
        dataset_list,
        key="dataset_select",
        index=example_index,
        help="选择要处理的数据集。",
    )

    #
    # If a particular dataset is selected, loads dataset and template information
    #
    if dataset_key is not None:

        #
        # Check for subconfigurations (i.e. subsets)
        #
        #configs = get_dataset_confs(os.listdir(os.path.join(DATASET_FOLDER_PATH, dataset_key)))
        #configs = get_dataset_confs("../datasets/%s" % (dataset_key))
        #print(configs)
        #conf_option = None
        #if len(configs) > 0:
            #conf_option = st.sidebar.selectbox("子集", configs, index=0, format_func=lambda a: a.name)

        #subset_name = str(conf_option.name) if conf_option else None
        #print(subset_name)
        dataset = datasets.load_dataset(os.listdir(os.path.join(DATASET_FOLDER_PATH, dataset_key)))
        #try:
            #if subset_name is None:
                #dataset = datasets.load_dataset(os.listdir(os.path.join(DATASET_FOLDER_PATH, dataset_key)))
                #dataset = datasets.load_dataset("../datasets/%s" % (dataset_key))
            #else:
                #dataset = datasets.load_dataset("../datasets/%s/%s" % (dataset_key, subset_name), subset_name)
        ##except OSError as e:
            #st.error(
                #f"您自己的数据集需要手动放置"
                #f"这适用于  {dataset_key}{f'/{subset_name}' if subset_name is not None else ''}. "
                #f"\n\n请将原始数据集放到 `数据集存放根目录/{dataset_key}{f'/{subset_name}' if subset_name is not None else ''}`. "
            #)
            #st.stop()

        splits = list(dataset.keys())
        index = 0
        if "train" in splits:
            index = splits.index("train")
        split = st.sidebar.selectbox("Split", splits, key="split_select", index=index)
        dataset = dataset[split]
        dataset = renameDatasetColumn(dataset)

        #
        # Loads template data
        #
        try:
            dataset_templates = DatasetTemplates(dataset_key, conf_option.name if conf_option else None)
        except FileNotFoundError:
            st.error(
                "无法找到提示文件夹!\n\n"
                "我们希望该文件夹在工作目录中。"
                "你可能需要在 repo 的根目录下重新启动应用程序。"
            )
            st.stop()

        template_list = dataset_templates.all_template_names
        num_templates = len(template_list)
        st.sidebar.write(
            "创建的提示数量为 "
            + f"`{dataset_key + (('/' + conf_option.name) if conf_option else '')}`"
            + f": **{str(num_templates)}**"
        )

        if mode == "数据集预览":
            if num_templates > 0:
                template_name = st.sidebar.selectbox(
                    "模板名称",
                    template_list,
                    key="template_select",
                    index=0,
                    help="选择要可视化的提示。",
                )

            step = 50
            example_index = st.sidebar.number_input(
                f"选择实例索引 (Size = {len(dataset)})",
                min_value=0,
                max_value=len(dataset) - step,
                value=0,
                step=step,
                key="example_index_number_input",
                help="Offset = 50.",
            )
        else:  # mode = Sourcing
            st.sidebar.subheader("选择实例")
            print(len(dataset))
            example_index = st.sidebar.slider("选择实例索引", 0, len(dataset) - 1)

            example = dataset[example_index]
            example = removeHyphen(example)

            st.sidebar.write(example)

        st.sidebar.subheader("数据集模式")
        rendered_features = render_features(dataset.features)
        st.sidebar.write(rendered_features)

        #
        # Display dataset information
        #
        st.header("数据集: " + dataset_key + " " + (("/ " + conf_option.name) if conf_option else ""))

        # If we have a custom dataset change the source link to the hub
        split_dataset_key = dataset_key.split("/")
        possible_user = split_dataset_key[0]

        #
        # Body of the app: display prompted examples in mode `Prompted dataset viewer`
        # or text boxes to create new prompts in mode `Sourcing`
        #
        if mode == "数据集预览":
            def read_markdown_file(markdown_file):
                with open(markdown_file, encoding='utf-8') as fp:
                    w = fp.read()
                return w
            #
            # Display template information
            #
            if num_templates > 0:
                template = dataset_templates[template_name]
                st.markdown("## 模板")
                #st.subheader("##Prompt")
                st.markdown("### 名称")
                st.text(template.name)
                st.markdown("### 参考")
                st.text(template.reference)
                st.markdown("### 是否执行为原数据集设计的原始任务？ ")
                st.text(template.metadata.original_task)
                st.markdown("### 提示中是否会明确列出输出模板中的选择？ ")
                st.text(template.metadata.choices_in_prompt)
                st.markdown("### 指标")
                st.text(", ".join(template.metadata.metrics) if template.metadata.metrics else None)
                st.markdown("### 答案选择")
                if template.get_answer_choices_expr() is not None:
                    show_jinja(template.get_answer_choices_expr())
                else:
                    st.text(None)
                st.markdown("### Jinja模板")
                splitted_template = template.jinja.split("|||")
                st.markdown("#### 输入模板")
                show_jinja(splitted_template[0].strip())
                if len(splitted_template) > 1:
                    st.markdown("#### 目标模板")
                    show_jinja(splitted_template[1].strip())
                st.markdown("***")

            #
            # Display a couple (steps) examples
            #
            for ex_idx in range(example_index, example_index + step):
                if ex_idx >= len(dataset):
                    continue
                example = dataset[ex_idx]
                example = removeHyphen(example)
                col1, _, col2 = st.beta_columns([12, 1, 12])
                with col1:
                    st.write(example)
                if num_templates > 0:
                    with col2:
                        prompt = template.apply(example, highlight_variables=False)
                        if prompt == [""]:
                            st.write("∅∅∅ *空白的结果*")
                        else:
                            st.write("输入")
                            show_text(prompt[0])
                            if len(prompt) > 1:
                                st.write("目标")
                                show_text(prompt[1])
                st.markdown("***")
        else:  # mode = Sourcing
            st.markdown("## 创建提示")

            #
            # Create a new template or select an existing one
            #
            col1a, col1b, _, col2 = st.beta_columns([9, 9, 1, 6])

            # current_templates_key and state.templates_key are keys for the templates object
            current_templates_key = (dataset_key, conf_option.name if conf_option else None)

            # Resets state if there has been a change in templates_key
            if state.templates_key != current_templates_key:
                state.templates_key = current_templates_key
                reset_template_state()

            with col1a, st.form("new_template_form"):
                new_template_name = st.text_input(
                    "创建一个新的提示",
                    key="new_template",
                    value="",
                    help="输入名称并点击回车键，创建一个新的提示。",
                )
                new_template_submitted = st.form_submit_button("创建")
                if new_template_submitted:
                    if new_template_name in dataset_templates.all_template_names:
                        st.error(
                            f"有一个名称为 {new_template_name} 已经存在 "
                            f"为数据集 {state.templates_key}."
                        )
                    elif new_template_name == "":
                        st.error("需要提供一个提示名称。")
                    else:
                        template = Template(new_template_name, "", "")
                        dataset_templates.add_template(template)
                        reset_template_state()
                        state.template_name = new_template_name
                else:
                    state.new_template_name = None

            with col1b, st.beta_expander("或选择提示", expanded=True):
                template_list = dataset_templates.all_template_names
                if state.template_name:
                    index = template_list.index(state.template_name)
                else:
                    index = 0
                state.template_name = st.selectbox(
                    "", template_list, key="template_select", index=index, help="选择要处理的提示。"
                )

                if st.button("删除提示", key="delete_prompt"):
                    dataset_templates.remove_template(state.template_name)
                    reset_template_state()

            variety_guideline = """
            :heavy_exclamation_mark::question:我们强烈鼓励创建多样化的提示，而不只是改变表面的措辞（即略微改变2或3个词）。
            我们希望多样性的提示会对你所使用的模型的稳健性产生非同小可的影响。
            \r**为了获得各种提示，你可以尝试沿着这些轴线移动光标**:
            \n- **疑问句与肯定句的形式**: 对输入的某一属性提出问题，或告诉模型对输入的某一内容作出决定。
            \n- **任务描述定位**: 关于任务的描述在哪里与输入相混合？在开始，在中间，在最后？
            \n- **间接提问或进行背景介绍**: 比如说，*鉴于这个评论，你会购买这个产品吗？* 是一种间接的方式来询问评论所包含的情感是否积极。
            """

            col1, _, _ = st.beta_columns([18, 1, 6])
            with col1:
                if state.template_name is not None:
                    show_text(variety_guideline, with_markdown=True)

            #
            # Edit the created or selected template
            #
            col1, _, col2 = st.beta_columns([18, 1, 6])
            with col1:
                if state.template_name is not None:
                    template = dataset_templates[state.template_name]
                    #
                    # If template is selected, displays template editor
                    #
                    with st.form("edit_template_form"):
                        updated_template_name = st.text_input("名称", value=template.name)
                        state.reference = st.text_input(
                            "提示性参考",
                            help="对提示的简短描述和/或提示的论文参考。",
                            value=template.reference,
                        )

                        # Metadata
                        state.metadata = template.metadata
                        state.metadata.original_task = st.checkbox(
                            "是否执行为原数据集设计的原始任务？",
                            value=template.metadata.original_task,
                            help="提示要求模型执行为该数据集设计的原始任务。",
                        )
                        state.metadata.choices_in_prompt = st.checkbox(
                            "提示中是否会明确列出输出模板中的选择？",
                            value=template.metadata.choices_in_prompt,
                            help="提示明确列出了输出的模板中的选择。",
                        )

                        # Metrics from here:
                        # https://github.com/google-research/text-to-text-transfer-transformer/blob/4b580f23968c2139be7fb1cd53b22c7a7f686cdf/t5/evaluation/metrics.py
                        metrics_choices = [
                            "BLEU",
                            "ROUGE",
                            "Squad",
                            "Trivia QA",
                            "Accuracy",
                            "Pearson Correlation",
                            "Spearman Correlation",
                            "MultiRC",
                            "AUC",
                            "COQA F1",
                            "Edit Distance",
                        ]
                        # Add mean reciprocal rank
                        metrics_choices.append("Mean Reciprocal Rank")
                        # Add generic other
                        metrics_choices.append("Other")
                        # Sort alphabetically
                        metrics_choices = sorted(metrics_choices)
                        state.metadata.metrics = st.multiselect(
                            "指标",
                            metrics_choices,
                            default=template.metadata.metrics,
                            help="选择所有常用的指标（或应该是  "
                            "如果是一个新的任务，就用这个词）来评价这个提示。",
                        )

                        # Answer choices
                        if template.get_answer_choices_expr() is not None:
                            answer_choices = template.get_answer_choices_expr()
                        else:
                            answer_choices = ""
                        state.answer_choices = st.text_input(
                            "答案选择",
                            value=answer_choices,
                            help="一个用于计算答案选择的Jinja表达式。"
                            "用三道杠分开选择 (|||).",
                        )

                        # Jinja
                        state.jinja = st.text_area("模板", height=40, value=template.jinja)

                        # Submit form
                        if st.form_submit_button("保存"):
                            if (
                                updated_template_name in dataset_templates.all_template_names
                                and updated_template_name != state.template_name
                            ):
                                st.error(
                                    f"有一个名称为 {updated_template_name} 已经存在 "
                                    f"为数据集 {state.templates_key}."
                                )
                            elif updated_template_name == "":
                                st.error("需要提供一个提示名称。")
                            else:
                                # Parses state.answer_choices
                                if state.answer_choices == "":
                                    updated_answer_choices = None
                                else:
                                    updated_answer_choices = state.answer_choices

                                dataset_templates.update_template(
                                    state.template_name,
                                    updated_template_name,
                                    state.jinja,
                                    state.reference,
                                    state.metadata,
                                    updated_answer_choices,
                                )
                                # Update the state as well
                                state.template_name = updated_template_name
            #
            # Displays template output on current example if a template is selected
            # (in second column)
            #
            with col2:
                if state.template_name is not None:
                    st.empty()
                    template = dataset_templates[state.template_name]
                    prompt = template.apply(example)
                    if prompt == [""]:
                        st.write("∅∅∅ *空白结果*")
                    else:
                        st.write("输入")
                        show_text(prompt[0], width=40)
                        if len(prompt) > 1:
                            st.write("目标")
                            show_text(prompt[1], width=40)

#
# Must sync state at end
#
state.sync()
