from TTS.api import TTS
import sounddevice as sd

# Load model (downloads first time)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

def speak(text):
    wav = tts.tts(text)
    sd.play(wav, samplerate=22050)
    sd.wait()