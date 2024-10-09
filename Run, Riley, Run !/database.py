import mysql.connector

# Connexion à la base de données
def open_db():
    return mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Cactus-8",
    database="run_raily_run",
    auth_plugin='mysql_native_password', # Spécifier le plugin
    buffered = True,
    autocommit = True
)

db_connection = open_db()  # Établissement de la connexion
print("Connexion réussie")

def search_best_score():
    query = "SELECT best_score FROM player"
    cursor = db_connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchone()  # Récupération de toutes les lignes de résultats
    cursor.close()
    return rows

def edit_score(best_score):
    query = "UPDATE player SET best_score = %s WHERE idPlayer = 1"
    cursor = db_connection.cursor()
    cursor.execute(query,(best_score, ))
    print(best_score)
    cursor.close()

def search_score_to_unlock(idcharacter):
    query = "SELECT score_to_unlock FROM `character` WHERE idCharacter = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (idcharacter, ))
    rows = cursor.fetchone()  # Récupération de toutes les lignes de résultats
    cursor.close()
    return rows


