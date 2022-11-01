from tkinter import *
import cv2
import PIL.Image, PIL.ImageTk
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import roman
import requests
import win32com.client
from bs4 import BeautifulSoup
from PIL import Image
from email.message import EmailMessage
listener = sr.Recognizer()
engine = pyttsx3.init()



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
   
def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                info = listener.recognize_google(voice)
                print(info)
                return info.lower()

    except:
        pass


def send_email(receiver, subject, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('pythonproject91@gmail.com', 'ehrzmqijajvpueni')
        email = EmailMessage()
        email['From'] = 'pythonproject91@gmail.com'
        email['To'] = receiver
        email['Subject'] = subject
        email.set_content(message)
        server.send_message(email)

email_list = {
    'samreen': 'samreenkazi17@gmail.com',
    'arsheen': 'arsheenkazi@gmail.com',
    'carl': 'carlj2619@gmail.com',
    'leon': 'ddsouza3112@gmail.com',
}


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set("Good Morning Samreen")
        window.update()
        speak("Good Morning Samreen!")
    elif hour >= 12 and hour <= 18:
        var.set("Good Afternoon Samreen!")
        window.update()
        speak("Good Afternoon Samreen!")
    else:
        var.set("Good Evening Samreen")
        window.update()
        speak("Good Evening Samreen!")
    speak("Hey this is Rodricks! How may I help you miss")
   
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "None"
    var1.set(query)
    window.update()
    return query

def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'orange')
    wishme()
    while True:
        btn1.configure(bg = 'orange')
        query = takeCommand().lower()
        if 'bye' in query:
            var.set("Bye Miss")
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Bye Miss")
            break

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    var.set(results)
                    window.update()
                    speak(results)
                except Exception as e:
                    var.set('sorry miss could not find any results')
                    window.update()
                    speak('sorry miss could not find any results')

        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            var.set('opening google')

            window.update()
            speak('opening google')
            webbrowser.open("google.com")
           
        elif 'open gmail' in query:
            var.set('opening gmail')
            window.update()
            speak('opening gmail')
            webbrowser.open("gmail.com")
           
        elif 'open yahoo' in query:
            var.set('opening yahoo')
            window.update()
            speak('opening yahoo')
            webbrowser.open("yahoo.com")
       
        elif 'hello' in query:
            var.set('Hello Miss')
            window.update()
            speak("Hello Miss")
           
       
        elif ('play music' in query) or ('change music' in query):
            var.set('Here are your favorites')
            window.update()
            speak('Here are your favorites')
            music_dir = 'C:/Users/samre/Music/rosp' # Enter the Path of Music Library
            songs = os.listdir(music_dir)
            n = random.randint(0,6)
            os.startfile(os.path.join(music_dir, songs[n]))
           

        elif 'what is the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Miss the time is %s" % strtime)
            window.update()
            speak("Miss the time is %s" %strtime)

        elif 'what is the date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Miss today's date is %s" %strdate)
            window.update()
            speak("Miss today's date is %s" %strdate)

        elif 'thank you' in query:
            var.set("Welcome Miss")
            window.update()
            speak("Welcome Miss")

        elif 'what can you do for me' in query:
            var.set('I can do multiple tasks for you miss. tell me whatever you want to perform miss')
            window.update()
            speak('I can do multiple tasks for you miss. tell me whatever you want to perform miss')

        elif 'how old are you' in query:
            var.set("I am a little baby miss")
            window.update()
            speak("I am a little baby miss")

        elif 'what is your name' in query:
            var.set(" Hey everyone I am Rodricks")
            window.update()
            speak('Hey everyone I am Rodricks')
           
        elif 'say hello' in query:
            var.set('Hello Everyone! I am Rodricks')
            window.update()
            speak('Hello Everyone! I am Rodricks')

        elif 'open chrome' in query:
            var.set("Opening Google Chrome")
            window.update()
            speak("Opening Google Chrome")
            path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
           
        elif 'click photo' in query:
            stream = cv2.VideoCapture(0)
            grabbed, frame = stream.read()
            if grabbed:
                cv2.imshow('pic', frame)
                cv2.imwrite('pic.jpg',frame)
            stream.release()
           
        elif 'record video' in query:
            cap = cv2.VideoCapture(0)
            out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret:
                   
                    out.write(frame)

                    cv2.imshow('frame',frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break
            cap.release()
            out.release()
            cv2.destroyAllWindows()
           
           
        elif 'send email' in query:
            def get_email_info():
                var.set('To Whom you want to send email')
                window.update()
                talk('To Whom you want to send email')
                name = get_info()
                receiver = email_list[name]
                print(receiver)
                var.set('What is the subject of your email?')
                window.update()
                talk('What is the subject of your email?')
                subject = get_info()
                var.set('Tell me the body in your email')
                window.update()
                talk('Tell me the body in your email')
                message = get_info()
                send_email(receiver, subject, message)
                var.set('Email has been sent!')
                window.update()
                speak('Email has been sent!')
            get_email_info()

def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('Rodricks')

label = Label(window, width = 500, height = 500)
label.pack()
window.after(0, update, 0)

btn0 = Button(text = 'WISH ME',width = 20, command = wishme, bg = '#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text = 'SPEAK',width = 20,command = play, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()


window.mainloop()
