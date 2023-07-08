# import speech_recognition as sr
# import os

# def say(text):
#     os.system("say {text}")
    



# if __name__ == '__main__':
#  print('Pycharm')
#  say("hello I am jarvis AI")
 
 
 
# import pyttsx3

# # Create a TTS engine
# engine = pyttsx3.init()

# # Set properties (optional)
# engine.setProperty('rate', 150)  # Speed of speech

# # Convert text to speech
# text = "Hello, how are you?"
# engine.say(text)

# # Play the speech
# engine.runAndWait()


import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while  1:
    print ('enter the word you want t speak it out by computer')
    s = input()
    speaker.Speak(s)