import pyttsx3


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        
  
    def say_text(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

