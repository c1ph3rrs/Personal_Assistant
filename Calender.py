#!/usr/bin/env python3
import datetime
import pyttsx3


def calender():
    currentDT = datetime.datetime.now()
    engine = pyttsx3.init()
    engine.say(currentDT.strftime("%A, %B %d, %Y"))
    print(currentDT.strftime("%A, %B %d, %Y"))
    engine.runAndWait()
