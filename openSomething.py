#!/usr/bin/env python3
from selenium import webdriver
import pyttsx3


def openSomeThing(command):
    driver = webdriver.Chrome()
    command = command.lower()

    if "google" in command:
        engine = pyttsx3.init()
        engine.say("Opening Google")
        engine.runAndWait()

        driver.get("https://www.google.com")

    elif "facebook" in command:
        engine = pyttsx3.init()
        engine.say("Opening Facebook")
        engine.runAndWait()
        driver.get("https://www.facebook.com")

    elif "twitter" in command:
        engine = pyttsx3.init()
        engine.say("Opening Twitter")
        engine.runAndWait()
        driver.get("https://twitter.com")

    elif "instagram" in command:
        engine = pyttsx3.init()
        engine.say("Opening Instagram")
        engine.runAndWait()
        driver.get("https://www.instagram.com")

    elif "gmail" in command:
        engine = pyttsx3.init()
        engine.say("Opening Gmail")
        engine.runAndWait()
        driver.get("https://mail.google.com")

    elif "youtube" in command:
        engine = pyttsx3.init()
        engine.say("Opening Youtube")
        engine.runAndWait()
        driver.get("https://www.youtube.com")

    else:
        print("Sorry Sir. I have no permission to open this")
        engine = pyttsx3.init()
        engine.say("Sorry Sir. I have no permission to open this")
        engine.runAndWait()
