import speech_recognition as sr

class SpeechToWord:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def get_word_from_speech(self):
        waiting = True
        word = ""
        while(waiting):
            print("listening")
            with sr.Microphone() as source2:

                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                self.recognizer.adjust_for_ambient_noise(source2, duration=0.5)
                
                #listens for the user's input
                audio2 = self.recognizer.listen(source2)
                
                # Using google to recognize audio
                MyText = self.recognizer.recognize_google(audio2)
                MyText = MyText.lower()
                word = MyText
                waiting = False
        return word
        
            

    