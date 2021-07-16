#!/usr/bin/env python3
import pyttsx3


def yourInfo(command):

    if "your name" in command:
        print("My name is Cipher. And i am a Program")
        engine = pyttsx3.init()
        engine.say("My name is Cipher. And i am a Program")
        engine.runAndWait()

    elif "developed you" in command or "code you" in command or "make you" in command:
        print("Ibrahim Akram is a Person who Developed me. He is a very nice Guy")
        engine = pyttsx3.init()
        engine.say(
            "Ibrahim Akram is a Person who Developed me. He is a very nice Guy")
        engine.runAndWait()

    elif "how are you" in command:
        print("It is your pleasure Sir. Thanks. I am Fine. How are You")
        engine = pyttsx3.init()
        engine.say("It is your pleasure Sir. Thanks. I am Fine. How are You")
        engine.runAndWait()

    else:
        print("I have no words for this question. Please ask another question")
        engine = pyttsx3.init()
        engine.say(
            "I have no words for this question. Please ask another question")
        engine.runAndWait()
