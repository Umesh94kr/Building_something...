from pywhispercpp.model import Model 
from recorder import record_audio

model = Model('tiny.en')

def transcribe():
    segments = model.transcribe('output.wav')
    for segment in segments:
        print(f"[{segment.t0:.2f}s -> {segment.t1:.2f}s] {segment.text}")
    text = " ".join([s.text for s in segments])
    return text

if __name__ == "__main__":
    record_audio()
    text = transcribe()
    print(f"Transcribed text : {text}")
