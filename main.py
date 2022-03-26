import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import subprocess as sp
import time
import pyjokes
import winshell
import subprocess
import json
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def reply(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        #audio = r.record(source,duration=5)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        reply("Say that again please...")  
        return "None"
    
    return query

def sendEmail(to, content,eid,password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(eid,password)
    server.sendmail(eid, to, content)
    server.close()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        reply("Good Morning!")

    elif hour>=12 and hour<18:
        reply("Good Afternoon!")
    else:
        reply("Good Evening!")  

    reply("I am Toodle. Please tell me how may I help you")

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand()
        if 'wikipedia' in query:
            reply('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            reply("According to Wikipedia")
            reply(results)

        elif 'location' in query:
            reply('Which place are you looking for ?')
            temp_audio = takeCommand()
            reply(temp_audio)
            reply('Locating...')
            url = 'https://google.nl/maps/place/' + temp_audio + '/&amp;'
            try:
                webbrowser.get().open(url)
                reply('This is what I found Sir')
            except:
                reply('Please check your Internet')

        elif 'search' in query:
            reply('Searching for ' + query.split('search')[1])
            url = 'https://google.com/search?q=' + query.split('search')[1]
            try:
                webbrowser.get().open(url)
                reply('This is what I found Sir')
            except:
                reply('Please check your Internet')

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            reply(f"Sir, the time is {strTime}")

        elif 'joke' in query:
            reply(pyjokes.get_joke(language="en", category="neutral"))
        
        elif 'tounge twister' in query:
            reply(pyjokes.get_joke(language="en", category="twister"))

        elif 'shutdown system' in query:
            reply("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
                 
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            reply("Recycle Bin Recycled")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif 'news' in query:
             
            try:
                jsonObj = urlopen('''https://newsapi.org/v2/top-headlines?country=us&apiKey=8582ca6f34a84c02a4ed53e9627f398a''')
                data = json.load(jsonObj)
                i = 1
                 
                reply('Here are some top news from all the coutires')
                print('''=============== NEWS HEADLINES ============'''+ '\n')
                 
                for item in data['articles']:
                    if i<=5:
                        print(item['description'] + '\n')
                        reply(str(i) + '. ' + item['title'] + '\n')
                        i += 1
            except Exception as e:
                 
                print(str(e))

        elif 'open notepad' in query:
            reply("File name")
            name = takeCommand()
            path = ('C:\Public\File'+name+'.txt')
            sp.Popen(['notepad.exe', path])
            file1 = open("exp.txt","w")
            reply("What do you want to write?")
            cont = takeCommand()
            file1.write(cont)
            file1.close()
            
            file1 = open("exp.txt",'rt')
            reply("Reading content of file")
            reply(file1.read())
            file1.close()

        elif 'email to' in query:
            reply("Enter your gmail host name")
            #time.sleep(8)
            hname = input()
            eid = (hname+'@gmail.com')
            reply("Enter your gmail password")
            #time.sleep(8)
            password = input()
            try:
                reply("Enter host name of receiver's gmail id")
                to = input()+"@gmail.com"
                reply("What should I say?")
                content = input()
                sendEmail(to, content,eid,password)
                reply("Email has been sent!")
            except Exception as e:
                print(e)
                reply("Sorry my friend. I am not able to send this email")
