import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')# Window ek Api degi use aap inbuild voice hogi 
voices=engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("How can i help you?")
def takeCommand():
    r=sr.Recognizer()# it will recognizing the audio
    with sr.Microphone as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        # print(e)
        print("Say that again")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    # User id and password enter here
    server.login("youremail@gmail.com","password")
    server.sendmail('youremail@gmail.com',to,content)
    server.close()
if __name__ == "__main__":
    speak("Hello")
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for executing task based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query=query.replace("wikipedia"," ")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        # elif 'play music' in query:
        #     music_dir='D:\\Favourite song'
        #     songs=os.listdir(music_dir)
        #     print(songs)
        #    os.startfile(os.path.join(music_dir,songs[o]))
        elif 'time' in query:
            t1=datetime.datetime.now().t1("%H : %M : %S")
            speak(f"sir,time is {t1}")
        elif 'open code' in query:
            code="C:\\Users\\PCD\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code)
        elif 'email to Dhanraj' in query:
            try:
                speak('What should i say?')
                content=takeCommand()
                #to whom the mail is to be send email id to that person
                to='dhanrajyouremail@gmail.com'
                sendEmail(to,content)
                speak('Email has been send')
            except Exception as e:
                print(e)
                speak("Sorry your email is not send")
