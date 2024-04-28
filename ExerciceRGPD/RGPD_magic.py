import json
import random
import sqlite3 as lite
import string
from datetime import date


def connect_to_database():
    conn = lite.connect('credits.db')
    c = conn.cursor()


def close_connection(conn):
    conn.commit()
    conn.close()


def update_dossier(c, clients):
    today = date.today().strftime('%Y-%m-%d')
    dossiers = []

    for client in clients:
        dossier = {
            'reference_client': client['id_client'],
            'numero_de_dossier': ''.join(random.choices(string.digits, k=6)),
            'type_credit': random.choice(['personnel', 'voiture', 'immobilier']),
            'montant_credit': random.randint(1500, 200000) + (random.randint(0, 4) * 1500),
            'duree_credit': random.choice([1, 2, 5, 7, 10, 15, 20]),
            'date_creation': today,
            'date_cloture': None if random.random() < 0.5 else today if int(today[:4]) - date(today[:4], 1,
                                                                                              1).weekday() <= 3 else None,
            'statut_rgpd': ''
        }

        dossiers.append(dossier)

    c.executemany("INSERT INTO dossier VALUES (NULL,?,?,?,?,?,?,?)",
                  [(dossier['reference_client'], dossier['numero_de_dossier'], dossier['type_credit'],
                    dossier['montant_credit'], dossier['duree_credit'], dossier['date_creation'],
                    dossier['date_cloture'], dossier['statut_rgpd']) for dossier in dossiers])


def update_rgpd(c):
    today = date.today().strftime('%Y-%m-%d')
    archive = []
    suppression_rgpd = []

    for row in c.execute("SELECT * FROM dossier"):
        if (row[7] is not None and int(date.fromisoformat(row[6]).strftime('%Y')) >= 5 and row[3] == 'personnel' and
            row[7] == False) or \
                (row[7] is not None and int(date.fromisoformat(row[6]).strftime('%Y')) >= 10 and row[3] == 'voiture' and
                 row[7] == True):
            archive.append({'reference_client': row[1], 'numero_de_dossier': row[2], 'type_credit': row[3],
                            'montant_credit': row[4], 'duree_credit': row[5], 'date_creation': row[6],
                            'statut_rgpd': row[7]})
        elif (row[7] is not None and int(date.fromisoformat(row[6]).strftime('%Y')) >= 10 and row[3] == 'immobilier' and
              row[7] == False) or \
                (row[7] is not None and int(date.fromisoformat(row[6]).strftime('%Y')) >= 15 and row[3] == 'voiture' and
                 row[7] == True):
            suppression_rgpd.append({'id_dossier': row[0], 'reference_client': row[1], 'numero_de_dossier': row[2],
                                     'type_credit': row[3], 'montant_credit': row[4], 'duree_credit': row[5],
                                     'date_creation': row[6], 'date_cloture': row[7], 'statut_rgpd': row[8]})

    with open(f'archive_{today[:4]}.json', 'w') as archive_file:
        json.dump(archive, archive_file, indent=4)

    with open(f'suppression_rgpd_{today[:4]}.json', 'w') as suppression_rgpd_file:
        json.dump(suppression_rgpd, suppression_rgpd_file, indent=4)

    for dossier in archive:
        c.execute("UPDATE dossier SET statut_rgpd = ? WHERE numero_de_dossier = ?",
                  (True, dossier['numero_de_dossier']))

    for dossier in suppression_rgpd:
        c.execute("DELETE FROM dossier WHERE id_dossier = ?", (dossier['id_dossier'],))


def get_all(c):
    """Retrieve all dossier entries."""
    return [{'reference_client': row[1], 'numero_de_dossier': row[2], 'type_credit': row[3],
             'montant_credit': row[4], 'duree_credit': row[5], 'date_creation': row[6],
             'statut_rgpd': row[7]} for row in cursor.execute("SELECT * FROM Dossier")]


# Other functions remain the same

if __name__ == "__main__":
    database_name = 'credits.db'
    conn, c = connect_to_database('credits.db')

    # Update dossier
    update_dossier(c, clients)

    # Update GDPR status and create log files
    update_rgpd(c)

    close_connection(conn)
