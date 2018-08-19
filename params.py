# coding: utf-8
from os.path import join, expanduser
from nnmnkwii.datasets import jsut, voice_statistics

dataset = voice_statistics
dataset_script_kwargs = {"column": "yomi"}
dataset_wav_kwargs = {"speakers": ["uemura"], "emotions": ["angry"]}

in_dir = join(expanduser("~"), "data/voice-statistics/")
dst_dir = "outputs_{}_{}".format(dataset_wav_kwargs["speakers"][0], dataset_wav_kwargs["emotions"][0])
