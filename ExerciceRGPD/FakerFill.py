import random
import sqlite3 as lite
import string
from datetime import date

from faker import Faker


def fill_fake_data():
    fake = Faker('fr_FR')
    conn = lite.connect('credits.db')
    c = conn.cursor()

    # Remplissage Faker (delete all data before filling).
    c.execute("DELETE FROM client")
    c.execute("DELETE FROM dossier")
    conn.commit()

    clients = []
    for _ in range(100):
        clients.append({
            'Nom_client': fake.name().split()[0],
            'Prenom_client': fake.name().split()[1],
            'Status_contentieux': random.choice([True, False])
        })
    c.executemany("INSERT INTO client VALUES (NULL,?,?,?)",
                  [(client['Nom_client'], client['Prenom_client'], client['Status_contentieux']) for client in clients])
    conn.commit()

    dossiers = []
    date_crea = date.today().strftime('%Y-%m-%d')

    for _ in range(100):
        dossier = {
            'reference_client': random.choice([client['id_client'] for client in clients]),
            'numero_de_dossier': ''.join(random.choices(string.digits, k=6)),
            'type_credit': random.choice(['personnel', 'voiture', 'immobilier']),
            'montant_credit': random.randint(1500, 200000) + (random.randint(0, 4) * 1500),
            'duree_credit': random.choice([1, 2, 5, 7, 10, 15, 20]),
            'date_creation': date.today().strftime('%Y-%m-%d'),
            'date_cloture': None if random.random() < 0.5 else date.today().strftime(
                '%Y-%m-%d') if date.today().year - int(
                date.fromisoformat(date_crea).strftime('%Y')) >= 1 else None,
            'statut_rgpd': ''
        }
        dossiers.append(dossier)
    c.executemany("INSERT INTO dossier VALUES (NULL,?,?,?,?,?,?,?)", [(dossier['reference_client'],
                                                                       dossier['numero_de_dossier'],
                                                                       dossier['type_credit'],
                                                                       dossier['montant_credit'],
                                                                       dossier['duree_credit'],
                                                                       dossier['date_creation'],
                                                                       dossier['date_cloture'], dossier['statut_rgpd'])
                                                                      for dossier in dossiers])
    conn.commit()

    conn.close()


if __name__ == "__main__":
    fill_fake_data()
