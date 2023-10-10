from clara.assistant import ClaraAssistant
from clara.voice_recognizer import VoiceRecognizer
from clara.audio_player import AudioPlayer
from clara.nlp_processor import NLPProcessor

class Main:
    def __init__(self):
        self.assistant = ClaraAssistant()
        self.voice_recognizer = VoiceRecognizer()
        self.audio_player = AudioPlayer("audios")
        self.nlp_processor = NLPProcessor()
    
    def initialize_assistant(self):
        while True:
            user_input = self.voice_recognizer.recognize_speech()

            self.assistant.check_wake_word(user_input)

            if self.assistant.woken_up:
                if "clara" in user_input:
                    greeting = self.assistant.start()
                    if greeting:
                        print("C.L.A.R.A", greeting)
                        self.audio_player.say_response(greeting)

                if "tchau" in user_input:
                    farewell = self.assistant.end()
                    if farewell:
                        print(farewell)
                        self.audio_player.say_response(farewell)
                        break

                processed_command = self.nlp_processor.process_text(user_input)
                self.audio_player.say_response(processed_command)
