import sqlite3 as lite


def connect_to_database():
    db_path = './BDD/credits.db'
    conn = lite.connect(db_path)
    return conn


def check_archive_rgpd(c, conn):
    c.execute("""
        UPDATE dossier
        SET statut_rgpd = 'archive_rgpd'
        WHERE date_cloture IS NOT NULL 
            AND ((strftime('%Y', 'now') - strftime('%Y', date_creation) >= 5 
            AND (SELECT status_contentieux FROM client WHERE client.id_client = dossier.reference_client) = 0)
            OR (strftime('%Y', 'now') - strftime('%Y', date_creation) >= 10 
            AND (SELECT status_contentieux FROM client WHERE client.id_client = dossier.reference_client) = 1));
    """)
    conn.commit()


def check_suppress_rgpd(c, conn):
    c.execute("""
        UPDATE dossier
        SET statut_rgpd = 'suppression_rgpd'
        WHERE date_cloture IS NOT NULL 
            AND ((strftime('%Y', 'now') - strftime('%Y', date_creation) >= 10 
            AND (SELECT status_contentieux FROM client WHERE client.id_client = dossier.reference_client) = 0)
            OR (strftime('%Y', 'now') - strftime('%Y', date_creation) >= 15 
            AND (SELECT status_contentieux FROM client WHERE client.id_client = dossier.reference_client) = 1));
    """)
    conn.commit()


def check_ouvert(c, conn):
    c.execute("""
        UPDATE dossier
        SET statut_rgpd = 'ouvert'
        WHERE statut_rgpd IS NULL;
    """)
    conn.commit()


if __name__ == "__main__":
    try:
        conn = connect_to_database()
        c = conn.cursor()

        check_archive_rgpd(c, conn)
        check_suppress_rgpd(c, conn)
        check_ouvert(c, conn)

    except lite.Error as e:
        print("Erreur de connection a la base de donnee:", e)

    finally:
        if conn:
            conn.close()
