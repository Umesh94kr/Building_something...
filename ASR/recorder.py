import sounddevice as sd
import numpy as np
import soundfile as sf
import time
import os

BASE_PATH = os.path.dirname(__file__)

def record_until_silence(
    filename="output.wav",
    sample_rate=16000,
    silence_threshold=0.01,
    silence_duration=2.0,
    chunk_duration=0.1
):
    """
    Records audio until 2 seconds of silence detected.
    """

    print("🎤 Speak... (auto stops after silence)")

    chunk_size = int(sample_rate * chunk_duration)
    silence_chunks_required = int(silence_duration / chunk_duration)

    audio_buffer = []
    silence_counter = 0
    recording_started = False

    with sd.InputStream(samplerate=sample_rate, channels=1, dtype='float32') as stream:
        while True:
            chunk, _ = stream.read(chunk_size)
            chunk = chunk.flatten()
            # We use RMS (Root Mean Square) because it measures the energy / loudness of the audio signal.
            rms = np.sqrt(np.mean(chunk**2))

            if rms > silence_threshold:
                recording_started = True
                silence_counter = 0
                audio_buffer.append(chunk)
            else:
                if recording_started:
                    silence_counter += 1
                    audio_buffer.append(chunk)

                    if silence_counter >= silence_chunks_required:
                        print("🛑 Silence detected. Stopping.")
                        break

    audio = np.concatenate(audio_buffer)
    filepath = os.path.join(BASE_PATH, 'output.wav')
    sf.write(filepath, audio, sample_rate)

    print(f"Saved to {filepath}")
    return audio
