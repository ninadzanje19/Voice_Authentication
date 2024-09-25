from pydub import AudioSegment
from pathlib import Path
from setuptools.extern import names
from pydub import AudioSegment
import numpy as np
import scipy.io.wavfile as wav
from pydub import AudioSegment
from python_speech_features import mfcc
from address import *
from Extra_Functions import *

#get the names of all the files from a directory
def get_names(directory):
    directory = Path(directory)
    name_list = []
    for i in directory.iterdir():
        i = str(i)
        i = i.split('\\')[-1]
        i = i.split('.')[0]
        name_list.append(i)
    return name_list

#get the name of a file from its address
def get_name(file):
    file = Path(file)
    file = str(file)
    file = file.split('\\')[-1]
    file = file.split('.')[0]
    file = file.replace(" ", "_")
    return file


#preprocess the audio directory
def preprocess_audio_dir(input_dir, output_dir):
    names = get_names(input_dir)
    input_dir = Path(input_dir)

    for i, j in zip(input_dir.iterdir(),names):
        audio = AudioSegment.from_file(i)
        audio = audio.set_channels(1).set_frame_rate(16000)
        process_audio_name = str(output_dir) + "\\" +j + ".wav"
        audio.export(process_audio_name, format="wav")




#extract mfcc data of a particular audio file
def extract_mfcc(file_path, num_cepstral=13, nfft=512):
    # Read the audio file
    sample_rate, signal = wav.read(file_path)

    # Extract MFCC features
    mfcc_features = mfcc(signal, sample_rate, numcep=num_cepstral, nfft=nfft)

    # Compute the mean of the MFCC features along time axis
    mfcc_mean = np.mean(mfcc_features, axis=0)

    #features.append(mfcc_mean)
    return mfcc_mean


#compare similarity between two audio files
def similarity_percentage(voice1, voice2):
    #get mfcc data
    voice1 = extract_mfcc(voice1)
    voice2 = extract_mfcc(voice2)
    # Ensure the arrays have the same length
    if len(voice1) != len(voice2):
        raise ValueError("Arrays must have the same length")

    # Convert lists to numpy arrays if they aren't already
    vec1 = np.array(voice1)
    vec2 = np.array(voice2)

    # Compute the dot product
    dot_product = np.dot(vec1, vec2)

    # Compute the norm (magnitude) of each vector
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)

    # Compute the cosine similarity
    cosine_similarity = dot_product / (norm1 * norm2)

    # Convert to percentage
    similarity_percentage = cosine_similarity * 100

    return {"result": similarity_percentage, "voice1_mfcc": list(voice1), "voice2_mfcc": list(voice2)}
#    return similarity_percentage


#get the amplitudes of the audio file returns and array
def get_amplitude(audio_path):
    # Read the audio file
    sample_rate, signal = wav.read(audio_path)

    # If the signal is stereo, take only one channel
    if signal.ndim > 1:
        signal = signal[:, 0]

    # Get the absolute amplitude values and convert them to integers
    amplitude = np.abs(signal).astype(int)

    return amplitude

#get the lodness of the audio file
def get_loudness(audio_path):
    # Load the audio file
    audio = AudioSegment.from_file(audio_path)

    # Get the loudness in dBFS (decibels relative to full scale)
    loudness = audio.dBFS

    return loudness


#normalize by using rms
def rms_normalize(audio_segment, target_dBFS):
    """Normalize given audio segment to target dBFS."""
    change_in_dBFS = target_dBFS - audio_segment.dBFS
    return audio_segment.apply_gain(change_in_dBFS)


#normalize the audio file to a set loudness
def normalize_audio(input_path, output_path, target_dBFS=-20.0):
    # Load the audio file
    audio = AudioSegment.from_file(input_path)

    # Normalize the audio to the target dBFS
    normalized_audio = rms_normalize(audio, target_dBFS)

    # Export the normalized audio
    normalized_audio.export(output_path, format="wav")


#preprocess the audio file
def preprocess_audio(input_audio, output_dir, target_dBFS=-20.0):
    audio = AudioSegment.from_file(input_audio)
    audio = audio.set_channels(1).set_frame_rate(16000)
    audio = rms_normalize(audio, target_dBFS)
    process_audio_name = str(output_dir) + "\\" + get_name(input_audio) + ".wav"
    audio.export(process_audio_name, format="wav")
    return process_audio_name

def slash_replace(file_name):
    file_name = str(file_name)
    file_name = file_name.split("\\")
    file_name_fslash = ""
    for i in file_name:
        file_name_fslash += i
        if i == file_name[-1]:
            break
        file_name_fslash += "/"
    return file_name_fslash

print(slash_replace("G:\Projects\Voice_Authentication\Voice_Authentication\processed_audio_files\Akshay_angry.wav")
)