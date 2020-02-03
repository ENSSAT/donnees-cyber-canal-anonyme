import time
from random import random
from datetime import timedelta, datetime
from threading import Thread

class Utilisateur:
    def __init__(self, nom, canal):
        self.nom = nom
        self.canal = canal
        self.messages_envoyes = set() # message envoyes par cet utilisateur
        self.locked = False # personnes avec qui un secret est partagé


    def generer_secret(self, interlocuteur, duree: timedelta):
        def _thread_generer_secret():
            tfin = datetime.now() + duree
            while datetime.now() < tfin:
                dodo = random() * 0.9 + 0.1
                time.sleep(dodo)

                b = (random() > 0.5)*1

                msg = self.canal.poster_message_anonyme(
                    self.nom if b==0 else interlocuteur.nom)

                self.messages_envoyes.add(msg)
        
        if not self.locked:
            self.locked = True
            t0 = datetime.now()

            thread = Thread(target=_thread_generer_secret)
            thread.start()

            interlocuteur.generer_secret(self, duree)

            if thread:
                thread.join()
            
            t1 = datetime.now()
            self.locked = False
            return (t0, t1)


    def extraire_secret(self, interlocuteur, t0, t1):
        messages = self.canal.recuperer_messages_anonymes(t0, t1)

        bits = []
        for message in messages:
            je_ment = message in self.messages_envoyes and not self.nom in message.texte
            il_ment = message not in self.messages_envoyes and self.nom in message.texte
            value = (je_ment or il_ment) * 1
            bits.append(value)
        
        return bytes(bits).hex()
    

    def __str__(self):
        return "%s (%s messages envoyés)"%(self.nom, len(self.messages_envoyes))
