#!/usr/bin/env python3
from selenium import webdriver
from bs4 import BeautifulSoup
import pyttsx3

description = ""


def searchfromGoogle(command):

    command = command.lower()
    command = command.replace("cypher", "")
    command = command.replace("tell me about", "")
    command = command.replace("who is" or "what is", "")

    driver = webdriver.Chrome()

    driver.get("https://www.google.com/search?q=" + command)

    data = driver.execute_script("return document.documentElement.outerHTML")

    driver.quit()

    req = BeautifulSoup(data, 'html.parser')
    soup = req.find('div', {'class', 'kno-rdesc'})

    for soup in soup.find_all('span'):
        global description
        description = soup.get_text()
        print(description)

        engine = pyttsx3.init()
        engine.say(description)
        engine.runAndWait()
