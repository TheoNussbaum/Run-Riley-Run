import mysql.connector


# Fonction pour ouvrir la connexion à la base de données
def open_db():
    return mysql.connector.connect(
        host="127.0.0.1",  # Adresse du serveur de la base de données
        port=3306,  # Port par défaut pour MySQL
        user="root",  # Nom d'utilisateur MySQL
        password="Cactus-8",  # Mot de passe pour la connexion
        database="run_raily_run",  # Nom de la base de données
        auth_plugin='mysql_native_password',  # Spécification du plugin d'authentification
        buffered=True,  # Activation du buffering pour éviter des erreurs de lecture multiples
        autocommit=True  # Active l'autocommit, chaque requête est directement validée
    )

# Connexion à la base de données
db_connection = open_db()
print("Connexion réussie")

# Rechercher le meilleur score du joueur
def search_best_score():
    query = "SELECT best_score FROM player"  # Requête SQL pour récupérer le meilleur score
    cursor = db_connection.cursor()  # Création du curseur pour exécuter la requête
    cursor.execute(query)  # Exécution de la requête
    rows = cursor.fetchone()  # Récupération de la première ligne du résultat
    cursor.close()  # Fermeture du curseur
    return rows  # Retour du résultat (meilleur score)

# Met à jour le meilleur score du joueur
def edit_score(best_score):
    query = "UPDATE player SET best_score = %s WHERE idPlayer = 1"
    cursor = db_connection.cursor()
    cursor.execute(query, (best_score,))
    cursor.close()

# Récupère le score nécessaire pour débloquer un personnage
def search_score_to_unlock(idcharacter):
    query = "SELECT score_to_unlock FROM `character` WHERE idCharacter = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (idcharacter,))
    rows = cursor.fetchone()
    cursor.close()
    return rows

# Met à jour l'ID du personnage sélectionné
def edit_idCharacter(idcharacter):
    query = "UPDATE player SET Character_idCharacter = %s WHERE idPlayer = 1"
    cursor = db_connection.cursor()
    cursor.execute(query, (idcharacter,))
    cursor.close()

# Récupère l'ID du personnage sélectionné
def search_idCharacter():
    query = "SELECT Character_idCharacter FROM `player`"
    cursor = db_connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchone()
    cursor.close()
    return rows
