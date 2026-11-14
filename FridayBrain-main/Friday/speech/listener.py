import speech_recognition as sr


class Listener:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("\n🎤 Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio)
            print(f"Boss: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry Boss, I didn't understand.")
            return ""
        except sr.RequestError:
            print("Speech recognition service is unavailable.")
            return ""