import speech_recognition as sr
import os
import webbrowser
import datetime
from selenium_web import *
from NewsApi import *
from JokesApi import *
from WeatherApi import *
import randfacts
import pytz

def say(text):
    os.system(f'say "{text}"')

def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            query = recognizer.recognize_google(audio, language='en-us')
            print(f'User : {query}')
            return query
        except Exception as e:
            print(f"Error: {e}")
            return ""

if __name__ == '__main__':
    say('Hello, I am your Voice Assistant. How can I help you?')
    while True:
        print('Listening...')
        query = takeCommand()

        if not query:
            continue

        if 'exit' in query.lower() or 'stop' in query.lower():
            say('Goodbye! Have a great day.')
            break

        if 'open' in query.lower():
            sites = [
                ['Youtube', 'https://www.youtube.com'],
                ['Google', 'https://www.google.com'],
                ['Wikipedia', 'https://www.wikipedia.com'],
                ['Facebook', 'https://www.facebook.com'],
                ['Twitter', 'https://www.twitter.com'],
                ['Instagram', 'https://www.instagram.com'],
                ['LinkedIn', 'https://www.linkedin.com'],
                ['Reddit', 'https://www.reddit.com'],
                ['Amazon', 'https://www.amazon.com'],
                ['Netflix', 'https://www.netflix.com']
            ]
            for site in sites:
                if f'open {site[0]}'.lower() in query.lower():
                    say(f'Opening {site[0]}')
                    webbrowser.open(site[1])
                    break
            else:
                say("Website not found in the list. Please try another.")

        elif 'play music' in query.lower():
            say('Playing Let her go by Passenger for you')
            musicPath = '/Users/fahmid/PycharmProjects/Let_her_go.mp3'
            os.system(f'open "{musicPath}"')

        elif 'date' in query.lower() or 'time' in query.lower():
            dhaka_tz = pytz.timezone('Asia/Dhaka')
            now = datetime.datetime.now(dhaka_tz)
            say(f"Today is {now.strftime('%d')} of {now.strftime('%B')} and it's currently {now.strftime('%I:%M %p')} in Dhaka,Bangladesh.")

        elif 'wikipedia' in query.lower():
            say('Tell me the topics you want to search for')
            try:
                text = takeCommand()
                say(f'Searching {text} on Wikipedia')
                assistant = Information()
                assistant.get_info(text)
            except Exception as e:
                say("Sorry Couldn't hear you")

        elif 'news' in query.lower():
            arr = news()
            say("Here's top 3 news for you")
            for i in range(len(arr)):
                print(arr[i])
                say(arr[i])

        elif 'fact' in query.lower() or 'facts' in query.lower():
            facts = randfacts.get_fact()
            say('Sure, Did you know that')
            print(facts)
            say(facts)

        elif 'joke' in query.lower() or 'jokes' in query.lower():
            jokes = joke()
            say('Sure, Get ready!')
            print(jokes[0])
            say(jokes[0])
            print(jokes[1])
            say(jokes[1])

        elif 'weather' in query.lower():
            say('Sure')
            say(f'The temperature in Dhaka is {temp()} degree celcius and with {des()}')
        else:
            say("Sorry I don't have information for that.")