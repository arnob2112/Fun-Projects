import speech_recognition as sr
import datetime
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes


listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)
run_app = True


def talk(text):
    alexa.say(text)
    alexa.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk("How can I help you?")
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("// " + command)
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except Exception as e:
        print("exception: ", e)

    return command


def run_alexa():
    command = take_command()

    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print("Current time is " + time)
        talk("Current time is " + time)
    elif "play" in command:
        song = command.replace("play", "")
        talk("playing " + song)
        pywhatkit.playonyt(song)
    elif "tell me about" in command:
        look_for = command.replace("tell me about", "")
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    elif "search" in command:
        look_for = command.replace("search", "")
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif "stop" == command:
        global run_app
        run_app = False
        print("stopped")
    else:
        talk("Sorry, I didn't understand you. But I am going to search for you.")
        pywhatkit.search(command)


while run_app:
    run_alexa()
