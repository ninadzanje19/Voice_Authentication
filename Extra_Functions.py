from pathlib import Path

from address import audio_dir


def get_names(directory):
    directory = Path(directory)
    name_list = []
    for i in directory.iterdir():
        i = str(i)
        i = i.split('\\')[-1]
        i = i.split('.')[0]
        name_list.append(i)
    return name_list


def get_name(file):
    file = Path(file)
    file = str(file)
    file = file.split('\\')[-1]
    file = file.split('.')[0]
    return file


def create_dir(directory):
    for i in get_names(directory):
        i = i.split('_')[0]
        print(i)


def give_name():
    pass