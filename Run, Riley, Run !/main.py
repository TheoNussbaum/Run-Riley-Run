"""
Auteur : Carlos Ferreira & Théo Nussbaum
Date : 06.09.2024
Projet : Run, Riley, Run!
Description : Fichier du système du jeu
"""
import pygame
import random
from button import Button

pygame.init()

# Variables Constantes
screen_width = 1920
screen_height = 1080
fps = 60
screen = pygame.display.set_mode((screen_width, screen_height))

CITY = pygame.image.load(r".\background\CITY.png").convert_alpha()
FRONT = pygame.image.load(r".\background\FRONT.png").convert_alpha()
MIDDLE = pygame.image.load(r".\background\MIDDLE.png").convert_alpha()
SKY = pygame.image.load(r".\background\SKY.png").convert_alpha()

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

obstacles_objects = [pygame.image.load(r".\obstacles\Poubelle_Obstacle.png"),
             pygame.image.load(r".\obstacles\Balle_Obstacle.png")]

Box_Obstacles = [pygame.image.load(r".\obstacles\Caisse_Obstacle_1.png"),
                 pygame.image.load(r".\obstacles\Caisse_Obstacle_2.png"),
                 pygame.image.load(r".\obstacles\Caisse_Obstacle_3.png")]

menu_bg_image = pygame.image.load(r".\images\bg_city_menu.png").convert()
title_image = pygame.image.load(r".\images\title.png")
start_unpressed_image = pygame.image.load(r".\images\start_button_unpressed.png")
start_pressed_image = pygame.image.load(r".\images\start_button_pressed.png")
rules_unpressed_image = pygame.image.load(r".\images\rules_button_unpressed.png")
rules_pressed_image = pygame.image.load(r".\images\rules_button_pressed.png")

start_button = Button(662, 489, start_unpressed_image)
rules_button = Button(782, 803, rules_unpressed_image)

# Variables
game_speed = 10
Run_Menu = True
menu_close = False

#######################################################################################################################
############################################### Classe du joueur ######################################################
#######################################################################################################################

