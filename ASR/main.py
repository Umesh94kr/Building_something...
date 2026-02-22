from pywhispercpp.model import Model 
from .recorder import record_until_silence
import os 

BASE_PATH = os.path.dirname(__file__)

# downloads the model on your machine
model = Model('tiny.en')

def transcribe():
    filepath = os.path.join(BASE_PATH, 'output.wav')
    segments = model.transcribe(filepath)
    for segment in segments:
        print(f"[{segment.t0:.2f}s -> {segment.t1:.2f}s] {segment.text}")
    text = " ".join([s.text for s in segments])
    return text

def invoke_ASR():
    record_until_silence()
    text = transcribe()
    print(f"Transcribed text : {text}")
    return text

if __name__ == "__main__":
    record_until_silence()
    text = transcribe()
    print(f"Transcribed text : {text}")
