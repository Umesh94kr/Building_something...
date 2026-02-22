from ASR.main import invoke_ASR 
from TextToSpeech.main import invoke_TTS


if __name__ == "__main__":
    quest = invoke_ASR()
    answer = "Hey Buddy! I'm doing good."
    invoke_TTS(answer)