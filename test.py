# Python program to translate
# speech to text and text to speech


import importlib
import speech_recognition as sr
import pyttsx3
import os

# Initialize the recognizer
r = sr.Recognizer()
os.remove('text.py')
f = open("text.py", "w")
f.write("def voiceCommand():\n  print('') \n")
f.close()
print('ready:')


# Function to convert text to
# speech
def SpeakText(command):
  
  # Initialize the engine
  engine = pyttsx3.init()
  engine.say(command)
  engine.runAndWait()
  
  
# Loop infinitely for user to
# speak

while(1):

  
  # Exception handling to handle
  # exceptions at the runtime
  try:
    
    # use the microphone as source for input.
    with sr.Microphone() as source2:
      # wait for a second to let the recognizer
      # adjust the energy threshold based on
      # the surrounding noise level
      r.adjust_for_ambient_noise(source2, duration=0.2)
      
      #listens for the user's input
      audio2 = r.listen(source2)
      
      # Using google to recognize audio
      MyText = r.recognize_google(audio2)
      MyText = MyText.lower()
      print(f"heard: {MyText}")
  except sr.RequestError as e:
    print(f"Nothing found, try help")
    SpeakText(f"Nothing found, try help")
    # print("Could not request results; {0}".format(e))
    
  except sr.UnknownValueError:
    print(f"Nothing found, try help")
    SpeakText(f"Nothing found, try help")
    # print("unknown error occured")