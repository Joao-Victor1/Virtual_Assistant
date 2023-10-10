import spacy
class ClaraAssistant:

    def __init__(self):
        self.woken_up = False
        self.nlp = spacy.load("pt_core_news_sm")
    
    def check_wake_word(self, command):
        if "clara" in command:
            self.woken_up = True

    def start(self):
        return "Olá! Como posso ajudar?"

    def end(self):
        return "Até logo!"
    
    def process_command(self, command):
        if self.woken_up:
            doc = self.nlp(command)
            return doc.text
        else:
            return ""