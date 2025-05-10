
from ast import NodeTransformer
from datetime import datetime
from email.mime import audio

from logging import exception
from unittest.mock import patch
import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import speech_recognition as s
import pyttsx3
import wikipedia
import webbrowser
import os
r = sr.Recognizer()
engine = pyttsx3.init()
qnumber="no task"

def SpeakText(command):
    engine.setProperty("rate",150)
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(command)
    engine.runAndWait()
    
def speaking():
    with sr.Microphone() as source2:
        r.energy_threshold=250
        r.adjust_for_ambient_noise(source2,duration=5)
        print("listening..")
        r.pause_threshold=0.5
        audio2 = r.listen(source2)
        try:
             MyText = r.recognize_google(audio2,language='en-IN')
             MyText = MyText.lower()
             print("Did you say "+MyText)
             #SpeakText(MyText)
        except:
             print("say that again please...")
             speaking()
        return MyText


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        SpeakText("good morning sir!,please confirm the password.")
        security()
    elif hour>=12 and hour<18:
        SpeakText("good afternoon sir!,please confirm the password.")
        security()
    else:
        SpeakText("good evening sir!,please confirm the password.")
        security()
       


def activation():
    query=speaking().lower()
    if 'jarvis' in query:
        wishme()
    '''else:
        SpeakText("sorry sir, first you have to speak my name to run any command,do you know my name??")
        m=speaking()
        if 'no ' in m:
            SpeakText('sorry sir, i cannot give you the access to my command')
        elif 'yes 'in m:
            SpeakText('please confirm my name')
            activation()'''


def security():
     a=speaking().lower()
     if a=='1234':
        SpeakText("identity confirmed")
        task()

     else:
        SpeakText("identity denied, do you want to try it again?")
        m=speaking()
        if 'yes' in m:
            SpeakText("again,say the password")
            security()
        else:
            SpeakText("thankyou for calling me")
def task():

    SpeakText("what can i do for you sir ?")        
    query=speaking().lower()
    if 'tell me about' in query:
            SpeakText('searching sir...')
            query=query.replace('search about',"")
            results=wikipedia.summary(query,sentences=2)
            SpeakText('according to the information')
            print(results)
            SpeakText(results)
            SpeakText("sir can i do anything else for you?")
            a=speaking().lower()
            if a=="yes":
                 task()
            elif a=='no':
                 SpeakText("ok sir i am always at your service,you can call me whenever you want.")
    elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            SpeakText("sir can i do anything else for you?")
            a=speaking().lower()
            if a=="yes":
                 task()
            elif a=='no':
                 SpeakText("ok sir i am always at your service,you can call me whenever you want.")
    elif 'open google' in query:
            webbrowser.open("google.com")    
            SpeakText("sir can i do anything else for you?")
            a=speaking().lower()
            if a=="yes":
                 task()
            elif a=='no':
                 SpeakText("ok sir i am always at your service,you can call me whenever you want.")
    elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            SpeakText("sir, the time is")
            SpeakText(strtime)
            SpeakText("sir can i do anything else for you?")
            a=speaking().lower()
            if a=="yes":
                 task()
            elif a=='no':
                 SpeakText("ok sir i am always at your service,you can call me whenever you want.")
           # elif 'vs code' in query:
                #path='C:\Users\HP\Downloads'
                #os.startfile()
    elif 'note my task' in query:
            SpeakText("sure sir,please tell me the tasks you want to complete today")
            #qnumber="no task"
            qnumber=speaking().lower()
            SpeakText("ok sir , i will remind you the task")
            SpeakText("sir can i do anything else for you?")
            a=speaking().lower()
            if a=="yes":
                 task()
            elif a=='no':
                 SpeakText("ok sir i am always at your service,you can call me whenever you want.")
                 
    elif 'shutdown' in query:
            SpeakText('as you command sir.')
            


activation()


