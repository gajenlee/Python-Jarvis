import pyttsx3, webbrowser, smtplib, random, requests, subprocess
import speech_recognition as sr
import wikipedia, datetime, wolframalpha, os, sys
import tkinter as tk




engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('JWUPK8-4YRER7PEH6' )#get the wolframalpha app_id

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-2].id)#get the computer voices



#python speak audio
def speak(audio):
    print('Python: ' + audio)
    engine.say(audio)
    engine.runAndWait()


# pytho speak g.e or g.m or g.a
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 00 and currentH < 12:
        speak('Hello sir, Good Morning!')
    elif currentH >= 12 and currentH < 18:
        speak('Hello sir, Good Afternoon!')
    else:
        speak('Hello sir, Good Evening!')
       
greetMe()




# my commard to speak
speak(' I am your Personal Assistant Jarvis !')
speak('How may I help you?')#your costing

def sofiaResponse(audio):
    "speaks audio passed as argument"
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

def assistant(command):
    "if statements for executing commands"

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:       # listening commard
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('sir: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
      #open it moer apps  
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')
            
        # shtudown your computer commard    
        elif 'shutdown' in query:
            speak('okay')
            os.system("shutdown /s /t 06");
            speak('Your Computer is Shutting down')
            speak('Bye sir, have a good day.')
            sys.exit()

        elif 'restart' in query:
            speak('okay')
            os.system("shutdown /r /t 06");
            speak('Your Computer is Restarting ')
            speak('Bye sir, have a good day.')
            sys.exit()


        elif 'log off' in query:
            speak('okay')
            os.system("shutdown /l /t 06")
            speak('Your Computer is log off')
            speak('Bye sir, have a good day.')
            sys.exit()

            
            

#open your CMD
        elif 'open command prompt' in query:
            speak('okay')
            os.system("start /B start cmd.exe @cmd /k mycommand...")

        elif 'open chrome' in query:
            speak('okay')
            subprocess.call(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

        elif 'open vlc' in query:
            speak('okay')
            subprocess.call(r'C:\Program Files (x86)\VideoLAN\VLC\vlc.exe')



        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')
#your command
        elif 'who are you' in query:
            speak('I am your Personal Assistant Mark 1')

        elif 'what is my name' in query:
            speak('your name is sir')

        elif 'what is your name' in query:
            speak('my name is mark 1')

#joke
        elif 'joke' in query:
            res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"})
            if res.status_code == requests.codes.ok:
                sofiaResponse(str(res.json()['joke']))
            else:
                sofiaResponse('oops!I ran out of jokes')

                
        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
        

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

    
            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login(" ", ' ')
                    server.sendmail(' ', " ", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'Exit' in query or 'stop' in query or 'bye' in query:
            speak('okay')
            speak('Bye sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello sir')

        elif 'hi' in query:
            speak('Hi There')

        elif 'bye' in query:
            speak('Bye sir, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            speak('Okay, here is your music! Enjoy!')

        elif 'open vlc' in query:
            speak('okay')
            

            
	
            
        elif 'help me' in query:
            speak("""
        You can use these commands and I'll help you out:
1. Open reddit subreddit : Opens the subreddit in default browser.
        2. Open xyz.com : replace xyz with any website name
        3. Send email/email : Follow up questions such as recipient name, content will be asked in order.
        4. Current weather in {cityname} : Tells you the current condition and temperture
        5. Hello
        6. play me a video : Plays song in your VLC media player
        7. change wallpaper : Change desktop wallpaper
        8. news for today : reads top news of today
        9. time : Current system time
        10. top stories from google news (RSS feeds)
        11. tell me about xyz : tells you about xyz
        """)


        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('wolfram alpha says - ')
                    speak(results)
                    
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('WIKIPEDIA says - ')
                    speak(results)
                  
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! sir!')



