# Link to GitHub: https://github.com/reybahl/Assistant/blob/master/main.py


from intentclassification.intent_classification import IntentClassifier
from assistantfunctions.weather import get_weather
import pyttsx3
import speech_recognition as sr

class Assistant:
        def __init__(self, name):
            self.name = name # Create instance variable name
            self.speech_engine = pyttsx3.init()
            self.speech_engine.setProperty("rate", 150)
            self.sr = sr.Recognizer()
            self.mic = sr.Microphone(device_index=0)


        def say(self, text):
            self.speech_engine.say(text)
            self.speech_engine.runAndWait()

        def reply(self, text):
            intent = intentclassifier.predict(text)
            
            replies = {
                
                'weather' : get_weather
                }

            reply_func = replies[intent]

            if callable(reply_func):
                self.say(reply_func())

        def listen(self):
            with self.mic as source:
                print("listening")
                audio = self.r.listen(source, timeout = 7, phrase_time_limit = 10)
            
            return self.r.recognize_google(audio)

        def main(self):
            while True:
                said = self.listen()
                self.reply(said)

        
            
        
intentclassifier = IntentClassifier()
assistant = Assistant("Assistant") # Create an instance and name it "Assistant"
assistant.main()
