class ClaraAssistant:

    def __init__(self):
        self.woken_up = False
    
    def check_wake_word(self, command):
        if "teste" in command.lower():
            self.woken_up = True

    def start(self):
        return "Olá! Como posso ajudar?"

    def end(self):
        return "Até logo!"
    
    def process_command(self, command):
        pass