# Run, Riley, Run !

**Run, Riley, Run !** est un jeu vidéo de type *infinite runner* inspiré du célèbre jeu "Chrome Dino", avec un univers graphique basé sur le dessin animé **The Boondocks**. Le jeu est développé en Python en utilisant la bibliothèque **Pygame**.


![CITY](https://github.com/user-attachments/assets/b3604f20-1b8f-4015-8dd6-32173ccbf39a)

## Fonctionnalités

- Jouabilité infinie avec des obstacles de plus en plus rapides et difficiles.
- Univers graphique inspiré de la série animée *The Boondocks*.
- Commandes simples et intuitives (sauter, esquiver).
- Gestion du score et de la progression du joueur.
- Personnages débloquables (En fonction du BestScore).

## Installation

### Prérequis
- **Python 3.x**
- **Librairie Pygame** installé (si nécessaire, vous pouvez l’installer avec la commande suivante) :
  ```bash
  pip install pygame
  ```
- **Librairie Random**
- **Librairie mysql-connector** installé (si nécessaire, vous pouvez l’installer avec la commande suivante) :
  ```bash
  pip install mysql-connector
  ```

- **MySQL Server**
- **Client SQL**, par example HediSQL
- **Connection a la DB** pour interagire avec la base de données executer cette requete dans votre client SQL (changer le "utilisateur" et le "mot de passe" par vos valeurs)
  ```SQL
  ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Cactus-8';
  FLUSH PRIVILEGES;
  ```
  Cette requete change l'algorithme de cryptage de votre mot de passe, car mysql-connector ne support pas celui de base.

### Étapes pour lancer le jeu
1. Clonez ce dépôt sur votre machine locale (GitHub Desktop)
2. Accédez au dossier du jeu
3. Lancez le fichier main.py

## Commandes du jeu
- Flèche directionnel vers le haut : Sauter

![Design sans titre (1)](https://github.com/user-attachments/assets/7978f2ec-7b63-485a-ad1e-f6012e73179e)
- Maintenir la flèche directionnel vers le bas : Esquiver

![Design sans titre (2)](https://github.com/user-attachments/assets/dc9abd33-c06d-41c2-acf0-f948c57655f6)


## Auteurs
- Nussbaum Théo (@TheoNussbaum)
- Ferreira Carlos (@CarlosFerreiraCPNV)
