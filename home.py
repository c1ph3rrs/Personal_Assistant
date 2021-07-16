#!/usr/bin/env python3

from playsound import playsound
from programInfo import yourInfo as info
from googleSearch import searchfromGoogle as search
from playMusic import playYoutubeMusic as music
from openSomething import openSomeThing as some
from exitProgram import exitprogram as ex
from Calender import calender as cal
import speech_recognition as sr
from selenium import webdriver
import pyttsx3
import datetime
import os


runningState = True


def startPlayAudio():
    playsound('audio/play.mp3')


def stopListiningAudio():
    playsound('audio/close.mp3')


def startListining():
    global command
    startPlayAudio()

    engine = pyttsx3.init()
    engine.say("Please Say Something. I'm Listining")
    engine.runAndWait()
    print("Please Say Something. I am Listining")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        command = input("Please Enter the Command")
        # audio = r.listen(source)
        # command = r.recognize_google(audio)
        print("text = " + command)

        if "Cipher" or "cypher" in command:
            if "your info" in command or "about you" in command:
                info(command)

            elif "launch" in command:
                application = command.replace('cypher launch ', '')
                application = application.lower()
                application = application.replace(' ', '-')
                engine = pyttsx3.init()
                print("Opening " + application)
                engine.say("Opening " + application)

                engine.runAndWait()
                os.system(application)

            elif "who is" in command or "who" in command or "tell me about" in command:
                search(command)

            elif "calendar" in command:
                cal()

            elif "time" in command:
                currentDT = datetime.datetime.now()
                engine = pyttsx3.init()
                engine.say(currentDT.strftime("%I:%M:%S %p"))
                print(currentDT.strftime("%I:%M:%S %p"))
                engine.runAndWait()

            elif "open" in command:
                some(command)

            elif "play" in command:
                music(command)

            elif "exit" in command or "shutdown" in command or "terminate" in command or "sleep" in command:
                global runningState
                runningState = ex()

            else:
                print("Sorry Sir. I am not understand Your Command. Please Speek Again")
                engine = pyttsx3.init()
                engine.say(
                    "Sorry Sir. I am not understand Your Command. Please Speek Again")
                engine.runAndWait()
        else:
            print("")

    stopListiningAudio()


while runningState == True:
    startListining()
