"""
Auteur : Carlos Ferreira & Théo Nussbaum
Date : 04.09.2024
Projet : Run, Riley, Run!
Description : Fichier du système du jeu
"""
import pygame
from button import Button

pygame.init()

# Variables Constantes
screen_width = 1920
screen_height = 1080

fps = 60

screen = pygame.display.set_mode((screen_width, screen_height))

bg_image = pygame.image.load(r".\images\bg_for_playing.png")
running = [pygame.image.load(r".\running\step_1.png"),
           pygame.image.load(r".\running\step_2.png"),
           pygame.image.load(r".\running\step_3.png"),
           pygame.image.load(r".\running\step_4.png"),
           pygame.image.load(r".\running\step_5.png"),
           pygame.image.load(r".\running\step_6.png")]
menu_bg_image = pygame.image.load(r".\images\bg_city_menu.png").convert()
title_image = pygame.image.load(r".\images\title.png")
start_unpressed_image = pygame.image.load(r".\images\start_button_unpressed.png")
start_pressed_image = pygame.image.load(r".\images\start_button_pressed.png")

Run_Menu = True
menu_close = False
start_button = Button(662, 489, start_unpressed_image)

# Class du joueur
class Player:
    x_pos = 40
    y_pos = 795

    def __init__(self):
        # Déclarations de variables pour le lancement de la class Player
        # self.duck_img = ducking
        self.run_img = running
        # self.jump_img = jumping

        self.player_duck = False
        self.player_run = True
        self.player_jump = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.x_pos
        self.player_rect.y = self.y_pos

    # Cette fonction servira à mettre à jour l'état et l'image du personnage en fonction de ce qu'il fait dans le jeu.
    def update(self, user_input):
        if self.player_duck:
            self.duck()
        if self.player_run:
            self.run()
        if self.player_jump:
            self.jump()

        # Si l'animation est fini recommencer
        if self.step_index >= 48:
            self.step_index = 0

        # Si le joueur appuye pour sauter et que le joueur n'est pas dans les aires (n'a pas sauté), on vas donc dire que le joueur peut sauter
        if user_input[pygame.K_UP] and not self.player_jump:
            self.player_duck = False
            self.player_run = False
            self.player_jump = True

        # Si le joueur appuye pour se baisser et que le joueur n'est pas dans les aires (n'a pas sauté), on vas donc dire que le joueur peut se baisser
        elif user_input[pygame.K_DOWN] and not self.player_jump:
            self.player_duck = True
            self.player_run = False
            self.player_jump = False

        # Si le joueur n'est pas entrain dans les aires (n'a pas sauté) ou qu'il ne c'est pas baissé, on vas donc dire que le joueur peut courrir
        elif not (self.player_jump or user_input[pygame.K_DOWN]):
            self.player_duck = False
            self.player_run = True
            self.player_jump = False

    # Fonction pour se baisser
    def duck(self):
        pass

    # Fonction pour courrir
    def run(self):
        # Parametre la vitesse du personnage
        self.image = self.run_img[self.step_index // 8]
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.x_pos
        self.player_rect.y = self.y_pos
        self.step_index += 1

    # Fonction pour sauter
    def jump(self):
        pass

    # Fonction pour afficher le personnage
    def draw(self, screen_parameter):
        screen_parameter.blit(self.image, (self.player_rect.x, self.player_rect.y))


# Le jeu
def Run_Riley_Run():
    game_on = True
    timer = pygame.time.Clock()
    player = Player()
    bg_x = 0
    player_alive = True

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
        screen.blit(bg_image, (bg_x, 0))

        # Vitesse à laquelle le arrière plan vas défiler
        bg_x += -10

        # Si le joueur est toujours en vie et que l'arrière plan est arrivé à sa limite (-5350), on le reset on le mettant à nouveau au début (-1521)
        if player_alive:
            if bg_x <= -5350:
                bg_x = -1521

        # Affichage de l'écran et mise à jour des inputs pour vérifier si on doit modifier l'état du personnage.
        player.draw(screen)
        player.update(user_input)

        # FPS
        timer.tick(fps)

        # Refresh de la page
        pygame.display.update()

    # QUIT
    pygame.quit()


while Run_Menu:
    timer = pygame.time.Clock()
    wait = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run_Menu = False

    mouse_pos = pygame.mouse.get_pos()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_q]:
        Run_Menu = False

    #print(f"x = {x} & y = {y}")

    screen.blit(menu_bg_image, (0, 0))
    screen.blit(title_image, (11, 52))
    state = start_button.draw(screen)

    if start_button.draw(screen):
        print("START!")

    print(start_button.clicked)

    # Si on à ordonné de fermer la fenêtre et que l'image à déjà changé alors on ferme le menu et on ouvre le jeu
    if menu_close and start_button.image == start_pressed_image:
        Run_Menu = False
        # Run_Characters_Menu = True
        Run_Riley_Run_State = True

    # On change l'image du bouton
    if start_button.clicked:
        start_button = Button(665, 504, start_pressed_image)
        menu_close = True


    pygame.display.flip()

    timer.tick(60)


# Lancement du jeu
Run_Riley_Run()
