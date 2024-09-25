from pathlib import Path

from address import audio_dir


def get_name(directory):
    directory = Path(directory)
    name_list = []
    for i in directory.iterdir():
        i = str(i)
        i = i.split('\\')[-1]
        i = i.split('.')[0]
        name_list.append(i)
    return name_list

print(get_name(audio_dir))

def create_dir(directory):
    for i in get_name(directory):
        i = i.split('_')[0]
        print(i)