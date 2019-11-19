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
    position=4

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
                print("l'ennemi a réussi a esquive ton coup")
                print(ennemi.Health)

            elif ( hasard3 < (ennemi.parry)/100  ):
                    ennemi.Health = ennemi.Health - (degat * (1 - (ennemi.Armor_point) / 100))*(1- 0.7)
                    print(ennemi.Health)


            else:
                ennemi.Health=ennemi.Health - (degat * (1 - (ennemi.Armor_point) / 100))
                print(ennemi.Health)


        if (choix == '2'):
            print("tu veux utiliser un objet?")
            print(" (1) prendre une arme     (2)  prendre une potion    (3) prendre des fleurs")

        if (choix == '3'):
            print (" (1) lancer une boule de feu (40 MP)     (2)  guerir (20 MP)")
            choix=input()

            if (choix == '1'):
                if (self.MP >= 40):
                    self.MP = self.MP - 40
                    ennemi.Health -=10
                    print ("voici tes MP :",self.MP, "ennemi Health :", ennemi.Health)
                else:
                    print("pas assez de MP")

            else:
                if (self.MP >= 30):
                    self.MP = self.MP - 30
                    self.Health +=10
                    print("voici ton Health  :",self.Health, "voici tes MP :",self.MP )

                else:
                    print("pas assez de MP")




    def nextlevel(self):
        n=self.Experience
        k=1
        A= k*100
        if (A >= n):
            self.Level +=1
            k+=1
            print("ton personnage a atteint le niveau", end='  ')
            print(k)
