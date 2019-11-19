from Scripts.Monstre import *
from Scripts.Character import *





class Map:

    heros=Character("vipria")
    ennemi=Monstre()
    TailleX=10

    objets = {'excalibur  (1)': 100, 'cote_de_mailles  (2)': 50, 'poulet_roti (3)': 20, 'Bible  (4)': 30}


    def _init_(self,TailleX):
        self.TailleX=TailleX


    def initialisation(self,position_heros):

        self.heros.position = position_heros
        n=self.TailleX
        Liste=[]
        Liste.append("M")
        for k in range (1,n-2):
            Liste.append("_")
        Liste.append("*")
        Liste.append("||")
        Liste[position_heros]='@'

        return(Liste)

    def mapdisplay(self,Liste):
        n=len(Liste)
        for k in range (0,n-1):
            print(Liste[k],end='  ')
        print(Liste[n-1])


    def mapdisplay2(self,Liste):
        print ("choisis    (q)  gauche    (d)  droite")
        position = input()
        n=len(Liste)
        if position == 'q':
            if Liste[1] != '@':
                k=0
                while Liste[k] != '@':
                    k+=1
                Liste[k]='_'
                Liste[k-1]='@'
                self.heros.position -=1
                self.mapdisplay(Liste)
            else:
                print("bienvenue chez le marchand")
                print ("tu peux t'acheter ce que tu veux")
                for key,value in self.objets.items():
                    print(key,value,end='  ')
                    choix = input ()


                    if (choix ==1):
                        self.heros.max_damage+=20
                        print("degats d'attaques +20  max_damage =",end='   ')
                        print(self.heros.max_damage)

                    if (choix == 2):
                        self.heros.Armor_point += 20
                        print("points de defense +20  Armor_point=",end='   ')
                        print(self.heros.Armor_point)

                    if (choix == 3):
                        self.heros.Health += 20
                        print("points de vie +20  health=",end='  ')
                        print(self.heros.Health)

                    if (choix == 4):
                        self.heros.Experience +=100
                        print("experience +100")
                        self.heros.nextlevel()








        else :
            if Liste[n-3] != '@':
                k=0
                while Liste[k] != '@':
                    k+=1
                Liste[k]='_'
                Liste[k+1]='@'
                self.heros.position += 1
                self.mapdisplay(Liste)

            else :
                print("coucou")
                while (   (self.heros.Health>=0) or   (self.ennemi.Health >=0)) :
                    print("salut")
                    self.heros.actions(ennemi)
                    if (self.ennemi.Health <= 0):
                        print("Bravo tu as gagné")
                    else:
                        print("t'as perdu grosse merde")



