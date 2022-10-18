# coding=utf-8
import os

import datasets
import requests

from templates import INCLUDED_USERS

DEFAULT_PROMPTSOURCE_CACHE_HOME = ".cache/"


def removeHyphen(example):
    example_clean = {}
    for key in example.keys():
        if "-" in key:
            new_key = key.replace("-", "_")
            example_clean[new_key] = example[key]
        else:
            example_clean[key] = example[key]
    example = example_clean
    return example


def renameDatasetColumn(dataset):
    col_names = dataset.column_names
    for cols in col_names:
        if "-" in cols:
            dataset = dataset.rename_column(cols, cols.replace("-", "_"))
    return dataset


#
# Helper functions for datasets library
#


def get_dataset_builder(path, conf=None):
    "Get a dataset builder from name and conf."
    module_path = datasets.load.dataset_module_factory(path)
    builder_cls = datasets.load.import_main_class(module_path.module_path, dataset=True)
    if conf:
        builder_instance = builder_cls(name=conf, cache_dir=None, hash=module_path.hash)
    else:
        builder_instance = builder_cls(cache_dir=None, hash=module_path.hash)
    return builder_instance


def get_dataset(path, conf=None):
    "Get a dataset from name and conf."
    builder_instance = get_dataset_builder(path, conf)
    if builder_instance.manual_download_instructions is None and builder_instance.info.size_in_bytes is not None:
        builder_instance.download_and_prepare()
        return builder_instance.as_dataset()
    else:
        return load_dataset(path, conf)


def load_dataset(dataset_name, subset_name):
    cache_root_dir = (
        os.environ["PROMPTSOURCE_MANUAL_DATASET_DIR"]
        if "PROMPTSOURCE_MANUAL_DATASET_DIR" in os.environ
        else DEFAULT_PROMPTSOURCE_CACHE_HOME
    )
    data_dir = (
        f"{cache_root_dir}/{dataset_name}"
        if subset_name is None
        else f"{cache_root_dir}/{dataset_name}/{subset_name}"
    )
    print(data_dir)
    return datasets.load_dataset(
        dataset_name,
        subset_name,
        data_dir=data_dir,
    )


def get_dataset_confs(path):
    "Get the list of confs for a dataset."
    module_path = datasets.load.dataset_module_factory(path).module_path
    # Get dataset builder class from the processing script
    builder_cls = datasets.load.import_main_class(module_path, dataset=True)
    # Instantiate the dataset builder
    confs = builder_cls.BUILDER_CONFIGS
    if confs and len(confs) > 1:
        return confs
    return []


def render_features(features):
    """Recursively render the dataset schema (i.e. the fields)."""
    if isinstance(features, dict):
        return {k: render_features(v) for k, v in features.items()}
    if isinstance(features, datasets.features.ClassLabel):
        return features.names

    if isinstance(features, datasets.features.Value):
        return features.dtype

    if isinstance(features, datasets.features.Sequence):
        return {"[]": render_features(features.feature)}
    return features


#
# Loads dataset information
#


def filter_datasets():

    chinese_datasets = []

    dataset_file_path = "/data/xx/test_github/createprompt_test/promptsource/datasets"
    dataset_file_name = os.listdir(dataset_file_path)
    for dataset_name in dataset_file_name:
        chinese_datasets.append(dataset_name)

    return sorted(chinese_datasets)


def list_datasets():
    """Get all the datasets to work with."""
    dataset_list = filter_datasets()
    dataset_list.sort(key=lambda x: x.lower())
    return dataset_list
