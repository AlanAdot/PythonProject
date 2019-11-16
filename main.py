from Scripts.Character import *
from Scripts.Monstre import *

print( "on va lancer le rpg, t'es pret")

monstre1=Monstre()
personnage1=Character("hulk")
personnage2=Character("captain")

print(monstre1.Health)
personnage1.actions(monstre1)


