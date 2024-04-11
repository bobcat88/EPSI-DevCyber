import datetime as dt
from datetime import datetime as d
import json

personnes = []

def age_reel(personne):
    today = d.today()
    anniv_input = d.strptime(personne["date d'anniversaire"],"%Y/%m/%d")
    age = today.year - anniv_input.year - ((today.month, today.day))<(anniv_input.month,anniv_input.day)
    return age
    
while True:
    personne = {}
    personne["nom"] = input("Nom: ")
    personne["prénom"] = input("Prénom: ")
    personne["date d'anniversaire"] = input("date d'anniversaire au format AAAA/MM/JJ: ")
    personne["ville"] = input("Ville: ")
    personne["age"] = age_reel()
    personnes.append(personne)
    choice = input("Add another person? (y/n) ")
    if choice != "y":
        break

print(personnes)

with open('ExerciceData.json', 'w', encoding='utf-8') as f:
    json.dump(personnes, f, ensure_ascii=False, indent=4)
print("Données enregistrées")