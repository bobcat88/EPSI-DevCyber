import json
import tkinter as tk
from datetime import datetime as dt
from tkinter import filedialog as fd


def load_data_from_file():
    file_path = fd.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)


def get_age_from_birthday(birthday):
    today = dt.today()
    birthday_date = dt.strptime(birthday, "%Y/%m/%d")
    age = today.year - birthday_date.year - ((today.month, today.day) < (birthday_date.month, birthday_date.day))
    return age


def get_person_data():
    personne = {"nom": input("Nom: "), "prenom": input("Prénom: "),
                "date d'anniversaire": input("Date d'anniversaire au format AAAA/MM/JJ: "), "ville": input("Ville: ")}
    personne["age"] = get_age_from_birthday(personne["date d'anniversaire"])
    print(f"Age: {personne['age']}")
    return personne


def save_to_json(data):
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    folder_path = fd.askdirectory()
    if folder_path:
        filename = fd.asksaveasfilename(initialdir=folder_path, defaultextension=".json",
                                        filetypes=[("JSON files", "*.json")])
        if filename:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            print("Fichier sauvegardé comme:", filename)


def main():
    new_or_load = input("Nouveau fichier ou Charger ? N/C ")
    if new_or_load == "C":
        data = load_data_from_file()
    else:
        data = []

    while True:
        personne = get_person_data()
        data.append(personne)
        choice = input("Voulez-vous ajouter une autre personne? (O/N) ")
        if choice.upper() != "O":
            break

    save_to_json(data)


if __name__ == "__main__":
    main()
