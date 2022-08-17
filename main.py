import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import os
import pyjokes
import randfacts
from plyer import notification

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def printAndSpeak(printStr, speakStr):
    '''This function is used to print and speak at the same time instead of writing print and speak statements again and again.'''
    print(printStr)
    speak(speakStr)

def speak(audio):
    '''This function is usd to speak from the existing voices from the computer. It requires pyttsx3 module and some configurations'''
    engine.say(audio)
    engine.runAndWait()

def greet():

    '''This is the function where we greet the users according to the time. Like morning, afternoon and evening.'''
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        printAndSpeak("Good Morning!", "Good Morning!")

    elif hour >=12 and hour<18:
        printAndSpeak("Good Afternoon!", "Good Afternoon!")
    
    else:
        printAndSpeak("Good Evening!", "Good Evening!")

    printAndSpeak("I am Conical. A desktop AI for all users. How may i assist you?", "I am Conical. A desktop AI for all users. How may i assist you?")

def takeCommand():
    '''It takes microphone input from the user and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.energy_threshold = 200
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}\n")

    except Exception as e:
        #print(e)

        print("Speech not recognized...")

        return "None"
    return query

if __name__ == "__main__":
    greet()

    while True:
        query = takeCommand().lower()
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            printAndSpeak("Searching...", "Searching...")
            results = wikipedia.summary(query, sentences=3)
            printAndSpeak("According to Wikipedia...", "According to wikipedia")
            printAndSpeak(results, results)

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke(language = 'en', category='all')
            printAndSpeak(joke, joke)

        elif 'open youtube' in query:
            printAndSpeak("Bot: Opening youtube...", "Opening youtube...")
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            printAndSpeak("Bot: Opening google...", "Opening google...")
            webbrowser.open('google.com')

        elif 'open stack overflow' in query:
            printAndSpeak("Bot: Opening stackoverflow...", "Opening stackoverflow...")
            webbrowser.open('stackoverflow.com')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            printAndSpeak(f"Bot: Sir, The time is {strTime}", f"Sir, The time is {strTime}" )

        elif 'search' in query:
            try:
                printAndSpeak("What should I say?", "What should I say?")
                content = takeCommand()
                url  = 'https://google.com/search?q=' + content
                webbrowser.get().open(url)

            except Exception as e:
                print("sorry, but something went wrong")

        elif 'find location' in query:
            printAndSpeak("Where should I find?", "Where should I find?")
            location = takeCommand()
            url =  'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)


        elif 'tell me a fact' in query:
            fact = randfacts.getFact()
            printAndSpeak(fact, fact)

        elif 'conical quit' in query:
            printAndSpeak("Bot: Quitting sir, Thanks for your time!", "Quitting sir, Thanks for your time!")
            exit()
            
        