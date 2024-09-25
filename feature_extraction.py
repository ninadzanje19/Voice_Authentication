import numpy as np
import scipy.io.wavfile as wav
from pydub import AudioSegment
from python_speech_features import mfcc
from pathlib import Path
from address import process_audio_dir, features, audio_dir


def extract_mfcc(file_path, num_cepstral=13, nfft=512):
        # Read the audio file
        sample_rate, signal = wav.read(file_path)

        # Extract MFCC features
        mfcc_features = mfcc(signal, sample_rate, numcep=num_cepstral, nfft=nfft)

        # Compute the mean of the MFCC features along time axis
        mfcc_mean = np.mean(mfcc_features, axis=0)

        #features.append(mfcc_mean)
        return mfcc_mean


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



def get_amplitude(audio_path):
    # Read the audio file
    sample_rate, signal = wav.read(audio_path)

    # If the signal is stereo, take only one channel
    if signal.ndim > 1:
        signal = signal[:, 0]

    # Get the absolute amplitude values and convert them to integers
    amplitude = np.abs(signal).astype(int)

    return amplitude


def get_loudness(audio_path):
    # Load the audio file
    audio = AudioSegment.from_file(audio_path)

    # Get the loudness in dBFS (decibels relative to full scale)
    loudness = audio.dBFS

    return loudness


def rms_normalize(audio_segment, target_dBFS):
    """Normalize given audio segment to target dBFS."""
    change_in_dBFS = target_dBFS - audio_segment.dBFS
    return audio_segment.apply_gain(change_in_dBFS)

def normalize_audio(input_path, output_path, target_dBFS=-20.0):
    # Load the audio file
    audio = AudioSegment.from_file(input_path)

    # Normalize the audio to the target dBFS
    normalized_audio = rms_normalize(audio, target_dBFS)

    # Export the normalized audio
    normalized_audio.export(output_path, format="wav")



# Example usage
#arr1 = r"G:\Projects\Voice_Authentication\Voice_Authentication\data\data\process\audio2.wav"
#arr2 = r"G:\Projects\Voice_Authentication\Voice_Authentication\data\data\process\audio3.wav"
#arr3 = r"G:\Projects\Voice_Authentication\Voice_Authentication\data\process_audio\audio1.wav"
#arr4 = r"G:\Projects\Voice_Authentication\Voice_Authentication\data\process_audio\audio77.wav"
#print(f"Similarity Percentage: {similarity_percentage(arr4, arr3):.2f}%")

#extract_mfcc(r"G:\Projects\Voice_Authentication\Voice_Authentication\data\data\process\audio1.wav")
#extract_mfcc(r"G:\Projects\Voice_Authentication\Voice_Authentication\data\data\process\audio2.wav")

