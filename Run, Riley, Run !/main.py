"""
Auteur : Carlos Ferreira & Théo Nussbaum
Date : 27.10.2024
Projet : Run, Riley, Run!
Description : Fichier du système du jeu.

Sources Youtubes :
- PyGame Endless Vertical Platformer Beginner Tutorial in Python (Classe Joueur)
- Youtubeur "Max Rohowsky (Max on Tech)"
"""
from imports import *

pygame.init()

# Constantes pour la configuration de l'écran
screen_width = 1920
screen_height = 1080
fps = 60
screen = pygame.display.set_mode((screen_width, screen_height))

# Chargement des images de fond
city = pygame.image.load(r".\background\CITY.png").convert_alpha()
front = pygame.image.load(r".\background\FRONT.png").convert_alpha()
middle = pygame.image.load(r".\background\MIDDLE.png").convert_alpha()
sky = pygame.image.load(r".\background\SKY.png").convert_alpha()

# Initialisation des animations pour le joueur
running = [pygame.image.load(r".\running\step_1.png"),
           pygame.image.load(r".\running\step_2.png"),
           pygame.image.load(r".\running\step_3.png"),
           pygame.image.load(r".\running\step_4.png"),
           pygame.image.load(r".\running\step_5.png"),
           pygame.image.load(r".\running\step_6.png")]

bending_down = [pygame.image.load(r".\bending_down\step_1.png"),
           pygame.image.load(r".\bending_down\step_2.png"),
           pygame.image.load(r".\bending_down\step_3.png"),
           pygame.image.load(r".\bending_down\step_4.png"),
           pygame.image.load(r".\bending_down\step_5.png"),
           pygame.image.load(r".\bending_down\step_6.png"),
           pygame.image.load(r".\bending_down\step_7.png"),
           pygame.image.load(r".\bending_down\step_8.png")]

jumping = [pygame.image.load(r".\jumping\step_1.png"),
           pygame.image.load(r".\jumping\step_2.png"),
           pygame.image.load(r".\jumping\step_3.png"),
           pygame.image.load(r".\jumping\step_4.png"),
           pygame.image.load(r".\jumping\step_5.png"),
           pygame.image.load(r".\jumping\step_6.png"),]

# Initialisation des obstacles du jeu
pneu_obstacle = [pygame.image.load(r".\obstacles\Pneu_Obstacle.png")]

red_bird_obstacle = [pygame.image.load(r".\obstacles\1_rouge.png"),
                 pygame.image.load(r".\obstacles\2_rouge.png"),
                 pygame.image.load(r".\obstacles\3_rouge.png"),
                 pygame.image.load(r".\obstacles\4_rouge.png")]

blue_bird_obstacle = [pygame.image.load(r".\obstacles\1_bleu.png"),
                 pygame.image.load(r".\obstacles\2_bleu.png"),
                 pygame.image.load(r".\obstacles\3_bleu.png"),
                 pygame.image.load(r".\obstacles\4_bleu.png")]

purple_bird_obstacle = [pygame.image.load(r".\obstacles\1_violet.png"),
                 pygame.image.load(r".\obstacles\2_violet.png"),
                 pygame.image.load(r".\obstacles\3_violet.png"),
                 pygame.image.load(r".\obstacles\4_violet.png")]

pink_bird_obstacle = [pygame.image.load(r".\obstacles\1_rose.png"),
                 pygame.image.load(r".\obstacles\2_rose.png"),
                 pygame.image.load(r".\obstacles\3_rose.png"),
                 pygame.image.load(r".\obstacles\4_rose.png")]

green_bird_obstacle = [pygame.image.load(r".\obstacles\1_vert.png"),
                 pygame.image.load(r".\obstacles\2_vert.png"),
                 pygame.image.load(r".\obstacles\3_vert.png"),
                 pygame.image.load(r".\obstacles\4_vert.png")]

box_obstacles = [pygame.image.load(r".\obstacles\Caisse_Obstacle_1.png"),
                 pygame.image.load(r".\obstacles\Caisse_Obstacle_2.png"),
                 pygame.image.load(r".\obstacles\Caisse_Obstacle_3.png"),
                 pygame.image.load(r".\obstacles\Caisse_Obstacle_4.png")]

bird_obstacles = [red_bird_obstacle, blue_bird_obstacle, purple_bird_obstacle, pink_bird_obstacle]

