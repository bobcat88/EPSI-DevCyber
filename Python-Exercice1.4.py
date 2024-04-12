import datetime as dt
from datetime import datetime as d
import tkinter as tk
from tkinter import filedialog as fd
import json

personnes = []

def age_reel(personne):
    today = d.today()
    anniv_input = d.strptime(personne["date d'anniversaire"],"%Y/%m/%d")
    age = today.year - anniv_input.year - ((today.month, today.day) < (anniv_input.month, anniv_input.day))
    return age
    
while True:
    personne = {}
    personne["nom"] = input("Nom: ")
    personne["prénom"] = input("Prénom: ")
    personne["date d'anniversaire"] = input("date d'anniversaire au format AAAA/MM/JJ: ")
    personne["ville"] = input("Ville: ")
    personne["age"] = age_reel(personne)
    print(f"Age: {personne['age']}")    
    
    personnes.append(personne)
    choice = input("voulez vous ajouter une personne? (O/N) ")
    if choice != "O":
        break

#print(personnes) #used for test

def save_to_json(data):
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    folder_path = fd.askdirectory()
    if folder_path:
        filename = fd.asksaveasfilename(initialdir=folder_path, defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if filename:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("Data saved to:", filename)
    root.attributes('-topmost', False)

save_to_json(personnes)

print("Données enregistrées")