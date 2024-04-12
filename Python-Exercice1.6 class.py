class Voiture:
  roue = 4
  def __init__(self, nom, portes, volants, vitesses, moteur):
    self.nom = nom
    self.portes = portes
    self.volants = volants
    self.vitesses = vitesses
    self.moteur = moteur

voiture = Voiture('Ionic', 5, 1, [0, 180], 'V6')

print ("Le modèle : " + str(voiture.nom))
print ("possède " + str(voiture.portes) + " portes")
print ("et possède " + str(voiture.volants) + " volant")
print ("elle possède une vitesse comrpise entre : " +str(voiture.vitesses) + "Km/h")
print ("et possède un moteur de type : " + str(voiture.moteur))