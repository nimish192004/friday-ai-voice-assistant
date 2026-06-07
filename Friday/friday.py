import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import shlex
import random
import pyautogui
import pyjokes



def speak(audio) -> None:
    os.system(f'say "{audio}"')


def time() -> None:
    """Tells the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    speak("The current time is")
    speak(current_time)
    print("The current time is", current_time)


def date() -> None:
    """Tells the current date."""
    now = datetime.datetime.now()
    speak("The current date is")
    speak(f"{now.day} {now.strftime('%B')} {now.year}")
    print(f"The current date is {now.day}/{now.month}/{now.year}")


def wishme() -> None:
    """Greets the user based on the time of day."""
    speak("Welcome back, sir!")
    print("Welcome back, sir!")

    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good morning!")
        print("Good morning!")
    elif 12 <= hour < 16:
        speak("Good afternoon!")
        print("Good afternoon!")
    elif 16 <= hour < 24:
        speak("Good evening!")
        print("Good evening!")
    else:
        speak("Good night, see you tomorrow.")

    assistant_name = load_name()
    speak(f"{assistant_name} at your service. Please tell me how may I assist you.")
    print(f"{assistant_name} at your service. Please tell me how may I assist you.")


def screenshot() -> None:
    """Takes a screenshot and saves it."""
    img = pyautogui.screenshot()
    img_path = os.path.join(os.path.expanduser("~"), "Pictures", "screenshot.png")
    img.save(img_path)
    speak(f"Screenshot saved as {img_path}.")
    print(f"Screenshot saved as {img_path}.")

def takecommand() -> str:
    """Takes microphone input from the user and returns it as text."""
    r = sr.Recognizer()
    try:
        mic_names = sr.Microphone.list_microphone_names()
        print("Available microphones:", mic_names)
    except Exception as e:
        print("Could not list microphones:", type(e).__name__, e)
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.dynamic_energy_threshold = True
        r.energy_threshold = 300
        r.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=7)
            print("Audio captured, processing...")
        except sr.WaitTimeoutError:
            speak("Timeout occurred. Please try again.")
            return None

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("Recognized query:", query)
        print(query)
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        print("Recognition failed: unknown value")
        return None
    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        print("Recognition failed: request error")
        return None
    except Exception as e:
        speak(f"An error occurred: {e}")
        print(f"Error: {e}")
        return None

def play_music(song_name=None) -> None:
    """Plays music from the user's Music directory."""
    song_dir = os.path.join(os.path.expanduser("~"), "Music")
    try:
        songs = os.listdir(song_dir)
    except FileNotFoundError:
        songs = []

    if song_name:
        songs = [song for song in songs if song_name.lower() in song.lower()]

    if songs:
        song = random.choice(songs)
        song_path = os.path.join(song_dir, song)
        if hasattr(os, "startfile"):
            os.startfile(song_path)
        else:
            if os.name == "posix":
                os.system(f"open {shlex.quote(song_path)}")
            else:
                os.system(f"start {shlex.quote(song_path)}")
        speak(f"Playing {song}.")
        print(f"Playing {song}.")
    else:
        speak("No song found.")
        print("No song found.")

def set_name() -> None:
    """Sets a new name for the assistant."""
    speak("What would you like to name me?")
    name = takecommand()
    if name:
        with open("assistant_name.txt", "w") as file:
            file.write(name)
        speak(f"Alright, I will be called {name} from now on.")
    else:
        speak("Sorry, I couldn't catch that.")

def load_name():
    """Loads the assistant name from a file, defaulting to Friday."""
    default_name = "Friday"
    try:
        with open("assistant_name.txt", "r") as file:
            name = file.read().strip()
            return name if name else default_name
    except FileNotFoundError:
        return default_name

def search_wikipedia(query):
    """Searches Wikipedia and returns a summary."""
    try:
        speak("Searching Wikipedia...")
        result = wikipedia.summary(query, sentences=2)
        speak(result)
        print(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("Multiple results found. Please be more specific.")
    except Exception:
        speak("I couldn't find anything on Wikipedia.")


if __name__ == "__main__":
    wishme()

    while True:
        query = takecommand()
        if not query:
            continue

        if "hi friday" in query or "hello" in query:
            speak("Hello Nimish, how can I help you?")
        elif "how are you" in query or "how are" in query:
            speak("I am doing great. Thank you for asking.")
        elif "your name" in query:
            speak("My name is Friday.")

        elif "facetime" in query:
            if os.name == "posix":
                os.system('open -a "FaceTime"')
            else:
                speak("FaceTime launch is only supported on macOS.")
        elif "date" in query:
            date()
        elif "time" in query:
            if "facetime" not in query:
                time()

        elif "wikipedia" in query:
            query = query.replace("wikipedia", "").strip()
            search_wikipedia(query)

        elif "play music" in query:
            song_name = query.replace("play music", "").strip()
            play_music(song_name)

        elif "open youtube" in query:
            wb.open("youtube.com")

        elif "open chrome" in query or "open google" in query or "google" in query:
            if os.name == "posix":
                os.system('open -a "Google Chrome" "https://google.com"')
            else:
                wb.open("https://google.com")

        elif "open music" in query or "music" in query:
            if os.name == "posix":
                os.system('open -a "Music"')
            else:
                speak("Music launch is only supported on macOS.")

        elif "open settings" in query or "settings" in query:
            if os.name == "posix":
                # macOS Ventura+ uses System Settings; older versions use System Preferences
                if os.system('open -Ra "System Settings"') == 0:
                    os.system('open -a "System Settings"')
                else:
                    os.system('open -a "System Preferences"')
            else:
                speak("Settings launch is only supported on macOS.")

        elif "open word" in query or "open ms word" in query or "microsoft word" in query:
            if os.name == "posix":
                os.system('open -a "Microsoft Word"')
            else:
                speak("Microsoft Word launch is only supported on macOS.")

        elif "open photos" in query or "photos" in query:
            if os.name == "posix":
                os.system('open -a "Photos"')
            else:
                speak("Photos launch is only supported on macOS.")

        elif "open safari" in query or "safari" in query:
            if os.name == "posix":
                os.system('open -a "Safari"')
            else:
                wb.open("https://www.apple.com/safari/")

        elif "open facetime" in query or "facetime" in query:
            if os.name == "posix":
                os.system('open -a "FaceTime"')
            else:
                speak("FaceTime launch is only supported on macOS.")

        elif "open whatsapp" in query or "whatsapp" in query:
            if os.name == "posix":
                os.system('open -a "WhatsApp"')
            else:
                speak("WhatsApp launch is only supported on macOS.")

        elif "change your name" in query:
            set_name()
        elif "rename" in query and "you" in query:
            set_name()

        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")
        elif "take screenshot" in query or "take a screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)
        elif "joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)

        elif "shutdown" in query:
            speak("Shutting down the system, goodbye!")
            os.system("shutdown /s /f /t 1")
            break
        elif "turn off" in query or "power off" in query:
            speak("Shutting down the system, goodbye!")
            os.system("shutdown /s /f /t 1")
            break
            
        elif "restart" in query:
            speak("Restarting the system, please wait!")
            os.system("shutdown /r /f /t 1")
            break
        elif "reboot" in query:
            speak("Restarting the system, please wait!")
            os.system("shutdown /r /f /t 1")
            break
            
        elif "offline" in query or "exit" in query:
            speak("Going offline. Have a good day!")
            break
        elif "quit" in query or "stop" in query or "bye" in query:
            speak("Going offline. Have a good day!")
            break
        else:
            speak("Sorry, I didn't recognize that command. Please say one of the supported commands.")
            print("Unknown command:", query)
