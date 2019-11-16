from random import *

class Character:

    Health=100
    Pointdedefense=10
    dodge=5
    parry=30
    critical_hit=25
    MP=60
    min_damage=1
    max_damage=30
    Armor_point=5
    Level=1
    Experience=0


    def __init__(self, name):
        self.name= name
        print(self.name)

    def actions(self,ennemi):
        print("vous attaquez")
    
        print("(1)    tu veux attaquer  , (2)  utiliser un objet,  (3) utiliser un sort")
        
        choix = input()
        if (choix == '1'):
            print(choix)
        





