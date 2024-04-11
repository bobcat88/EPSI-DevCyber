from collections import Counter
from numpy import sort

liste_billets = [100, 50, 20, 10, 2, 1]
montant_restant = int(input("combien d'argent souhaitez vous retirer?"))
billets_donné = []

for billets in liste_billets:
    while montant_restant >= billets :
        montant_restant -= billets
        billets_donné.append(billets)
        
total_billets = Counter(billets_donné)

print("voici l'argent que vous allez recevoir:")
print(f"{total_billets}")