def creer_pyramide(chaine):
    longueur = len(chaine)
    caractères_utilisés = 0
    for i in range(1, longueur * 2, 2):
        print(chaine[caractères_utilisés:caractères_utilisés + i].ljust(longueur, ' '))
        caractères_utilisés += i

chaine = input("Entrez une chaîne de caractères : ")
creer_pyramide(chaine)
import os
os.system("pyramide.txt")