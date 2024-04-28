import random
import sqlite3 as lite
import string
from datetime import date

from faker import Faker

# création bdd et création des tables.
fake = Faker('fr_FR')
conn = lite.connect('credits.db')
c = conn.cursor()

c.execute("CREATE TABLE Client (\n"
          "    id_client INTEGER PRIMARY KEY,\n"
          "    Nom_client TEXT NOT NULL,\n"
          "    Prenom_client TEXT NOT NULL,\n"
          "    Status_contentieux BOOLEAN NOT NULL)")

c.execute("CREATE TABLE Dossier ("
          "    id_dossier INTEGER PRIMARY KEY,"
          "    reference_client INTEGER REFERENCES Client(id_client),\n"
          "    numero_de_dossier TEXT UNIQUE NOT NULL,\n"
          "    type_crédit TEXT NOT NULL,\n"
          "    montant_credit INTEGER NOT NULL CHECK (montant_credit BETWEEN 1500 AND 200000),\n"
          "    durée_crédit INTEGER NOT NULL CHECK(durée_crédit IN (1, 2, 5, 7, 10, 15, 20)),\n"
          "    date_création DATE NOT NULL,\n"
          "    date_clôture DATE,\n"
          "    statut_rgpd TEXT)")

conn.commit()

# Remplissage Faker.
c.execute("DELETE FROM Client")
c.execute("DELETE FROM Dossier")
conn.commit()

clients = []
for _ in range(100):
    clients.append({
        'Nom_client': fake.name().split()[0],
        'Prenom_client': fake.name().split()[1],
        'Status_contentieux': random.choice([True, False])
    })
c.executemany("INSERT INTO Client VALUES (NULL,?,?,?)", clients)
conn.commit()

dossiers = []
date_crea = date.today().strftime('%Y-%m-%d')

for _ in range(100):
    dossier = {
        'reference_client': random.choice([client['id_client'] for client in clients]),
        'numero_de_dossier': ''.join(random.choices(string.digits, k=6)),
        'type_crédit': random.choice(['personnel', 'voiture', 'immobilier']),
        'montant_credit': random.randint(1500, 200000) + (random.randint(0, 4) * 1500),
        'durée_crédit': random.choice([1, 2, 5, 7, 10, 15, 20]),
        'date_création': date.today().strftime('%Y-%m-%d'),
        'date_clôture': None if random.random() < 0.5 else date.today().strftime('%Y-%m-%d') if date.today().year - int(
            date.fromisoformat(date_crea).strftime('%Y')) >= 1 else None,
        'statut_rgpd': ''
    }
    dossiers.append(dossier)
c.executemany("INSERT INTO Dossier VALUES (NULL,?,?,?,?,?,?,?)", dossiers)
conn.commit()

variable_archive = []
variable_supression_rgpd = []
for row in c.execute("SELECT * FROM Dossier"):
    if (row[8] is not None and date.today().year - int(date.fromisoformat(row[6]).strftime('%Y')) >= 5 and row[
        7] == False) or \
            (row[8] is not None and date.today().year - int(date.fromisoformat(row[6]).strftime('%Y')) >= 10 and row[
                7] == True):
        variable_archive.append({'reference_client': row[1], 'numero_de_dossier': row[
