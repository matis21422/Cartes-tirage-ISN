from browser import document, alert
#import random declare la fonction random
#import replit declare la fonction replit
import random



liste_1 = ["C1","CR","CD","CV","CX","C9","C8","C7","K1","KR","KD","KV","KX","K9","K8","K7","P1","PR","PD","PV","PX","P9","P8","P7","T1","TR","TD","TV","TX","T9","T8","T7"]
#random.shuffle melange la liste
#n sert a compter le rang de la carte dans la liste
#juste sert a compter les points
#ncartes est le nombre de cartes a faire afficher
random.shuffle(liste_1)


n = 0
juste = 0
ncartes = int(input("Choisissez le nombre de cartes sur lequel vous voulez vous entrainer de 1 a 32:")) - 1
#La boucle While permet de compter le nombre de cartes donnees


while n <= ncartes:
  #la variable inp et la boucle if est la variable qui permet de faire avancer le programme lorsue l'utilisateur appuye sur "enter"
  inp = str(input())
  if inp == "":
    #print(liste_1[n]) fait afficher la carte suivant dans la liste melangee avant
    print(liste_1[n])
    n = n+1


pause = str(input())
print("")


n = 0
while n <= ncartes:
  print("Carte de rang" , n + 1)
  resultat = str(input())

  if resultat == liste_1[n]:
    print("bravo")
    juste = juste + 1

  else:
    print("FAUX! La bonne reponse est " , liste_1[n])
  n = n+1
print("Vous avez eu " , juste , "reponses justes sur " , ncartes + 1 , "cartes.")
