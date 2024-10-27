# ![title](https://github.com/user-attachments/assets/f8257954-8c25-4fc5-a231-da8dd2085e85)

Un jeu d'arcade où vous incarnez Riley, inspiré par le jeu "Chrome Dino" et l'univers de The Boondocks. Esquivez les obstacles et essayez de survivre aussi longtemps que possible dans cette course sans fin !



## À propos du jeu
**Run, Riley, Run !** est un jeu d'arcade en 2D développé avec Pygame. Vous incarnez Riley, un jeune personnage qui court sans relâche dans un environnement inspiré de The Boondocks. Votre objectif est de sauter ou d'esquiver les obstacles pour aller le plus loin possible sans vous faire toucher. Plus vous survivez longtemps, plus le jeu devient difficile et rapide. À la manière du jeu "Chrome Dino" de Google, ce jeu est simple à prendre en main mais difficile à maîtriser.

## Aperçu du jeu
![image](https://github.com/user-attachments/assets/680f7de7-44ae-4783-aaa3-246ce131b79e)

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

### Fichiers
- main.py : Le fichier principal qui lance le jeu. Il contient la logique principale, l'affichage de Riley et la génération des obstacles.
- button.py : Gère les boutons et les interactions de l'interface utilisateur. Ce fichier définit les propriétés des boutons et les rend interactifs.
- database.py : Contient des fonctions pour sauvegarder et récupérer le score ou d'autres informations de la base de données. Utile pour garder une trace des meilleurs scores.

### Étapes pour lancer le jeu
1. Clonez ce dépôt sur votre machine locale (GitHub Desktop)
2. Accédez au dossier du jeu
3. Lancez le fichier main.py


## Commandes du jeu
- **Flèche directionnel vers le haut** : Sauter

![Design sans titre (1)](https://github.com/user-attachments/assets/7978f2ec-7b63-485a-ad1e-f6012e73179e)
- **Maintenir la flèche directionnel vers le bas** : Esquiver

![Design sans titre (2)](https://github.com/user-attachments/assets/dc9abd33-c06d-41c2-acf0-f948c57655f6)

- **Échap** : Pour mettre la partie en Pause

![image](https://github.com/user-attachments/assets/0a9ef903-541b-4063-a0fa-50536155c9bb)


## Auteurs
- Nussbaum Théo (@TheoNussbaum)
- Ferreira Carlos (@CarlosFerreiraCPNV)
