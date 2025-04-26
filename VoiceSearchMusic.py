import webbrowser
import speech_recognition as sr
import pyttsx3
import urllib.parse
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def search_and_play_music(query):
    """Search for the music video and play it."""
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.youtube.com/results?search_query={encoded_query}"
    print(f"Searching for '{query}' on YouTube...")
    speak(f"Now searching for {query} on YouTube.")
    webbrowser.open(url)

def voice_command_search():
    """Listen for voice commands and execute the search."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Please say the name of the song or artist...")
        speak("Please say the name of the song or artist...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"You said: {query}")
        search_and_play_music(query)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio. Please try again.")
        speak("Sorry, I could not understand the audio. Please try again.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        speak("Could not request results from the service.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        speak("An unexpected error occurred.")

if __name__ == "__main__":
    try:
        while True:
            voice_command_search()
    except KeyboardInterrupt:
        print("Exiting the program. Goodbye!")
        speak("Exiting the program. Goodbye!")
