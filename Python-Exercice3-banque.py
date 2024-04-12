
class Compte:
    def __init__(self, numeroCompte, nomProprietaire, solde):
        self.numeroCompte = numeroCompte
        self.nomProprietaire = nomProprietaire
        self.solde = solde

    def retrait(self, montant):
        print("Solde avant retrait:", self.solde)
        self.solde -= montant
        print("Montant du retrait:", montant)
        print("Solde après retrait:", self.solde)

    def versement(self, montant):
        print("Solde avant versement:", self.solde)
        self.solde += montant
        print("Montant du versement:", montant)
        print("Solde après versement:", self.solde)

    def afficherSolde(self):
        print("Solde du compte:", self.solde)


class CompteCourant(Compte):
    def __init__(self, numeroCompte, nomProprietaire, solde, autorisationDecouvert, pourcentageAgios):
        super().__init__(numeroCompte, nomProprietaire, solde)
        self.autorisationDecouvert = autorisationDecouvert
        self.pourcentageAgios = pourcentageAgios

    def appliquerAgios(self):
        if self.solde < 0:
            print("Solde avant application des agios:", self.solde)
            self.solde -= self.solde * self.pourcentageAgios / 100
            print("Montant des agios:", self.solde * self.pourcentageAgios / 100)
            print("Solde après application des agios:", self.solde)


class CompteEpargne(Compte):
    def __init__(self, numeroCompte, nomProprietaire, solde, pourcentageInterets):
        super().__init__(numeroCompte, nomProprietaire, solde)
        self.pourcentageInterets = pourcentageInterets

    def appliquerInterets(self):
        print("Solde avant application des intérêts:", self.solde)
        self.solde += self.solde * self.pourcentageInterets / 100
        print("Montant des intérêts:", self.solde * self.pourcentageInterets / 100)
        print("Solde après application des intérêts:", self.solde)


# Demander à l'utilisateur le compte concerné et le montant de la transaction
type_compte = input("Entrez le type de compte (courant ou épargne): ")
montant = float(input("Entrez le montant de la transaction (positif pour un versement, négatif pour un retrait): "))

# Créer un compte en fonction du type entré par l'utilisateur
if type_compte == "courant":
    compte = CompteCourant("CC123456", "John Doe", 1000, 500, 1)
elif type_compte == "epargne":
    compte = CompteEpargne("CE654321", "Jane Doe", 2000, 2)

# Effectuer la transaction en fonction du montant entré par l'utilisateur
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