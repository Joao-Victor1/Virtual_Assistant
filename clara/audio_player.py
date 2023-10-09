import os
import uuid
from gtts import gTTS
import playsound

class AudioPlayer:
    def __init__(self, audio_dir):
        self.audio_dir = audio_dir
    
    def say_response(self, response_text):
        unique_id = str(uuid.uuid4())

        audio_path = os.path.join(self.audio_dir, f"response_{unique_id}.mp3")

        tts = gTTS(text=response_text, lang="pt")
        tts.save(audio_path)

        playsound.playsound(audio_path)