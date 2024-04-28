import random
import sqlite3 as lite
import string
from datetime import timedelta, date

from faker import Faker


def connect_to_database():
    db_path = './BDD/credits.db'
    conn = lite.connect(db_path)
    c = conn.cursor()
    return conn, c


def close_database_connection(conn):
    conn.commit()
    conn.close()


def vider_tables():
    conn, c = connect_to_database()
    c.execute("DELETE FROM client")
    c.execute("DELETE FROM dossier")
    close_database_connection(conn)


def create_fake_clients(num_clients=100):
    fake = Faker('fr_FR')
    conn, c = connect_to_database()

    clients = []
    for _ in range(num_clients):
        nom_client = fake.first_name()
        prenom_client = fake.last_name()
        status_contentieux = random.choice([True, False])
        c.execute("INSERT INTO client (nom_client, prenom_client, status_contentieux) VALUES (?, ?, ?)",
                  (nom_client, prenom_client, status_contentieux))
        client_id = c.lastrowid
        clients.append({'id_client': client_id, 'nom_client': nom_client, 'prenom_client': prenom_client,
                        'status_contentieux': status_contentieux})

    close_database_connection(conn)
    return clients


def create_fake_dossiers(num_dossiers=100):
    fake = Faker('fr_FR')
    conn, c = connect_to_database()
    start_date = date(2000, 1, 1)
    end_date = date(2023, 12, 31)
    c.execute("SELECT id_client FROM client")
    clients = c.fetchall()
    clients = [client[0] for client in clients]
    pourcentage_avec_date_cloture = 0.75

    for _ in range(num_dossiers):
        reference_client = random.choice(clients)
        numero_de_dossier = ''.join(random.choices(string.digits, k=6))
        type_credit = random.choice(['personnel', 'voiture', 'immobilier'])
        montant_credit = random.randint(1500, 200000)
        duree_credit = random.choice([1, 2, 5, 7, 10, 15, 20])
        date_creation = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        if random.random() < pourcentage_avec_date_cloture:
            date_cloture = date.today() if random.random() < 0.5 else date_creation + timedelta(
                days=random.randint(0, (date.today() - date_creation).days))
        else:
            date_cloture = None

        try:
            c.execute("INSERT INTO dossier VALUES (NULL,?,?,?,?,?,?,?,?)",
                      (reference_client, numero_de_dossier,
                       type_credit, montant_credit,
                       duree_credit, date_creation,
                       date_cloture, None))
            conn.commit()
        except lite.Error as e:
            print(f"erreur d'insertion dans base de donnee: {e}")
            conn.rollback()

    close_database_connection(conn)


if __name__ == "__main__":
    vider_tables()
    create_fake_clients()
    create_fake_dossiers()
