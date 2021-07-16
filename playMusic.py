#!/usr/bin/env python3
from selenium import webdriver
from bs4 import BeautifulSoup
import pyttsx3


def playYoutubeMusic(command):
    command.lower()
    command = command.replace("cypher play", "")

    videoplayer = ""
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/results?search_query=" + command)
    driver.maximize_window()

    data = driver.execute_script("return document.documentElement.outerHTML")

    soup = BeautifulSoup(data, 'html.parser')

    videoid = 1

    for link in soup.find_all('a', {'class', 'ytd-video-renderer'}):

        url = link.get("href")
        if videoid == 2:
            videoplayer = url
            print(url)

        videoid += 1

        driver.quit()

    engine = pyttsx3.init()
    engine.say(
        "Your video is in Processing. It is depend upon yout Internet speed. Please wait for some Moments.")
    engine.runAndWait()

    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com" + videoplayer)
    driver.maximize_window()
