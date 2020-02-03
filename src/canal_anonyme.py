from datetime import timedelta

from .message import Message
from .utilisateur import Utilisateur

class CanalAnonyme:
    def __init__(self):
        self.messages = set()

    def poster_message_anonyme(self, message: str, date=None):
        msg = Message(message, date=date)
        self.messages.add(msg)
        return msg

    def recuperer_messages_anonymes(self, date_debut, date_fin):
        return tuple(filter(
            lambda message: message.date >= date_debut and message.date <= date_fin,
            sorted(self.messages, key=lambda message: message.date)
        ))

    def generer_secret(self, emetteur: Utilisateur, recepteur: Utilisateur, duree: timedelta):
        emetteur.generer_secret(recepteur.nom, duree)
        recepteur.generer_secret(emetteur.nom, duree)

    def extraire_secret(self):
        pass
