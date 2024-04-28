import os
import sqlite3 as lite


def create_database():
    # Specify the path to the folder where the database should be saved
    folder_path = './BDD'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Create the database and tables.
    db_path = os.path.join(folder_path, 'credits.db')
    conn = lite.connect(db_path)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS client (
                    id_client INTEGER PRIMARY KEY,
                    nom_client TEXT NOT NULL,
                    prenom_client TEXT NOT NULL,
                    status_contentieux BOOLEAN NOT NULL)''')

    c.execute('''CREATE TABLE IF NOT EXISTS dossier (
                    id_dossier INTEGER PRIMARY KEY,
                    reference_client INTEGER REFERENCES client(id_client),
                    numero_de_dossier TEXT UNIQUE NOT NULL,
                    type_credit TEXT NOT NULL,
                    montant_credit INTEGER NOT NULL CHECK (montant_credit BETWEEN 1500 AND 200000),
                    duree_credit INTEGER NOT NULL CHECK(duree_credit IN (1, 2, 5, 7, 10, 15, 20)),
                    date_creation DATE NOT NULL,
                    date_cloture DATE,
                    statut_rgpd TEXT NULL)''')

    conn.commit()
    conn.close()


print("Base de donnee cree")

if __name__ == "__main__":
    create_database()
