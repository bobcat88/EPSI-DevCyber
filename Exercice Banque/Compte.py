class Compte:
    def __init__(self, numeroCompte, nomProprietaire, solde):
        self.numeroCompte = numeroCompte
        self.nomProprietaire = nomProprietaire
        self.solde = solde

    #fonction de retrait+showsolde
    def retrait(self, montant):
        print("Solde avant retrait:", self.solde)
        self.solde -= montant
        print("Montant du retrait:", montant)
        print("Solde après retrait:", self.solde)

    #fonction de versement sur compte+solde
    def versement(self, montant):
        print("Solde avant versement:", self.solde)
        self.solde += montant
        print("Montant du versement:", montant)
        print("Solde après versement:", self.solde)

    def afficherSolde(self):
        print("Solde du compte:", self.solde)
