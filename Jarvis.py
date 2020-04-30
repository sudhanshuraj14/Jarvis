import pyttsx3
import alsaaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests
import googlemaps
from cv2 import cv2
from newsapi import NewsApiClient
import goslate

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[16].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")

    elif hour>=12 and hour<18:    
        speak("Good Afternoon sir")

    else:
        speak("Good Evening sir")

    speak("Jarvis at your service, let me know if there's anything I can help you with")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Order Recognizing...")
        speak("Order recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print(e)
        print("Sorry Sir but I didn't heared it clearly, will You please repeat..")
        speak("Sorry Sir but I didn't heared it clearly, will You please repeat..") 
        return "None"
    return query
        
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your Gmail Account', 'Your Password')
    server.sendmail('Your Gmail Account', to, content)
    server.close()
if __name__ == "__main__":
    wish()
    while True:
        query=takecommand().lower()    
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'who are you' in query:
            speak("My name is Jarvis and I'm an artificial Intelligence program. Working on the memory capacity of five terabyte, with the gpu clock speed of three gigahrtz, I love to learn new things and its my dream to become the most advance and usefull software in future for the sake human kind")

        elif 'how are you' in query:
            print("I am fine sir")
            speak("I am fine sir")

        elif 'thank you' in query:
            print("It's my pleasure sir.")
            speak("It's my pleasure sir.")

        elif 'do you have friends' in query:
            print("Yeah I have two friends Google and Siri, Do you wana know something about them")
            speak("Yeah I have two friends Google and Siri, Do you wana know something about them")
            b = takecommand()
            if b == 'yes':
                print("About whome you wana know? Google or Siri")
                speak("About whome you wana know? Google or Siri")
                x = takecommand()
                if x == 'Google':
                    print("Google Assistant is an artificial intelligence-powered virtual assistant developed by Google that is primarily available on mobile and smart home devices. Unlike the company's previous virtual assistant, Now the Google Assistant can engage in two-way conversations")
                    print("Users primarily interact with the Google Assistant through natural voice, though keyboard input is also supported. In the same nature and manner as Google Now, the Assistant is able to search the Internet, schedule events and alarms, adjust hardware settings on the user's device, and show information from the user's Google account. Google has also announced that the Assistant will be able to identify objects and gather visual information through the device's camera, and support purchasing products and sending money, as well as identifying songs")
                    speak("Google Assistant is an artificial intelligence-powered virtual assistant developed by Google that is primarily available on mobile and smart home devices. Unlike the company's previous virtual assistant, Now the Google Assistant can engage in two-way conversations")
                    speak("Users primarily interact with the Google Assistant through natural voice, though keyboard input is also supported. In the same nature and manner as Google Now, the Assistant is able to search the Internet, schedule events and alarms, adjust hardware settings on the user's device, and show information from the user's Google account. Google has also announced that the Assistant will be able to identify objects and gather visual information through the device's camera, and support purchasing products and sending money, as well as identifying songs")
                if x == 'Siri':
                    print("Siri is a virtual assistant that is part of Apple Inc.'s iOS, iPadOS, watchOS, macOS, and tvOS operating systems. The assistant uses voice queries and a natural-language user interface to answer questions, make recommendations, and perform actions by delegating requests to a set of Internet services. The software adapts to users' individual language usages, searches, and preferences, with continuing use")
                    print("Siri supports a wide range of user commands, including performing phone actions, checking basic information, scheduling events and reminders, handling device settings, searching the Internet, navigating areas, finding information on entertainment, and is able to engage with iOS-integrated apps")
                    speak("Siri is a virtual assistant that is part of Apple Inc.'s iOS, iPadOS, watchOS, macOS, and tvOS operating systems. The assistant uses voice queries and a natural-language user interface to answer questions, make recommendations, and perform actions by delegating requests to a set of Internet services. The software adapts to users' individual language usages, searches, and preferences, with continuing use")
                    speak("Siri supports a wide range of user commands, including performing phone actions, checking basic information, scheduling events and reminders, handling device settings, searching the Internet, navigating areas, finding information on entertainment, and is able to engage with iOS-integrated apps")

        elif 'open calculator' in query:
            speak("Opening Calculator")
            speak("Please provide the first digit: ")
            num1 = takecommand()
            speak("Please provide the second digit: ")
            num2 = takecommand()
            speak(f"The two numbers are: {num1},{num2}")
            speak("Please specify what Operation do you want to perform?")
            speak("add, subtarct, multiply, divide")
            choice = takecommand()
            if choice == 'add':
                x= int(num1) + int(num2)
                speak(f"Addition of these two numbers are:{x}")

            if choice == 'subtract':
                x= int(num1) - int(num2)
                speak(f"Addition of these two numbers are:{x}")

            if choice == 'multiply':
                x= int(num1) * int(num2)
                speak(f"Addition of these two numbers are:{x}")

            if choice == 'divide':
                x= int(num1) / int(num2)
                speak(f"Addition of these two numbers are:{x}")

        elif 'open maps' in query:
            gmaps = googlemaps.Client(key='Your Google Maps API Key')
            geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
            reevrse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
            now = datetime.datetime.now()
            direction_result = gmaps.directions("Sydney Town Hall","Parramatta, NSW",mode="transit",departure_time=now)
            print(direction_result)
            
        elif 'open google' in query:
            speak("Opening Google..")
            webbrowser.open_new_tab("google.com")

        elif 'open youtube' in query:
            speak("Opening You tube..")
            webbrowser.open_new_tab("youtube.com")
            
        elif 'search' in query:
            speak("What do you want to search sir?")
            find = takecommand()
            speak(f"Searching for {find}")
            webbrowser.open_new_tab(find)

        elif 'open translator' in query:
            print("Opening translator..")
            speak("Opening translator..")
            speak("Please specify either English to other language or other language to english")
            q = takecommand()
            if q == 'English to other':
                print("Please provide an input to translate")
                speak("Please provide an input to translate")
                text = takecommand()
                gs = goslate.Goslate()
                speak("Please specify in which language you want to translate")
                name1 = input("Please specify in which language you want to translate: ")
                p = (gs.translate(text, name1))
                print(f"{name1} translation of {text} is: {p}")
                speak(f"{name1} translation of {text} is: {p}")

            if q == 'other to English':
                print("How do you wana give the input? Vocally or by Keyboard")
                speak("How do you wana give the input? Vocally or by Keyboard")
                k = takecommand()
                if k == 'Keyboard':
                    text = input("Please provide an input to translate: ") 
                    gs = goslate.Goslate()
                    lang_id = gs.detect(text)
                    lang_type = gs.get_languages()[lang_id]
                    print(f"Input language is in {lang_type} language")
                    speak(f"Input language is in {lang_type} language")
                    p = (gs.translate(text, 'en'))
                    print(f"English translation of {text} is: {p}")
                    speak(f"English translation of {text} is: {p}")
                if k == 'Vocally':
                    print("Please provide an input to translate")
                    speak("Please provide an input to translate")
                    text = takecommand()
                    gs = goslate.Goslate()
                    lang_id = gs.detect(text)
                    lang_type = gs.get_languages()[lang_id]
                    print(f"Input language is in {lang_type} language")
                    speak(f"Input language is in {lang_type} language")
                    p = (gs.translate(text, 'en'))
                    print(f"English translation of {text} is: {p}")
                    speak(f"English translation of {text} is: {p}")

        elif 'play music' in query:
            music_dir= 'Path of the directory/file'
            songs = os.listdir(music_dir)
            print(songs)
            speak("Playing Music")
            os.system(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            print(time)
            speak(f" Sir, The Time is {time}\n")

        elif 'webcam' in query:
            speak("Opening Webcam")
            vid_capture = cv2.VideoCapture(0)
            vid_cod = cv2.VideoWriter_fourcc(*'XVID')
            output = cv2.VideoWriter("cam_video.avi", vid_cod, 20.0, (640,480))
            while True:
                ret, frame = vid_capture.read()
                cv2.imshow("My cam video", frame)
                output.write(frame)
                if cv2.waitKey(1) &0XFF == ord('x'):
                    break
            vid_capture.release()
            output.release()
            cv2.destroyAllWindows()

        elif 'create file' in query:
            f = open("New","w+")
            speak("File Creation successfull..")
            speak("Please tell the contents to write in file sir!")
            notes = takecommand()
            f.write(f"Contents are: {notes}")
            speak("File writing completed..")
            f.close()

        elif 'edit file' in query:
            speak("What's the name of file sir?")
            data = takecommand()
            f = open(data,"a+")
            speak("File opened succesfully")
            speak("Please tell the contents to write in file sir!")
            note = takecommand()
            f.write(f"{note}")
            speak("Editing completed succesfully!")
            f.close()

        elif 'read file' in query:
            speak("Please provide name of the file sir")
            read = takecommand()
            f = open(read, "r")
            speak("File opened succesfully and the contents are")
            if f.mode == 'r':
                contents = f.read()
                print(contents)
                speak(contents)

        elif 'delete file' in query:
            speak("Please provide name of the file sir!")
            name = takecommand()
            os.remove(name)
            speak("File removed succesfully")

        elif 'weather update' in query:
            speak("Which city sir??")
            info = takecommand()
            city = info
            api_address = 'http://api.openweathermap.org/data/2.5/weather?appid='Your Openweathermap API KEY'&q='
            url = api_address + city
            json_data = requests.get(url).json()
            print(json_data)
            speak(json_data)

        elif 'news update' in query:
            newsapi = NewsApiClient(api_key='Your NEWS API KEY')
            speak("Please specify any topic")
            src = takecommand()
            speak(f"The news headlines of {src} are")
            headlines = newsapi.get_top_headlines(q=src, sources='the-times-of-india, the-hindu', language='en')
            print(headlines)
            speak(headlines)
            sources = newsapi.get_sources()
            speak("Should I read the whole news? yes or no")
            say = takecommand()
            if say == 'yes':
                speak(f"The news update about {src} are")
                article = newsapi.get_everything(q=src, sources='the-times-of-india, the-hindu', domains='timesofindia.com, thehindu.com', language='en', sort_by='relevancy')
                print(article)
                speak(article)
                sources = newsapi.get_sources()
                speak(f"Thats all about {src} todays news update")
            else:
                speak(f"Thats all about {src} headlines")

        elif 'send email' in query:
            try:
                speak("What should I say??")
                content = takecommand()
                to = "Recievers Email Address"
                sendEmail(to, content)
                print("Email has been sent to respective email address Sir")
                speak("Email has been sent to respective email address Sir")
            except Exception as e:
                print(e)
                speak("Sorry sir but I'm not able to send the mail..")