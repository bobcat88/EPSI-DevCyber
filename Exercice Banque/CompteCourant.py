from Compte import Compte

#creation classe Fille "CompteCourant"
class CompteCourant(Compte):
    def __init__(self, numeroCompte, nomProprietaire, solde, autorisationDecouvert, pourcentageAgios):
        super().__init__(numeroCompte, nomProprietaire, solde)
        self.autorisationDecouvert = autorisationDecouvert
        self.pourcentageAgios = pourcentageAgios

    #application d'agio montant+solde
    def appliquerAgios(self):
        if self.solde < 0:
            print("Solde avant application des agios:", self.solde)
            self.solde -= self.solde * self.pourcentageAgios / 100
            print("Montant des agios:", self.solde * self.pourcentageAgios / 100)
            print("Solde après application des agios:", self.solde)
