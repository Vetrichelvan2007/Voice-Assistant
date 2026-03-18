import pyttsx3
import pywhatkit
import datetime
import time
import webbrowser
import pyjokes
import AppOpener
import requests
import speech_recognition as sr 
import json


assistant=pyttsx3.init()
assistant.setProperty('rate',170)
voices=assistant.getProperty('voices')
assistant.setProperty('voice',voices[1].id)


def talk(text):
    assistant.say(text)
    assistant.runAndWait()

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        talk("listening")
        audio=r.listen(source)
    try:
        comment=r.recognize_google(audio)
        print("you :",comment)
        return comment
    except:
        print("sorry, i cant understand what you re saying")
        return ""

def local_mistral(a):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "mistral",
        "prompt": a,
        "stream": False
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            result = response.json()
            return result['response']
        else:
            return "Sorry, the local model returned an error."
    except requests.exceptions.ConnectionError:
        return "Could not connect to the local model. Please check if Ollama is running."


print("--------Welcome to mini voice assistant--------")
# talk("Welcome to mini voice assistant")
# talk("i can do the following things")

print("1.i can open browser")
print("2.i play any songs on youtube")
print("3.i can open any app")
print("4.i can searck anything in google")
print("5.i can tell joke")
print("6.i can tell the current time and date")

while(True):
    
    a=listen()
    words=a.split()

    if "hello" in words or "hi" in words:
        talk("hi. how can i help you")
        time.sleep(0.5)

    elif "browser" in words or "google" in words or "chrome" in words:
        a=a.replace("open","")
        talk("openning"+a)
        webbrowser.open('https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwiujvis_6qNAxW4SmwGHSgPOJ4QPAgI')

    elif "search" in  words and "google" in  words:
        a=a.replace("search","").strip()
        talk("search for "+a)

    elif "play" in words:
        a=a.replace("play","").strip()
        if a:
            talk("playing"+a)
            pywhatkit.playonyt(a)
        else:
            print("enter the song name")
            
    elif "open" in words:
        a=a.replace("open","").strip()
        if a:
            try:
                talk("openning"+a)
                AppOpener.open(a)
            except:
                talk("sorry, i cant able to open gthe app")
                print("sorry, i cant able to open gthe app")
    elif "joke" in words:
        joke=pyjokes.get_joke(language="en",category="all")
        print(joke)
        talk(joke)
    
    elif "date" in words or "time" in words:
        now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")   
        print("the current date and time is",now)
        talk("the current date and date is "+ now)

    elif "exit" in words:
        break

    else:
        if a:
            reply = local_mistral(a)
            print("Assistant:", reply)
            talk(reply  )

