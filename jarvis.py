import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import pywhatkit



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voice')
engine.setProperty('voice',voices[0])
engine.setProperty('rate',150)





def speak(text):
    print(f"Jarvis : {text}")
    engine.say(text)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try :
        print("Recogizing...")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print("Say that agian....")

    return query

def wishme():
    time = datetime.datetime.now().hour
    if time >0 and time <12:
        speak("Good Morning Sir.")

    elif time >12 and time<15:
        speak("Good Afternoon")
    else:
        speak("Good evening.")
    speak("Hello I am Jarvis How can i help you")


def current_time():
    time = datetime.datetime.now().strftime("%I %M %p")
    speak(f"The current time is {time[1:]}")



if __name__ == "__main__":

    wishme()
    while True:
        query = take_command().lower()

        if "time" in query:
            current_time()

        elif "open google" in query:
            speak("Opening google")
            webbrowser.open("google.com")
        elif "open youtube" in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
        elif "who is" in query or "wikipedia" in query:
            query = query.replace("who is","")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            summery = wikipedia.summary(query,sentences = 2)
            speak(summery)
        elif "play" in query:
            query = query.replace("play","")
            query = query.replace("youtube","")
            query = query.replace("jarvis","")
            pywhatkit.playonyt(query)
        elif "insult" in query:
            query = query.replace("insult","")
            query = query.replace("jarvis","")

            speak(f"{query}, you are a fool")
            
            






    