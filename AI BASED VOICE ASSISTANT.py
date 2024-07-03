import datetime
import pyttsx3
import speech_recognition
import pyaudio
import requests
from  bs4 import Beautifulsoup
import wikipedia
import webbrowser
import xml

from intro import play_gif
play_gif

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
        r.adjust_for_ambient_noise(source)
        print("Listening....")
        r.pause_threshold = 1  # this will take 1 sec pause and will execute after 1 sec
        r.energy_threshold = 300# this will neither take outside voices nor too much look voice that unable to recognise
        audio = r.listen(source, timeout=0, phrase_time_limit=4)  # it will wait for 4 sec and execute afterward


    try:
        print("Understanding...")
        query = r.recognise_google(audio,language = 'en-in')
        print(f"You Said: {query}\n")

    except Exception as e:  # if don't say anything
        print("Say that again")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()  # this will continue to listen to user but will not stop the execution of program
                if "go to sleep" in query:
                    speak("Ok mam , You can me call anytime")
                    break 

# here we'll start CONVERSATION
                elif "hello" in query:
                    speak("Hello ekta, how are you?")
                elif "i am fine" in query:
                    speak("that's great, good to hear that")
                elif "how are you?" in query:
                    speak("Perfect from this side as well")
                elif "how was your today" in query:
                    speak("It was wonderful day today! how was your day?")
                elif "same here, OK thank you" in query:
                    speak("your welcome mam, anytime")

# searching famous site from webbrowser
                elif "google" in query:
                    from searchnow import searchGoogle
                    searchGoogle()
                elif "youtube" in query:
                    from searchnow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from searchnow import searchwikipedia
                    searchwikipedia(query)

# automating temperature and weather

                elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}" + search
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}" + search
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                
# automating time
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"mam, the time is {strTime}")

# Google translate                  
                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("malti","")
                    query = query.replace("translate","")
                    translategl(query)

# News function 
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews() 

# calculator
                elif "calculator" in query:
                    from CalculateNumbers import WolfRamAlpha
                    from CalculateNumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("malti","")
                    Calc(query)

# Hotward detection
                elif "finally sleep" in query:  # this function will stop the jarvis from listening mode and the file will stop executing
                    speak("Going to sleep, mam")
                    exit()

                