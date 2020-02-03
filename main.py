from src import CanalAnonyme, Utilisateur
from datetime import datetime, timedelta

canal = CanalAnonyme()

alice = Utilisateur('Alice', canal)
bob = Utilisateur('Bob', canal)

t0, t1 = alice.generer_secret(bob, timedelta(seconds=3))
secret_alice = alice.extraire_secret(bob, t0, t1)
secret_bob = bob.extraire_secret(alice, t0, t1)

assert secret_alice == secret_bob, "echec lors de l'echange des cles"
print('alice et bob ont la même clé:', secret_alice)
