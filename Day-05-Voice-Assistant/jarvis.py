import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import wikipedia

# -------- TEXT TO SPEECH -------- #

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 130)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# -------- SPEECH TO TEXT -------- #

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source, timeout=20, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("Listening timeout")
            return ""

    try:
        print("Recognizing...")
        data = recognizer.recognize_google(audio)
        print("You said:", data)
        return data.lower()

    except sr.UnknownValueError:
        print("Not Understand")
        return ""

    except sr.RequestError:
        print("Network error")
        return ""


# -------- MAIN PROGRAM -------- #

if __name__ == '__main__':

    speak("Hello, I am Peter. Say hello Peter to activate me")

    while True:

        text = listen()

        if "hello peter" in text:

            speak("Yes, how can I help you")

            while True:

                command = listen()

                if command == "":
                    continue

                # NAME
                if "name" in command:
                    speak("My name is Peter")

                # AGE
                elif "age" in command or "old" in command:
                    speak("I do not have an age. I am an AI")

                # TIME
                elif "time" in command:
                    time = datetime.datetime.now().strftime("%I:%M %p")
                    speak("Current time is " + time)

                # YOUTUBE
                elif "youtube" in command:
                    speak("Opening YouTube")
                    webbrowser.open("https://www.youtube.com")

                # GOOGLE SEARCH
                elif "search" in command or "google" in command:
                    speak("What should I search on Google?")
                    search = listen()

                    if search != "":
                        webbrowser.open("https://www.google.com/search?q=" + search)
                        speak("Here are the search results")

                # WIKIPEDIA
                elif "wikipedia" in command:
                    speak("What topic should I search on Wikipedia?")
                    topic = listen()

                    if topic != "":
                        try:
                            result = wikipedia.summary(topic, sentences=2)
                            speak(result)
                        except:
                            speak("Sorry I could not find that")

                # JOKE
                elif "joke" in command:
                    joke = pyjokes.get_joke(language="en", category="neutral")
                    speak(joke)

                # STOP
                elif "stop" in command or "exit" in command:
                    speak("Goodbye")
                    exit()

                else:
                    speak("I did not understand that command")