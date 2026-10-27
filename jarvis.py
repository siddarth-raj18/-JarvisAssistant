import subprocess
import webbrowser
from urllib.parse import quote_plus
import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 175)

# Assistant starts in standby mode
awake = False

def speak(message):
    print(f"JARVIS: {message}")
    engine.say(message)
    engine.runAndWait()

def perform_command(command):
    global awake

    command = command.lower().strip()
    print(f"You said: {command}")

    # Remove wake word from the command
    command = command.replace("jarvis", "", 1).strip(" ,.!?")

    # Wake up
    if command in ("wake up", "start listening", "are you there","yeddelu"):
        awake = True
        speak("I am awake. How can I help you?")
        return True

    # Sleep mode
    if command in ("sleep", "go to sleep", "standby"):
        awake = False
        speak("Going to sleep. Say Jarvis to wake me up.")
        return True

    # Stop the program
    if command in (
        "shutdown",
        "shut down",
        "exit",
        "quit",
        "stop jarvis",
        "terminate"
    ):
        speak("Shutting down. Goodbye!")
        return False

    # Ignore normal commands while asleep
    if not awake:
        speak("I am sleeping. Say Jarvis to wake me up.")
        return True

    # Website commands
    if command == "open chat gpt":
        webbrowser.open("https://chatgpt.com")
        speak("Opening ChatGPT.")

    elif command == "open youtube":
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")

    elif command == "open google":
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")

    # Google search
    elif command.startswith("search google for"):
        query = command[len("search google for"):].strip()

        if query:
            url = "https://www.google.com/search?q=" + quote_plus(query)
            webbrowser.open(url)
            speak(f"Searching Google for {query}.")
        else:
            speak("Please tell me what to search for.")

    # YouTube search
    elif command.startswith("search youtube for"):
        query = command[len("search youtube for"):].strip()

        if query:
            url = (
                "https://www.youtube.com/results?search_query="
                + quote_plus(query)
            )
            webbrowser.open(url)
            speak(f"Searching YouTube for {query}.")
        else:
            speak("Please tell me what to search for.")

    # Windows applications
    elif command == "open notepad":
        subprocess.Popen(["notepad.exe"])
        speak("Opening Notepad.")

    elif command == "open calculator":
        subprocess.Popen(["calc.exe"])
        speak("Opening Calculator.")

    else:
        speak("I do not know that command yet.")

    return True

def run_jarvis():
    global awake

    speak("Jarvis is running in standby mode. Say Jarvis to wake me up.")

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)

        while True:
            try:
                if awake:
                    print("\nListening for your command...")
                    speak("Listening for your command...")
                else:
                    print("\nStandby. Say Jarvis to wake up...")
                    speak("Standby. Say Jarvis to wake up...")

                audio = recognizer.listen(
                    source,
                    timeout=None,
                    phrase_time_limit=6
                )

                command = recognizer.recognize_google(
                    audio,
                    language="en-IN"
                ).lower().strip()

                print(f"You said: {command}")

                # In standby, only wake when Jarvis is detected
                if not awake:
                    if "jarvis" in command:
                        awake = True
                        command_after_wake_word = command.replace(
                            "jarvis", "", 1
                        ).strip(" ,.!?")
                        if command_after_wake_word:
                            if not perform_command(command):
                                break
                        else:
                            speak("I am awake. How can I help you?")
                    continue

                if not perform_command(command):
                    break

            except sr.UnknownValueError:
                print("Could not understand. Please try again.")
                speak("I could not understand. Please try again.")

            except sr.RequestError as error:
                print(f"Speech recognition error: {error}")
                speak("Speech recognition is unavailable.")
                break

            except OSError as error:
                print(f"Microphone error: {error}")
                speak("Please check your microphone.")
                break

if __name__ == "__main__":
    try:
        run_jarvis()
    except KeyboardInterrupt:
        print("\nJarvis stopped.")
