"""
Auteur : Carlos Ferreira & Théo Nussbaum
Date : 04.09.2024
Projet : Run, Riley, Run!
Description : Fichier du système du changement de personnage
"""
from threading import Timer

import pygame
from button import Button

pygame.init()

# Variables Constantes
screen_width = 1920
screen_height = 1080

fps = 60
test = False
menu_state = False

screen = pygame.display.set_mode((screen_width, screen_height))

bg_image = pygame.image.load(r".\images\bg_character_menu.png")

left_select_buttons = [pygame.image.load(r".\images\select_left_little.png"),
                       pygame.image.load(r".\images\select_left_big.png")]

right_select_buttons = [pygame.image.load(r".\images\select_right_little.png"),
                        pygame.image.load(r".\images\select_right_big.png")]

character_choice_1 = [pygame.image.load(r".\character_choice\Choice_1.0.png"),
                      pygame.image.load(r".\character_choice\Choice_1.1.png")]

# Le jeu
def Choice_Characters_Menu():
    game_on = True
    #menu_state = False
    timer = pygame.time.Clock()
    x = 430
    y = 435

    left_choice = Button(430, 435, left_select_buttons[0])
    choice = Button(564, 158, character_choice_1[0])


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
        if user_input[pygame.K_LEFT]:
            x -= 5
        if user_input[pygame.K_RIGHT]:
            x += 5
        if user_input[pygame.K_UP]:
            y -= 5
        if user_input[pygame.K_DOWN]:
            y += 5

        #print(f"x = {x} & y = {y}")

        # Affichage de l'arrière plan
        screen.blit(bg_image, (0, 0))

        left_choice_state = left_choice.draw(screen)
        choice_state = choice.draw(screen)


        if left_choice_state[1]:
            left_choice = Button(-195, 60, left_select_buttons[1])
        else:
            left_choice = Button(-195, 60, left_select_buttons[0])

        if choice_state[1]:
            choice = Button(564, 158, character_choice_1[1])
        else:
            choice = Button(564, 158, character_choice_1[0])

        if choice_state[0]:
            Run_Riley_Run_State = True
            game_on = False
            #menu_state = True

        #screen.blit(left_select_buttons[1], (x, y))

        # FPS
        timer.tick(fps)

        # Refresh de la page
        pygame.display.update()

    # QUIT
    pygame.quit()


Choice_Characters_Menu()