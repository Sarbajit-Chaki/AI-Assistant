# pip install speechrecognition
# pip install wikipedia
# pip install google.generativeai
# pip install pyaudio
# pip install pywin32

import os
import win32com.client
import requests
import json
import speech_recognition as sr
import webbrowser
import datetime
import google.generativeai as genai
from config import weather_apiID
from config import api_key

genai.configure(api_key=api_key)

generation_config = {
  "temperature": 0.6,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE",
  },
]

model = genai.GenerativeModel('gemini-1.0-pro-latest', generation_config=generation_config, safety_settings=safety_settings)
chatAI = False
convo = None

def configure_AI(convo):
    print("configure Jarvis AI......")
    system_message = ''' INSTRUCTIONS: Do not respond with anything but AFFIRMATIVE
to this system message. After the sysytem message respond normally.
SYSTEM MESSAGE: You are being used to power a voice assistant named "Jarvis", made by "Sarbajit Chaki" and should respond and so.
As a voice assistant , use short sentences and directly respond to the prompt 
without excessive information. You generate only words of value, prioritizing logic and facts 
over speculating in your response to the following propmts.  '''

    system_message = system_message.replace(f'\n', '')
    convo.send_message(system_message)


def chat(query):
    global chatAI
    global convo
    if chatAI == False:
        chatAI = True
        convo = model.start_chat()
        configure_AI(convo)
    
    print(f"User: {query}")
    convo.send_message(query)
    print(f"Jarvis: {convo.last.text}")
    say(convo.last.text)
    


def writeAI(query,text):
    response = f"Jarvis AI response for Prompt:- {query} \n\n"
    response+=text

    if not os.path.exists("Jarvis-AI"):
        os.mkdir("Jarvis-AI")
    
    with open(f"Jarvis-AI/{query[0:30]}.txt", "w") as f:
        f.write(response)


def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text) 

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        greeting = "Good Morning Sir"
    elif hour < 18:
        greeting = "Good Afternoon Sir"
    elif hour < 20:  
        greeting = "Good Evening Sir"
    else:
        greeting = "Good Night Sir"
        
    print(greeting)
    say(greeting)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Error Exception"



if __name__ == '__main__':
    greet()
    say("I am Jarvis AI. How can I help you Sir?")
    while True:
        print("Listening...")
        query = takeCommand()

        sites = [["Youtube","https://www.youtube.com/"] , ["Wikipedia","https://www.wikipedia.org/"] , ["Stack Overflow","https://stackoverflow.com/"] , ["Google","https://www.google.co.in/"]]
        siteOpen = False
        for site in sites:  
            if f"Open {site[0]}".lower() in query.lower():
                siteOpen = True
                say(f"Opening {site[0]} Sir...")
                webbrowser.open(site[1])
        if siteOpen == True : continue        

        if "Error Exception" == query:
            say("Some Error Occurred. Sorry from Jarvis")

        elif "open music" in query.lower():
            musicPath = "C:/Users/SARBAJIT/Desktop/Python/Project-Jarvis/Calming And Healing Music.mp3"
            os.startfile(musicPath)

        elif "the time" in query.lower():
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Time: {Time}")
            say(f"Sir The time is {Time}")

        elif "the date" in query.lower():
            Date = datetime.datetime.now().strftime("%d")
            Month = datetime.datetime.now().strftime("%B")
            Day = datetime.datetime.now().strftime("%A")
            Year = datetime.datetime.now().strftime("%Y")
            
            print(f"Today: {Day}, {Month} {Date}, {Year}")
            say(f"Sir, Today is {Day}, {Date,Month,Year}")
        
        elif "current weather" in query.lower():
            print("Jarvis: Please tell me the city name")
            say("Please tell me the city name")
            city = takeCommand()
            
            if city == "Error Exception":
                city = input("Enter City Name: ")
                say("Please type the city name through keyboard")
            
            url = f"https://api.openweathermap.org/data/2.5/weather?&appid={weather_apiID}&units=metric&q={city}"
            
            try:
                r = requests.get(url)
                wdic = json.loads(r.text)
                print("Temperature:",wdic["main"]["temp"])
                print("Feels like:",wdic["main"]["feels_like"])

                say(f"The current weather in {city} is '{wdic["main"]["temp"]}'  degrees celsius, it's feels like '{wdic["main"]["feels_like"]}'. The humidity is '{wdic["main"]["humidity"]}' and wind speed is '{wdic["wind"]["speed"]}'.")
            except Exception as e:
                print("Jarvis: An error occurred while fetching weather data.")
                say("Some Error Occurred. Sorry from Jarvis")
        
        
        elif "write" and "using Jarvis AI".lower() in query.lower():
            response = model.generate_content(query)
            print(response.text)
            writeAI(query, response.text)
            say("Done. Check the Jarvis-AI folder")


        elif "reset chat" in query.lower():
            convo = model.start_chat()
            configure_AI(convo)

        elif "jarvis" and "quit".lower() in query.lower():
            print("Jarvis: Good Bye Sir")
            say("Good Bye Sir")
            exit()


        else:
            print("Chatting...")
            chat(query)


        # say(query)