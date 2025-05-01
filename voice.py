import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_voice_input(prompt="Speak now..."):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak(prompt)
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I did not understand.")
            return None