# Initialisation des images du Menu Start et Rules
start_menu_bg_image = pygame.image.load(r".\images\bg_city_menu.png").convert()
start_menu_title_image = pygame.image.load(r".\images\title.png")
start_button_unpressed_image = pygame.image.load(r".\images\start_button_unpressed.png")
start_button_pressed_image = pygame.image.load(r".\images\start_button_pressed.png")
rules_button_unpressed_image = pygame.image.load(r".\images\rules_button_unpressed.png")
rules_button_pressed_image = pygame.image.load(r".\images\rules_button_pressed.png")
bg_rules = pygame.image.load(r".\images\bg_rules.png")

# Initialisation des images du Menu des Personnages
characters_bg_image = pygame.image.load(r".\images\bg_character_menu.png")
character_choice_1 = [pygame.image.load(r".\characters\Choice_1.0.png"),
                      pygame.image.load(r".\characters\Choice_1.1.png")]
character_choice_2 = [pygame.image.load(r".\characters\Choice_2.0.png"),
                      pygame.image.load(r".\characters\huey_lock.png"),
                      pygame.image.load(r".\characters\Choice_2.1.png")]
character_choice_3 = [pygame.image.load(r".\characters\Choice_3.0.png"),
                      pygame.image.load(r".\characters\Saitama_Lock.png"),
                      pygame.image.load(r".\characters\Choice_3.1.png")]

# Initialisation des images du Menu Pause et perdu
game_over = pygame.image.load(r".\images\Game_Over_2.png")
pause_menu = pygame.image.load(r".\images\Pause_menu.png")
resume_button_unpressed = pygame.image.load(r".\images\Resume_Unpressed.png")
resume_button_pressed = pygame.image.load(r".\images\Resume_pressed.png")
quit_button_unpressed = pygame.image.load(r".\images\Quit_Unpressed.png")
quit_button_pressed = pygame.image.load(r".\images\Quit_Pressed.png")
play_again_button_unpressed = pygame.image.load(r".\images\Play_Again_Unpressed.png")

# Initialisation des variables pour les Boutons
start_button = Button(662, 489, start_button_unpressed_image)
rules_button = Button(782, 803, rules_button_unpressed_image)
resume_button_img = resume_button_unpressed
quit_button_img = quit_button_unpressed

# Définition des variables du jeu
game_speed = 10
initial_game_speed = 10
game_score = 0
game_speed_backup = 0
start_menu = True
menu_close = False
game_pause = False
game_on = True
rules = False
y_pause = 488
x_pause = 659

# Initialisation des variables des polices d'écritures
font = pygame.font.Font(r".\police\Myfont-Regular.ttf", 50)
font_super_kinds = pygame.font.Font(r".\police\Super_Kinds.ttf", 50)

#######################################################################################################################
############################################### Classe du joueur ######################################################
#######################################################################################################################

