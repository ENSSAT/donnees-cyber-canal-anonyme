from datetime import datetime

class Message:
    def __init__(self, texte, date=None):
        self.texte = texte
        self.date = datetime.now() if not date else date

    def __str__(self):
        return "[%s] %s"%(self.date.strftime('%H:%M:%S'), self.texte)