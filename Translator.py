from fnmatch import translate
from time import sleep
from googletrans import Translator
import googletrans
from gtts import gTTS
import pyttsx3
import speech_recognition 
import os
from playsound import playsound
import time


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)
print(voices[0])

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1  # this will take 1 sec pause and not execute after 1 sec
        r.energy_threshold = 300  # this will neither take outside voices nor too much look voice that unable to recognise
        audio = r.listen(source, 0, 4)  # it will wait for 4 sec and execute afterward


    try:
        print("Understanding...")
        query = r.recognise_google(audio, language = 'en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def translategl(query):
    speak("sure mam")
    print(googletrans.LANGUAGES)
    # to invoke the translator
    translator = Translator()
    speak("Choose the language in which you want to translate")
    b = input("To_Lang :- ")   
    # translating from source to destination
    text_to_translate = translator.translate(query,src = "auto",dest= b)
    text = text_to_translate.text
    try : 
        # 3rd argument is given false as by default it speaks very slowly
        speakgl = gTTS(text=text, lang=b, slow= False)
        # speech in capture_voice.mp3
        # the translated voice will be saved as "voice.mp3" file
        speakgl.save("voice.mp3")
        playsound("voice.mp3")
        
        # using os module to run translated voice
        # using time/ sleep module to 
        time.sleep(5)
        os.remove("voice.mp3")
    except:
        print("Unable to translate")

