import json
import os
import sqlite3 as lite


def connect_to_database():
    db_path = './BDD/credits.db'
    conn = lite.connect(db_path)
    return conn


def archive_to_json(c):
    archive_rgpd_log = []

    c.execute("SELECT * FROM dossier WHERE statut_rgpd = 'archive_rgpd'")
    archive_rows = c.fetchall()

    for row in archive_rows:
        archive_rgpd_log.append({
            'dossier_id': row[0],
            'reference_client': row[1],
            'numero_de_dossier': row[2],
            'type_credit': row[3],
            'montant_credit': row[4],
            'date_creation': row[6],
            'date_cloture': row[7]
        })
    logs_directory = './logs'
    if not os.path.exists(logs_directory):
        os.makedirs(logs_directory)
    archive_directory = os.path.join(logs_directory, 'archive')

    if not os.path.exists(archive_directory):
        os.makedirs(archive_directory)

    with open(os.path.join(archive_directory, 'archive_rgpd.json'), 'w') as f:
        json.dump(archive_rgpd_log, f, indent=4)


def suppression_to_json(c):
    suppression_rgpd_log = []

    c.execute("SELECT * FROM dossier WHERE statut_rgpd = 'suppression_rgpd'")
    suppression_rows = c.fetchall()

    for row in suppression_rows:
        suppression_rgpd_log.append({
            'dossier_id': row[0],
            'reference_client': row[1],
            'numero_de_dossier': row[2],
            'type_credit': row[3],
            'montant_credit': row[4],
            'date_creation': row[6],
            'date_cloture': row[7]
        })

    logs_directory = './logs'
    if not os.path.exists(logs_directory):
        os.makedirs(logs_directory)

    # Create the 'suppression' directory within 'logs' if it doesn't exist
    suppression_directory = os.path.join(logs_directory, 'suppression')
    if not os.path.exists(suppression_directory):
        os.makedirs(suppression_directory)

    # Save suppression_rgpd_log to JSON file in 'suppression' directory
    with open(os.path.join(suppression_directory, 'suppression_rgpd.json'), 'w') as f:
        json.dump(suppression_rgpd_log, f, indent=4)


if __name__ == "__main__":
    # Include database connection setup and cursor creation here
    try:
        conn = connect_to_database()
        c = conn.cursor()

        archive_to_json(c)
        suppression_to_json(c)

    except lite.Error as e:
        print("Erreur de connection a la base de donnee:", e)

    finally:
        if conn:
            conn.close()
