from Compte import Compte

#creation classe fille "CompteEpargne"
class CompteEpargne(Compte):
    def __init__(self, numeroCompte, nomProprietaire, solde, pourcentageInterets):
        super().__init__(numeroCompte, nomProprietaire, solde)
        self.pourcentageInterets = pourcentageInterets

    def appliquerInterets(self):
        print("Solde avant application des intérêts:", self.solde)
        self.solde += self.solde * self.pourcentageInterets / 100
        print("Montant des intérêts:", self.solde * self.pourcentageInterets / 100)
        print("Solde après application des intérêts:", self.solde)