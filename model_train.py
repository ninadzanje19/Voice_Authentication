"""import os
import numpy as np
from sklearn.model_selection import train_test_split
from feature_extraction import extract_mfcc
from model_class import VoiceModel
from audio_preprocessing import preprocess_audio
from address import *
from pathlib import Path
# Define directories for raw and processed audio files


process_audio_files = Path(process_audio_dir)
for filename in process_audio_files.iterdir():

    # Preprocess the audio file (e.g., resampling, normalization)
    #preprocess_audio(raw_audio_path, processed_audio_path)

    # Extract MFCC features
    mfcc_features = extract_mfcc(filename)
    # Append features and corresponding label
    for i in mfcc_features:
        features.append(i)
    filename = str(filename)
    labels.append(filename.split('_')[0])  # Assuming label is part of the filename

print(features)
print(labels)
# Convert lists to numpy arrays
X = np.array(features)
y = np.array(labels)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the voice model
voice_model = VoiceModel()
voice_model.train(X_train, y_train)

# Save the trained model to a file
model_path = r'G:\Projects\Voice_Authentication\Voice_Authentication\voice_authentication_model.pkl'
voice_model.save_model(model_path)

print(f"Model trained and saved to {model_path}")"""

import librosa
import numpy as np
from sklearn.mixture import GaussianMixture

def extract_features(audio_file):
    # Load audio file and extract MFCCs
    y, sr = librosa.load(audio_file)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfccs.T, axis=0)

def train_model(features, n_components=16):
    # Train a GMM
    gmm = GaussianMixture(n_components=n_components)
    gmm.fit(features)
    return gmm

def enroll_speaker(name, audio_files):
    features = np.array([extract_features(file) for file in audio_files])
    model = train_model(features)
    return {name: model}

def identify_speaker(audio_file, enrolled_speakers):
    features = extract_features(audio_file)
    scores = {name: model.score(features.reshape(1, -1))
              for name, model in enrolled_speakers.items()}
    return max(scores, key=scores.get)

# Usage
enrolled_speakers = {}
enrolled_speakers.update(enroll_speaker("Alice", ["alice_sample1.wav", "alice_sample2.wav"]))
enrolled_speakers.update(enroll_speaker("Bob", ["bob_sample1.wav", "bob_sample2.wav"]))

unknown_speaker = "unknown_sample.wav"
identified_speaker = identify_speaker(unknown_speaker, enrolled_speakers)
print(f"The speaker is identified as: {identified_speaker}")