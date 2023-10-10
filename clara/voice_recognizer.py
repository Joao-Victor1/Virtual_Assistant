import speech_recognition as sr

class VoiceRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
    
    def recognize_speech(self):
        with sr.Microphone() as source:
            try:
                audio = self.recognizer.listen(source)
                user_input = self.recognizer.recognize_google(audio, language="pt-BR").lower()
                return user_input
            
            except sr.UnknownValueError:
                print("Desculpe, não consegui entender o que você disse.")
                return ""
            
            except sr.RequestError:
                print("Erro na solicitação. Verifique sua conexão com a internet.")
                return ""