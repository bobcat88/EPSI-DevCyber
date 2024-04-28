import sqlite3 as lite


def connect_to_database():
    db_path = './BDD/credits.db'
    conn = lite.connect(db_path)
    return conn


def delete_suppressed_data(c, conn):
    c.execute("DELETE FROM dossier WHERE statut_rgpd = 'suppression_rgpd'")
    conn.commit()


if __name__ == "__main__":
    try:
        conn = connect_to_database()
        c = conn.cursor()

        delete_suppressed_data(c, conn)

    except lite.Error as e:
        print("Erreur de connection a la base de donnee:", e)

    finally:
        if conn:
            conn.close()