# Classe pour le joueur avec ses mouvements et états
class Player:
    # Position du joueur par défaut
    x_pos = 100
    y_pos = 795

    def __init__(self):
        # Images pour chaque état du joueur
        self.bending_down_img = bending_down
        self.run_img = running
        self.jump_img = jumping

        self.temp = 0

        # État initial : course
        self.bending_down = False
        self.run = True
        self.jump = False
        self.alive = True

        # Position et image actuelles
        self.step_index = 0
        self.image = self.run_img[0]
        self.rect = pygame.Rect(100, 795, 150, 195)
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos

        # Variables pour les parametres du saut
        self.gravity = 0.8
        self.jump_height = 23
        self.velocity = self.jump_height
        self.run_index = 48
        self.index_speed = self.run_index

    # Met à jour l'état du joueur selon l'entrée utilisateur
    def update(self, user_input):
        if self.alive:
            if self.bending_down:
                self.bending_down_movement()

            if self.run:
                self.run_movement()

            if self.jump:
                self.jump_movement()

        # Si l'animation est fini recommencer
        if self.step_index >= self.index_speed:
            self.step_index = 0

        # Gestion du saut
        if user_input[pygame.K_UP] and not self.jump:
                self.bending_down = False
                self.run = False
                self.jump = True

        # Gestion de se baisser
        elif user_input[pygame.K_DOWN] and not self.jump:
            self.bending_down = True
            self.run = False
            self.jump = False

        # Gestion de la course automatique
        elif not (self.jump or user_input[pygame.K_DOWN]):
            self.bending_down = False
            self.run = True
            self.jump = False

    # Mouvement du personnage en se baissant
    def bending_down_movement(self):
        if not game_pause:
            self.rect = pygame.Rect(140, 925, 250, 50)
            self.image = self.bending_down_img[self.step_index // 8]
            self.x_pos = 100
            self.y_pos = 795 + 30
            self.step_index += 1
            self.temp += 1

    # Mouvement du personnage en course
    def run_movement(self):
        if not game_pause:
            self.rect = pygame.Rect(100, 795, 150, 195)
            self.x_pos = 100
            self.y_pos = 795
            self.image = self.run_img[self.step_index // 8]
            self.rect.x = self.x_pos
            self.rect.y = self.y_pos
            self.step_index += 1

    # Mouvement du personnage en sautant
    def jump_movement(self):
        if not game_pause:
            self.image = self.jump_img[self.step_index // 8]
            self.rect.y = self.y_pos
            self.y_pos -= self.velocity
            self.velocity -= self.gravity
            self.step_index += 1

            if self.velocity < - self.jump_height:
                self.jump = False
                self.velocity = self.jump_height

    # Dessine le joueur à l'écran
    def draw(self, screen_parameter):
        screen_parameter.blit(self.image, (self.x_pos, self.y_pos))


#######################################################################################################################
################################### Classe qui permet de créer des obstacles ##########################################
#######################################################################################################################

# Classe pour les obstacles
class Obstacle:
    global game_speed

    # Déclarations des variables d'initialisation de l'obstacle
    def __init__(self, image, type):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = screen_width

    # Mise à jour de la position de l'obstacle
    def update(self):
        self.rect.x -= game_speed

        # Supprime l'obstacle s'il est plus sur l'écran
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    # Affiche l'obstacle sur l'écran
    def draw(self, window):
        window.blit(self.image[self.type], self.rect)


#######################################################################################################################
####################################### Classes appartenant aux obstacles #############################################
#######################################################################################################################

# Classe de l'objet Caisse
class Box(Obstacle):
    # Choisi le type de la caisse aléatoirement, lui attribue une image et une position
    def __init__(self, image):
        self.type = random.randint(0, 3)
        super().__init__(image, self.type)
        self.rect.y = 880


# Classe de l'objet Pneu
class Tire(Obstacle):
    # Choisi le type de la Pneu, lui attribue une image et une position
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 875


# Classe de l'objet Oiseau
class Bird(Obstacle):
    # Choisi le type de la Oiseau, lui attribue une image et une position
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 735
        self.index = 0
        self.index_speed = 24
        self.alive = True

    def draw(self, window):
        if self.index >= self.index_speed:
            self.index = 0
        screen.blit(self.image[self.index // 6], self.rect)
        if self.alive:
            if not game_pause:
                self.index += 1
                self.rect.x -= (game_speed - 6)


# Fonction pour le quitter le jeu
def quit_game():
    global game_on
    game_on = False


# Fonction pour le lancement du Menu Pause
def resume_game():
    global game_pause, game_speed, game_speed_backup
    game_speed = game_speed_backup
    game_pause = False


#######################################################################################################################
########################################## Fonction de lancement du jeu ###############################################
#######################################################################################################################

# Fonction principale pour le lancement du jeu
def Game():
    global obstacles, game_speed, game_speed_backup, game_pause, y_pause, x_pause, resume_button_img, quit_button_img, game_on, obstacle, game_current_score
    timer = pygame.time.Clock()
    player = Player()

    # Image cordonnées
    sky_bg_x = 0
    city_bg_x = 0
    middle_bg_x = 0
    front_bg_x = 0

    # Initialisation des obstacles
    obstacles = []

    # Score
    game_score = 0

    # Fonction de calcul et d'affichage du score
    def Score():
        global game_score, game_speed, game_speed_backup, start_menu
        text_x = 1850
        text_score_x = 1685
        text_color = (255, 248, 189)

        # Si le joueur est vivant, le score augmente en continu
        if player.alive:
            if not game_pause:
                game_score += 10 # Augmente le score
                game_speed_backup = game_speed

            # Augmente la vitesse de jeu tous les 1000 points jusqu'à un maximum de 30
            if game_score % 1000 == 0:
                if game_speed <= 30:
                    game_speed += 0.3 # Accélère progressivement le jeu
                    game_score += 20

            # Ajuste les positions de texte en fonction du nombre de chiffres dans le score
            if game_score > 99:
                text_score_x = 1675

            if game_score > 999:
                text_x = 1825
                text_score_x = 1635

            if game_score > 9999:
                text_x = 1810
                text_score_x = 1595

            if game_score > 99999:
                text_x = 1795
                text_score_x = 1565

            # Création des textes de score et affichage à l'écran
            text_score = font.render("Score: ", True, text_color)
            text_score_rect = text_score.get_rect()
            text_score_rect.center = (text_score_x, 40)

            text = font.render(str(game_score), True, text_color)
            text_rect = text.get_rect()
            text_rect.center = (text_x, 40)  # 100000 = 1670 / 10000 = 1685 / 1000 = 1700 / 100 = 1725

            screen.blit(text_score, text_score_rect)
            screen.blit(text, text_rect)

            return game_score

    # Permet de relancer une partie à l'état de base
    def reset_game():
        global game_score, game_speed, obstacles
        game_score = 0
        player.alive = True
        game_speed = initial_game_speed  # Assuming you have an initial game speed variable
        obstacles.clear()  # Clear all current obstacles


    # Boucle principale du jeu
    while game_on:
        x_quit_coords = 787
        y_quit_coords = 784

        x_resume_coords = 659
        y_resume_coords = 488

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False

        # Récupération des entrées clavier
        user_input = pygame.key.get_pressed()

        # Quitte le jeu si la touche 'Q' est enfoncée
        if user_input[pygame.K_q]:
            game_on = False

        # Affichage des éléments de fond avec un défilement pour simuler le mouvement
        screen.blit(sky, (sky_bg_x, 0))
        screen.blit(city, (city_bg_x, 0))
        screen.blit(middle, (middle_bg_x, 0))
        screen.blit(front, (front_bg_x, 0))
        resume_button = Button(x_resume_coords, y_resume_coords, resume_button_img)
        quit_button = Button(x_quit_coords, y_quit_coords, quit_button_img)

        # Affichage et mise à jour du joueur
        player.draw(screen)
        player.update(user_input)

        # Si le joueur est en vie, met à jour le score et défile le fond
        if player.alive:
            # Met le jeu en pause avec la touche 'Échap'
            if user_input[pygame.K_ESCAPE]:
                game_pause = True

            # Met à jour le score
            game_current_score = Score()

            # Défile les images de fond pour créer un effet de mouvement
            if not game_pause:
                # Vitesse à laquelle le arrière plan vas défiler
                sky_bg_x += -abs(game_speed) + 3
                city_bg_x += -abs(game_speed) + 2
                middle_bg_x += -abs(game_speed) + 1
                front_bg_x += -abs(game_speed)

            # Réinitialise les images de fond lorsque leur fin est atteinte
            if sky_bg_x <= -1920:
                sky_bg_x = 0
            if city_bg_x <= -1824:
                city_bg_x = 0
            if middle_bg_x <= -1841:
                middle_bg_x = 0
            if front_bg_x <= -1850:
                front_bg_x = 0

            temp = random.randint(0, 3)

            # Gère l'apparition aléatoire des obstacles
            if len(obstacles) == 0:
                # Ajoute un obstacle aléatoire parmi les types disponibles
                if random.randint(0, 2) == 0:
                    obstacles.append(Box(box_obstacles))
                elif random.randint(0, 2) == 1:
                    obstacles.append(Bird(bird_obstacles[temp]))
                elif random.randint(0, 2) == 2:
                    obstacles.append(Tire(pneu_obstacle))


        # Affiche chaque obstacle et vérifie les collisions avec le joueur
        for obstacle in obstacles:
            obstacle.draw(screen)
            obstacle.update()

            # Si collision entre le joueur et l'obstacle, le joueur meurt et le jeu s'arrête
            if player.rect.colliderect(obstacle.rect):
                player.alive = False
                obstacle.alive = False
                game_speed = 0 # Arrête le défilement

        # Gère le menu de pause si le jeu est en pause
        if game_pause:
            game_speed = 0 # Arrête le défilement du jeu
            screen.blit(pause_menu, (0, 0))
            resume_button.draw(screen)
            quit_button.draw(screen)

            # Vérifie si le bouton de reprise est cliqué pour continuer
            if resume_button.clicked:
                resume_button_img = resume_button_pressed
                t_resume = Timer(0.15, resume_game)
                t_resume.start()

            # Vérifie si le bouton de quitter est cliqué pour terminer le jeu
            if quit_button.clicked:
                quit_button_img = quit_button_pressed
                t_quit = Timer(0.15, quit_game)
                t_quit.start()
        else:
            resume_button_img = resume_button_unpressed

        # Affichage de l'écran de Game Over si le joueur est mort
        if not player.alive:
            screen.blit(game_over, (0, 0))
            play_again_button = Button(450, 590, play_again_button_unpressed)
            play_again_button.draw(screen)

            # Vérifie si le score actuel est le meilleur score et le met à jour si nécessaire
            tuple_best_score = search_best_score()
            int_best_score = int(tuple_best_score[0])
            if game_current_score > int_best_score:
                edit_score(int(game_current_score))

            # Relance le jeu si le bouton "Rejouer" est cliqué
            if play_again_button.clicked:
                reset_game()

        # Limite la vitesse d'exécution à la valeur d'images par seconde (FPS)
        timer.tick(fps)

        # Rafraîchit l'affichage de l'écran
        pygame.display.update()

    # Quitte pygame à la fin de la boucle de jeu
    pygame.quit()


#######################################################################################################################
########################################## Lancement du Menu Personnages ##############################################
#######################################################################################################################

# Fonction qui affiche le menu de choix de personnages et permet au joueur de sélectionner un personnage
def Choice_Characters_Menu():
    global running

    # Variables d'état du menu et de gestion du temps
    characters_menu = True
    timer = pygame.time.Clock()
    temp = 0

    # Création des boutons pour chaque personnage
    character_1 = Button(564, 158, character_choice_1[0])
    character_2 = Button(0, 0, character_choice_2[2])
    character_3 = Button(0, 0, character_choice_3[2])

    # Boucle principale du menu de sélection des personnages
    while characters_menu:
        # Gère les événements, permet de quitter le menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                characters_menu = False

        # Récupération des entrées clavier
        user_input = pygame.key.get_pressed()

        # Quitte le menu de sélection de personnage si la touche 'Q' est enfoncée
        if user_input[pygame.K_q]:
            characters_menu = False

        # Affiche l'arrière-plan du menu des personnages
        screen.blit(characters_bg_image, (0, 0))

        # Vérifie si les scores requis sont atteints pour débloquer les personnages
        if search_score_to_unlock(1) <= search_best_score():
            edit_id_character(1)  # Débloque le personnage 1

        if search_score_to_unlock(2) <= search_best_score():
            edit_id_character(2)  # Débloque le personnage 2

        if search_score_to_unlock(3) <= search_best_score():
            edit_id_character(3)  # Débloque le personnage 3

        # Récupère l'ID du personnage sélectionné par l'utilisateur
        tuple_id_character = search_id_character()
        int_id_character = int(tuple_id_character[0])

        # Affiche les boutons pour chaque personnage et gère les interactions
        if temp > 6:
            character_1_state = character_1.draw(screen)
            # Change l'image du bouton si le personnage est sélectionné
            if character_1_state[1]:
                character_1 = Button(564, 158, character_choice_1[1])
            else:
                character_1 = Button(564, 158, character_choice_1[0])

            # Si le bouton du personnage 1 est cliqué, commence le jeu avec ce personnage
            if character_1_state[0]:
                characters_menu = False
                Game()

            # Gère l'affichage du personnage 2 ou d'un cadenas si verrouillé
            if int_id_character < 2:
                screen.blit(character_choice_2[1], (0, 0))  # Affiche le cadenas
            else:
                character_2_state = character_2.draw(screen)

                if character_2_state[1]:
                    character_2 = Button(0, 0, character_choice_2[2])
                else:
                    character_2 = Button(0, 0, character_choice_2[0])

                if character_2_state[0]:
                    # Définit les images de course pour le personnage 2
                    running = [pygame.image.load(r".\running\Huey_step_1.png"),
                               pygame.image.load(r".\running\Huey_step_2.png"),
                               pygame.image.load(r".\running\Huey_step_3.png"),
                               pygame.image.load(r".\running\Huey_step_4.png"),
                               pygame.image.load(r".\running\Huey_step_5.png"),
                               pygame.image.load(r".\running\Huey_step_6.png")]
                    characters_menu = False
                    Game()

            # Gère l'affichage du personnage 3 ou d'un cadenas si verrouillé
            if int_id_character < 3:
                screen.blit(character_choice_3[1], (0, 0))  # Affiche le cadenas
            else:
                character_3_state = character_3.draw(screen)

                if character_3_state[1]:
                    character_3 = Button(1200, 0, character_choice_3[2])
                else:
                    character_3 = Button(1200, 0, character_choice_3[0])

                if character_3_state[0]:
                    # Définit les images de course pour le personnage 3
                    running = [pygame.image.load(r".\running\saitama_step_1.png"),
                               pygame.image.load(r".\running\saitama_step_2.png"),
                               pygame.image.load(r".\running\saitama_step_3.png"),
                               pygame.image.load(r".\running\saitama_step_4.png"),
                               pygame.image.load(r".\running\saitama_step_5.png"),
                               pygame.image.load(r".\running\saitama_step_6.png")]
                    characters_menu = False
                    Game()

        # Augmente temporairement pour initialiser l'affichage du menu
        if temp <= 6:
            temp += 1

        # Limite la vitesse d'exécution de la boucle à la valeur FPS définie
        timer.tick(fps)

        # Rafraîchit l'affichage de l'écran
        pygame.display.update()

    # Quitte pygame lorsque le menu est fermé
    pygame.quit()


#######################################################################################################################
############################################# Lancement du Menu Start #################################################
#######################################################################################################################

# Fonction qui ferme le menu de démarrage et lance le jeu
def quit_start_menu():
    global start_menu
    start_menu = False


# Active l'affichage des règles du jeu dans le menu de démarrage
def turn_true_rules():
    global rules
    rules = True


# Désactive l'affichage des règles du jeu pour revenir au menu principal
def turn_false_rules():
    global rules
    rules = False


# Instance temporaire du joueur pour l'affichage dans le menu des règles
temp_player = Player()

# Boucle principale du menu de démarrage, s'affiche jusqu'à ce que le jeu commence
while start_menu:
    timer = pygame.time.Clock()

    # Gère les événements comme la fermeture de la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_menu = False

    # Récupère la position de la souris pour détecter les interactions avec les boutons
    mouse_pos = pygame.mouse.get_pos()

    # Quitte le menu de démarrage si la touche 'Q' est enfoncée
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_q]:
        start_menu = False

    # Affichage du menu principal si les règles ne sont pas actives
    if not rules:
        # Affichage des images
        screen.blit(start_menu_bg_image, (0, 0)) # Affiche le fond du menu de démarrage
        screen.blit(start_menu_title_image, (11, 52)) # Affiche le titre du jeu

        # Affiche les boutons de démarrage et de règles
        start_button.draw(screen)
        rules_button.draw(screen)

        # Si le bouton de démarrage est cliqué, lance le jeu en quittant le menu
        if start_button.clicked:
            start_button = Button(602, 489, start_button_pressed_image)
            t_start_menu = Timer(0.15, quit_start_menu)
            t_start_menu.start()
    else:
        # Affiche l'écran des règles si l'option est sélectionnée
        screen.blit(bg_rules, (0, 0))

        # Change la position du joueur temporaire pour la démonstration
        temp_player.x_pos = 830

        # Affiche les instructions des commandes
        jump_text = font_super_kinds.render("Jump", True, (0, 0, 0))
        jump_text_rect = jump_text.get_rect()
        jump_text_rect.x = 440
        jump_text_rect.y = 200

        bending_down_text = font_super_kinds.render("Bending Down", True, (0, 0, 0))
        bending_down_text_rect = jump_text.get_rect()
        bending_down_text_rect.x = 440
        bending_down_text_rect.y = 500

        pause_menu_text = font_super_kinds.render("Pause Menu", True, (0, 0, 0))
        pause_menu_text_rect = pause_menu_text.get_rect()
        pause_menu_text_rect.x = 440
        pause_menu_text_rect.y = 820

        screen.blit(jump_text, jump_text_rect)
        screen.blit(bending_down_text, bending_down_text_rect)
        screen.blit(pause_menu_text, pause_menu_text_rect)

        # Affiche le personnage temporaire pour démontrer les contrôles
        temp_player.draw(screen)
        temp_player.update(pressed)

        # Affiche le bouton de retour pour quitter l'écran des règles
        back_button = Button(1500, 120, quit_button_unpressed)
        back_button.draw(screen)
        if back_button.clicked:
            back_button = Button(1500, 500, quit_button_pressed)
            t_rules = Timer(0.15, turn_false_rules)
            t_rules.start()

    # Si le bouton de règles est cliqué, affiche l'écran des règles
    if rules_button.clicked:
        rules_button = Button(782, 803, rules_button_pressed_image)
        t_rules = Timer(0.15, turn_true_rules)
        t_rules.start()
    else:
        rules_button = Button(782, 803, rules_button_unpressed_image)

    # Rafraîchit l'affichage de l'écran du menu
    pygame.display.flip()

    # Limite la vitesse d'exécution de la boucle à la valeur d'images par seconde (FPS)
    timer.tick(fps)


# Démarre le menu de sélection de personnage une fois que le menu de démarrage est terminé
Choice_Characters_Menu()