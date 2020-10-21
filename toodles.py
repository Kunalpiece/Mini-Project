import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import subprocess as sp
from selenium import webdriver
import pyautogui
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")   

    else:
        print("Good Evening!")
        speak("Good Evening!")  

    print("I am Oh Toodle. Please tell me how may I help you.")
    speak("I am Oh Toodle. Please tell me how may I help you.")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.record(source,duration=5)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)   
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
            driver.get("https://www.youtube.com/")
            pyautogui.click(284,168)
            driver.maximize_window()
            print("What do you want to search?")
            speak("What do you want to search?")
            cont = takeCommand()
            pyautogui.typewrite(cont)
            pyautogui.typewrite(["enter"])
            time.sleep(10)
            driver.close()

        elif 'open google' in query:
            driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
            driver.get("https://www.google.com/")
            pyautogui.click(474,423)
            driver.maximize_window()
            print("What do you want to search?")
            speak("What do you want to search?")
            cont = takeCommand()
            pyautogui.typewrite(cont)
            pyautogui.typewrite(["enter"])
            time.sleep(10)
            driver.close()

        elif 'play music' in query:
            driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
            driver.get("https://www.gaana.com/")
            pyautogui.click(430,221)
            driver.maximize_window()
            print("Which song you want to listen?")
            speak("Which song you want to listen?")
            cont = takeCommand()
            pyautogui.typewrite(cont)
            pyautogui.typewrite(["enter"])
            time.sleep(10)
            driver.close()

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open file' in query:
            speak("Name of the file to open.")
            cont = takeCommand()
            con = takeCommand() + ".txt"
            sp.Popen(['notepad.exe', con])
            file1 = open(con,'a')
            speak("What do you want to write?")
            cont = takeCommand()
            file1.write(cont)
            file1.close()
            
            file1 = open(con,'rt')
            print("Reading content of file")
            speak("Reading content of file")
            speak(file1.read())
            file1.close()