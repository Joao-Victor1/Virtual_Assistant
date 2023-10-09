import speech_recognition as sr

class VoiceRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
    
    def recognize_speech(self):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)

        try:
            user_input = self.recognizer.recognize_google(audio, language="pt-BR").lower()
            return user_input
        
        except sr.UnknownValueError:
            return ""