import os
import datetime as dt
from datetime import datetime as d
import tkinter as tk
from tkinter import filedialog as fd
import json

def Filecheck ():
    if os.path.isfile('*.json'):
        with open('*.json', 'r+', encoding='utf-8') as f:
          data = json.load(f)[0]
    else:
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        file_path = fd.askopenfilename()
    if file_path:
        with open(file_path,'r+', encoding='utf-8') as f:
            data = json.load(f)[0]
        root.attributes('-topmost', False)
    print(data)
    return data

def age_reel(personne):
    today = d.today()
    anniv_input = d.strptime(personne["date d'anniversaire"],"%Y/%m/%d")
    age = today.year - anniv_input.year - ((today.month, today.day) < (anniv_input.month, anniv_input.day))
    return age

def onstart():
    new_or_load = input("Nouveau fichier ou Charger ? N/C ")
    if new_or_load == "C":
        Filecheck()

data = onstart()

personnes = []

if data:
    personnes.extend(data)

while True:
    personne = {}
    personne["nom"] = input("Nom: ")
    personne["prenom"] = input("Prénom: ")
    personne["date d'anniversaire"] = input("date d'anniversaire au format AAAA/MM/JJ: ")
    personne["ville"] = input("Ville: ")
    personne["age"] = age_reel(personne)
    print(f"Age: {personne['age']}")    
    personnes.append(personne)
    choice = input("voulez vous ajouter une personne? (O/N) ")
    if choice != "O":
        break

def save_to_json(data):
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    folder_path = fd.askdirectory()
    if folder_path:
        filename = fd.asksaveasfilename(initialdir=folder_path, defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if filename:
            mode = 'a' if os.path.isfile(filename) else 'w'
            with open(filename, mode, encoding ='utf-8') as f:
                json.dump(data, f, indent=4)
            print("fichier sauvé comme:", filename)
    root.attributes('-topmost', False)

save_to_json(personnes)