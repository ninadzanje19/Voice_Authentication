from pydub import AudioSegment
from pathlib import Path
from setuptools.extern import names
from pydub import AudioSegment
from feature_extraction import *
from address import *
from Extra_Functions import *


"""def preprocess_audio(input_dir, output_dir):
    names = get_names(input_dir)
    input_dir = Path(input_dir)

    for i, j in zip(input_dir.iterdir(),names):
        audio = AudioSegment.from_file(i)
        audio = audio.set_channels(1).set_frame_rate(16000)
        process_audio_name = str(output_dir) + "\\" +j + ".wav"
        audio.export(process_audio_name, format="wav")"""

def preprocess_audio(input_audio, output_dir, target_dBFS=-20.0):
    audio = AudioSegment.from_file(input_audio)
    audio = audio.set_channels(1).set_frame_rate(16000)
    audio = rms_normalize(audio, target_dBFS)
    process_audio_name = str(output_dir) + "\\" + get_name(input_audio) + ".wav"
    audio.export(process_audio_name, format="wav")
    return process_audio_name


print(preprocess_audio(r"G:\Projects\Voice_Authentication\Voice_Authentication\data\audio_data\Akshay\Akshay_angry.ogg", process_audio_dir))


