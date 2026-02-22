from .translator import speak

def invoke_TTS(text):
    speak(text)

if __name__ == "__main__":
    text = input("Write your text input? ")
    speak(text)