class Player:
    # Position du joueur par défaut
    x_pos = 40  # jumping = 83  / running = 40
    y_pos = 795 # jumping = 620 / running = 795

    # Déclarations des variables d'initialisation du joueur
    def __init__(self):
        # Images des différents états du joueur
        self.bending_down_img = bending_down
        self.run_img = running
        self.jump_img = jumping

        # Dans quel état est le joueur
        self.player_bending_down = False
        self.player_run = True
        self.player_jump = False

        # Positionnement du joueur et l'image affiché
        self.step_index = 0
        self.image = self.run_img[0]
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.x_pos
        self.player_rect.y = self.y_pos

        # Variables pour les parametres du saut
        self.gravity = 1
        self.jump_height = 25
        self.velocity = self.jump_height
        self.run_index = 48
        self.index_speed = self.run_index

    # Cette fonction servira à mettre à jour l'état et l'image du personnage en fonction de ce qu'il fait dans le jeu.
    def update(self, user_input):
        if self.player_bending_down:
            self.bending_down()

        if self.player_run:
            self.run()

        if self.player_jump:
            self.jump()

        # Si l'animation est fini recommencer
        if self.step_index >= self.index_speed:
            self.step_index = 0

        # Si le joueur appuye pour sauter et que le joueur n'est pas dans les aires (n'a pas sauté), on vas donc dire que le joueur peut sauter
        if user_input[pygame.K_UP] and not self.player_jump:
                self.player_bending_down = False
                self.player_run = False
                self.player_jump = True

        # Si le joueur appuye pour se baisser et que le joueur n'est pas dans les aires (n'a pas sauté), on vas donc dire que le joueur peut se baisser
        elif user_input[pygame.K_DOWN] and not self.player_jump:
            self.player_bending_down = True
            self.player_run = False
            self.player_jump = False

        # Si le joueur n'est pas entrain dans les aires (n'a pas sauté) ou qu'il ne c'est pas baissé, on vas donc dire que le joueur peut courrir
        elif not (self.player_jump or user_input[pygame.K_DOWN]):
            self.player_bending_down = False
            self.player_run = True
            self.player_jump = False


    # Fonction pour se baisser
    def bending_down(self):
        self.image = self.bending_down_img[self.step_index // 8]
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.x_pos
        self.player_rect.y = self.y_pos + 30
        self.step_index += 1

    # Fonction pour courrir
    def run(self):
        self.player_rect.x = 40
        self.player_rect.y = 795
        self.image = self.run_img[self.step_index // 8]
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.x_pos
        self.player_rect.y = self.y_pos
        self.step_index += 1

    # Fonction pour sauter
    def jump(self):
        self.image = self.jump_img[self.step_index // 8]
        self.player_rect.y -= self.velocity
        self.velocity -= self.gravity
        self.step_index += 1

        if self.velocity < - self.jump_height:
            self.player_jump = False
            self.velocity = self.jump_height


    # Fonction pour afficher le personnage
    def draw(self, screen_parameter):
        screen_parameter.blit(self.image, (self.player_rect.x, self.player_rect.y))

#######################################################################################################################
################################### Classe qui permet de créer des obstacles ##########################################
#######################################################################################################################

class Obstacle:
    global player_alive

    # Déclarations des variables d'initialisation de l'obstacle
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = screen_width

    # Permet de mettre à jour l'emplacement de l'objet qui bouge
    def update(self):
        self.rect.x -= game_speed

        # Supprime l'obstacle s'il est plus sur l'écran
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    # Affiche l'obstacle sur l'écran
    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)

#######################################################################################################################
####################################### Classes appartenant aux obstacles #############################################
#######################################################################################################################

# Classe de l'objet Caisse
class Box(Obstacle):
    # Choisi le type de la caisse aléatoirement, lui attribue une image et une position
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 880


# Classe de l'objet Poubelle
class Trash(Obstacle):
    # Choisi le type de la poubelle, lui attribue une image et une position
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 830


# Classe de l'objet Balle
class Bullet(Obstacle):
    # Choisi le type de la balle, lui attribue une image et une position
    def __init__(self, image):
        self.type = 1
        super().__init__(image, self.type)
        self.rect.y = 780

#######################################################################################################################
########################################## Fonction de lancement du jeu ###############################################
#######################################################################################################################

def Run_Riley_Run():
    global obstacles
    game_on = True
    timer = pygame.time.Clock()
    player = Player()
    SKY_bg_x = 0
    CITY_bg_x = 0
    MIDDLE_bg_x = 0
    FRONT_bg_x = 0
    player_alive = True
    obstacles = []

    # Boucler tant que le jeu n'est pas fini
    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False

        # Keyboard Output
        user_input = pygame.key.get_pressed()

        # Quitter le jeu avec la touche Q
        if user_input[pygame.K_q]:
            game_on = False

        # Affichage de l'arrière plan
        screen.blit(SKY, (SKY_bg_x, 0))
        screen.blit(CITY, (CITY_bg_x, 0))
        screen.blit(MIDDLE, (MIDDLE_bg_x, 0))
        screen.blit(FRONT, (FRONT_bg_x, 0))

        # Vitesse à laquelle le arrière plan vas défiler
        SKY_bg_x += -7
        CITY_bg_x += -8
        MIDDLE_bg_x += -9
        FRONT_bg_x += -10

        # Si le joueur est toujours en vie et que l'arrière plan est arrivé à sa limite (-5350), on le reset on le mettant à nouveau au début (-1521)
        if player_alive:
            if SKY_bg_x <= -1920:
                SKY_bg_x = 0
            if CITY_bg_x <= -1824:
                CITY_bg_x = 0
            if MIDDLE_bg_x <= -1841:
                MIDDLE_bg_x = 0
            if FRONT_bg_x <= -1850:
                FRONT_bg_x = 0

        # S'il n'y a aucun obstacle dans la liste ajouter un obstacle aléatoirement
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(Box(Box_Obstacles))
            elif random.randint(0, 2) == 1:
                obstacles.append(Bullet(obstacles_objects))
            elif random.randint(0, 2) == 2:
                obstacles.append(Trash(obstacles_objects))

        # Affiche les obstacles sur l'écran et si le joueur est au même endroit que l'obstacle afficher la heatbox en rouge
        for obstacle in obstacles:
            obstacle.draw(screen)
            obstacle.update()
            if player.player_rect.colliderect(obstacle.rect):
                pygame.draw.rect(screen, (255, 0, 0), player.player_rect, 2)


        # Affichage de l'écran et mise à jour des inputs pour vérifier si on doit modifier l'état du personnage.
        player.draw(screen)
        player.update(user_input)

        # FPS
        timer.tick(fps)

        # Refresh de la page
        pygame.display.update()

    # QUIT
    pygame.quit()

#######################################################################################################################
############################################# Lancement du Menu Start #################################################
#######################################################################################################################

while Run_Menu:
    timer = pygame.time.Clock()
    wait = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run_Menu = False

    # Récupere la position de la souris
    mouse_pos = pygame.mouse.get_pos()

    # Ferme le jeu si on appuye sur Q
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_q]:
        Run_Menu = False

    # Affichage des images
    screen.blit(menu_bg_image, (0, 0))
    screen.blit(title_image, (11, 52))
    state = start_button.draw(screen)
    rules = rules_button.draw(screen)

    # Si on à ordonné de fermer la fenêtre et que l'image à déjà changé alors on ferme le menu et on ouvre le jeu
    if menu_close and start_button.image == start_pressed_image:
        Run_Menu = False
        # Run_Characters_Menu = True
        Run_Riley_Run_State = True

    # On change l'image du bouton
    if start_button.clicked:
        start_button = Button(665, 504, start_pressed_image)
        menu_close = True

    # On change l'image du bouton
    if rules_button.clicked:
        rules_button = Button(782, 803, rules_pressed_image)
    else:
        rules_button = Button(782, 803, rules_unpressed_image)

    # Mets à jour l'affichage
    pygame.display.flip()

    # FPS
    timer.tick(fps)


# Lancement du jeu
Run_Riley_Run()
