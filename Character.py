import random

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
        print(choix)
        if (choix == '1') :
            hasard1=random.uniform(0,1)
            hasard2=random.uniform(0,1)
            hasard3=random.uniform(0,1)

            n=  random.randint(self.min_damage,self.max_damage)
            print(n)

            if (hasard1 < (self.critical_hit) / 100):
                n = n * 2

            degat = n - ennemi.Pointdedefense

            if (hasard2 < (ennemi.dodge) / 100):
                break

            elif ( hasard3 < (ennemi.parry)/100  ):
                ennemi.Health = ennemi.Health - (degat * (1 - (ennemi.Armor_point) / 100))*(1- 0.7)

            else:
                ennemi.Health=ennemi.Health - (degat * (1 - (ennemi.Armor_point) / 100))

        if (choix == '2'):
            print("tu veux utiliser un objet?")
            print(" (1) prendre une arme     (2)  prendre une potion    (3) prendre des fleurs")


        "else:"
        "ennemi.Health = ennemi.Health - (degat * (1 - (ennemi.Armor_point) / 100))"

    "(2)"

    "(3)"
    if (self.MP >= 40):
        self.MP = self.MP - 40
        print(" (1) lancer une boule de feu      (2)  guerir")
        self.Health += 20

        ennemi.Health -= 10

    "else:"
    "print(pas assez de MP pour guerrir)"


