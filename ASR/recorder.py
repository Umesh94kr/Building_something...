import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

def record_audio(filename="output.wav", duration=5, sample_rate=16000, channels=1):
    """
    Records audio from the default microphone and saves it as a WAV file.

    Args:
        filename (str): Output WAV file name.
        duration (int): Duration of recording in seconds.
        sample_rate (int): Sampling rate (Hz).
        channels (int): Number of audio channels (1 = mono, 2 = stereo).
    """
    print(f"Recording for {duration} seconds...")
    
    # Record audio
    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=channels,
        dtype='int16'
    )
    
    sd.wait()  # Wait until recording is finished
    # Save to WAV file
    write(filename, sample_rate, recording)
    print(f"Saved recording to {filename}")
