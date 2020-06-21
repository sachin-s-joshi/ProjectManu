import pyttsx3
import speech_recognition as sr
from datetime import datetime
from weather import returnResponse, returnForCountries
import asyncio
import time


def tell(*asOrder):
    engine = pyttsx3.init()
    engine.setProperty('language', 'hi')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[33].id)
    engine.setProperty('rate', 170)
    for order in asOrder:
        engine.say(order)
    engine.runAndWait()


def mic():

    try:
        s = sr.Recognizer()
        with sr.Microphone() as src:
            print("I am Listening..")
            # s.pause_threshold = 1
            audio = s.listen(src, timeout=2)
        print('Recognizing...')
        quest = s.recognize_google(audio, language='en-in')
        print('Query:', quest)

    except Exception as identifier:
        print(identifier)
        tell('Sorry.I didn\'t hear back')
        quest = 'none'
    return quest


def current_time():
    date = datetime.now()
    time = date.strftime("%H:%M:%S")
    dt = date.strftime("%d/%m/%Y")
    tell(dt, time)


def myName(name='Shital'):
    tell(
        'My name is {0}, I can do wonderful things as your artificial assistant'.format(name))


def urName():
    tell(f'your name is Sachin Joshi. You are my Founder')


def CovidCases(state):
    tell('I am getting the details for {0}'.format(state))
    res = asyncio.run(returnResponse(state))
    print(res)
    print('There are {0} number of Confirmed Case of which {1} are recovered and {2} number of people have died'.format(
        res[0], res[1], res[2]))
    tell('There are {0} number of Confirmed Case of which {1} are recovered and {2} number of people have died'.format(
        res[0], res[1], res[2]))


def CovidCasesCountryWise(country):
    tell('I am getting the details for {0}'.format(country))
    res = asyncio.run(returnForCountries(country))
    print(res)
    if(type(res) is tuple):
        print('There are {0} number of Confirmed Case of which {1} are recovered and {2} number of people have died'.format(
            res[0], res[1], res[2]))
        tell('There are {0} number of Confirmed Case of which {1} are recovered and {2} number of people have died'.format(
            res[0], res[1], res[2]))
    else:
        tell(res)


if __name__ == "__main__":
    tell('Hi,Welcome back.')
    name = 'Manu'
    while True:
        tell('Please tell me how can I help?')
        query = mic()
        if 'your name' in query:
            myName(name)
            tell('Do you want me to call by other name?')
            q = mic()
            if q == 'yes':
                tell('What would you like to call me by?')
                q = mic()
                name = q
                myName(name)

        elif 'my name' in query:
            urName()
        elif 'date' in query or 'time' in query:
            current_time()
        elif 'corona in India' in query or 'India' in query:
            while True:
                tell('Sure,can you tell me which state?')
                que = mic()
                if que != 'none':
                    CovidCases(que)
                tell('Do you want to try some other states as well (yes or no)?')
                q = mic()
                if q.lower() == 'no':
                    break
        elif 'across world' in query:
            while True:
                tell('Sure,can you tell me which country?')
                que = mic()
                CovidCasesCountryWise(que)
                tell('Do you want to know some other countries as well (yes or no)?')
                q = mic()
                if q.lower() == 'no':
                    break
        elif 'quit' in query:
            quit()
        else:
            continue
