prix_ht = float(input("Entrez le prix HT : "))
print("Le prix HT est", prix_ht)

reduction = int(input("Entrez le pourcentage de réduction sans signe '%' : ")) #maybe float ? if reduction is not int

prix_ttc = prix_ht * (1 - reduction / 100) * 1.2 #if 20% VAT value food could be 5%

print("Le prix de vente TTC est", prix_ttc,"$")