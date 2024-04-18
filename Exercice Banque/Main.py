if __name__ == "__main__":
    from Compte import Compte
    import CompteCourant
    import CompteEpargne

# Demander à l'utilisateur le compte concerné et le montant de la transaction
type_compte = input("Entrez le type de compte (courant ou épargne): ")
montant = float(input("Entrez le montant de la transaction (positif pour un versement, négatif pour un retrait): "))

# Créer un compte en fonction du type entré par l'utilisateur (pour test)
if type_compte == "courant":
    compte = CompteCourant("FRC123456789", "John Doe", 1000, 500, 1) #creation comptecourant random (numeroCompte, nomProprietaire, solde, autorisationDecouvert, pourcentageAgios
elif type_compte == "épargne":
    compte = CompteEpargne("FRE123456789", "Jane Doe", 2000, 2) #creation compteepargne random (numeroCompte, nomProprietaire, solde, pourcentageInterets)

# Effectuer la transaction retrait ou versement en fonction du montant entré par l'utilisateur
if montant > 0:
    compte.versement(montant)
elif montant < 0:
    compte.retrait(montant)

# Appliquer les agios ou les intérêts si nécessaire
if type_compte == "courant":
    compte.appliquerAgios()
elif type_compte == "epargne":
    compte.appliquerInterets()

# Afficher le solde final du compte
compte.afficherSolde()