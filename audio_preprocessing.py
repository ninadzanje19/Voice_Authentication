from pydub import AudioSegment
from pathlib import Path
from setuptools.extern import names
from pydub import AudioSegment
from feature_extraction import *
from address import *
from Extra_Functions import *


def preprocess_audio(input_dir, output_dir):
    names = get_name(input_dir)
    input_dir = Path(input_dir)

    for i, j in zip(input_dir.iterdir(),names):
        audio = AudioSegment.from_file(i)
        audio = audio.set_channels(1).set_frame_rate(16000)
        process_audio_name = str(output_dir) + "\\" +j + ".wav"
        audio.export(process_audio_name, format="wav")

preprocess_audio(audio_dir, process_audio_dir)




"""def remove_background_noise(input_path, output_path):
    # Load the audio file
    audio = AudioSegment.from_file(input_path)

    # Convert AudioSegment to numpy array
    samples = np.array(audio.get_array_of_samples())

    # Get the sample rate
    sample_rate = audio.frame_rate

    # Perform noise reduction
    reduced_noise = nr.reduce_noise(y=samples, sr=sample_rate)

    # Convert the numpy array back to AudioSegment
    cleaned_audio = AudioSegment(
        reduced_noise.tobytes(),
        frame_rate=sample_rate,
        sample_width=samples.dtype.itemsize,
        channels=1
    )

    # Export the cleaned audio to a file
    cleaned_audio.export(output_path, format="wav")

    print(f"Cleaned audio saved to {output_path}")


# Example usage
input_path = 'path/to/your/input/audio/file.wav'
output_path = 'path/to/your/output/audio/cleaned_file.wav'
remove_background_noise(input_path, output_path)
"""