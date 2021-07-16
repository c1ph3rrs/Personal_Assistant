#!/usr/bin/env python3
import pyttsx3


def exitprogram():

    runningState = False

    print(
        "As you wish Sir. Thanks for your Precious time. I am going to exit. If you need any help Than you can")
    print("re run this Program and i will Come back")
    print(
        "Terminate Request has been send. Waiting for System to respond back. Done. Program is now going to Terminate. Take Care")

    engine = pyttsx3.init()

    engine.say(
        "As you wish Sir. Thanks for your Precious time. I am going to exit. If you need any help Than you can")
    engine.say("re run this Program and i will Come back")
    engine.say(
        "Terminate Request has been send. Waiting for System to respond back. Done. Program is now going to Terminate. Take Care")

    engine.runAndWait()

    return runningState
