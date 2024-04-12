class Vehicules:
	
  def __init__(self, portes, volants, vitesse, moteurs, roues):
    self.poid = portes
    self.prix = volants
    self.vitesse = vitesse
    self.roues = moteurs
    self.roues = roues
	
class Voiture(Vehicules):
  def __init__ (self, portes, volants, vitesse, moteurs, roues, decapotable, sansPermis):
    super(Vehicules, self).__init__()
    self.decapotable = decapotable
    self.sansPermis = sansPermis
  def hascapote(self):
    if self.decapotable == True :
      print("vous allez pouvoir chopper cet été")
    else:
      print("Nous sommes désolé, cet été vous allez rester celibataire, vous devriez regarder nos autres modèles")

class Camion(Vehicules):
  def __init__ (self, portes, volants, vitesse, moteurs, roues, charge, conteneurs):
    super(Vehicules, self).__init__()
    self.charge = charge
    self.conteneurs = conteneurs
  def canyousend2HQWorld(self):
    if self.conteneurs == True :
      print("Vous pouvez utiliser ce camion pour la logistique internationale")
    else:
      print("Nous sommes désolé, ce camion ne permet pas de gérer la logistique internationale")   

def Askbuycartruck():
  choice = input("Plutot Voiture ou Camion? Voiture/Camion")
  if choice == "Voiture":
    choicemodelcar = present2carmodel
  else:
    choicemodeltruck = present2truckmodel
    
# Création des modèles de voitures
voiture_decapotable = Voiture(4, 1, 200, 1, 4, True, False)
voiture_non_decapotable = Voiture(5, 1, 180, 1, 4, False, True)

# Création des modèles de camions
camion_3_conteneurs = Camion(2, 1, 120, 1, 6, 10000, 3)
camion_1_conteneur = Camion(2, 1, 100, 1, 4, 5000, 1)

# Appel des méthodes pour les voitures
voiture_decapotable.hascapote()
voiture_non_decapotable.hascapote()

# Appel des méthodes pour les camions
camion_3_conteneurs.canyousend2HQWorld()
camion_1_conteneur.canyousend2HQWorld()
  
    

        