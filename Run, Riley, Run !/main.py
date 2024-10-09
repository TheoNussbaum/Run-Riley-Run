"""
Auteur : Carlos Ferreira & Théo Nussbaum
Date : 04.10.2024
Projet : Run, Riley, Run!
Description : Fichier du système du jeu.
"""
import pygame.image
from pygame.examples.aliens import Player
from database import *

from imports import *

pygame.init()

# Variables Constantes
screen_width = 1920
screen_height = 1080
fps = 60

screen = pygame.display.set_mode((screen_width, screen_height))

# Images

city = pygame.image.load(r".\background\CITY.png").convert_alpha()
front = pygame.image.load(r".\background\FRONT.png").convert_alpha()
middle = pygame.image.load(r".\background\MIDDLE.png").convert_alpha()
sky = pygame.image.load(r".\background\SKY.png").convert_alpha()

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

start_menu_bg_image = pygame.image.load(r".\images\bg_city_menu.png").convert()
start_menu_title_image = pygame.image.load(r".\images\title.png")

start_button_unpressed_image = pygame.image.load(r".\images\start_button_unpressed.png")
start_button_pressed_image = pygame.image.load(r".\images\start_button_pressed.png")

rules_button_unpressed_image = pygame.image.load(r".\images\rules_button_unpressed.png")
rules_button_pressed_image = pygame.image.load(r".\images\rules_button_pressed.png")

# Characters
characters_bg_image = pygame.image.load(r".\images\bg_character_menu.png")

bg_rules = pygame.image.load(r".\images\bg_rules.png")

left_select_buttons = [pygame.image.load(r".\images\select_left_little.png"),
                       pygame.image.load(r".\images\select_left_big.png")]

right_select_buttons = [pygame.image.load(r".\images\select_right_little.png"),
                        pygame.image.load(r".\images\select_right_big.png")]

characters_locked = [pygame.image.load(r".\images\lock.png")]

character_choice_1 = [pygame.image.load(r".\characters\Choice_1.0.png"),
                      pygame.image.load(r".\characters\Choice_1.1.png")]

character_choice_2 = [pygame.image.load(r".\characters\Choice_2.0.png")]


character_choice_3 = [pygame.image.load(r".\characters\Choice_3.0.png")]

game_over = pygame.image.load(r".\images\Game_Over_2.png")

pause_menu = pygame.image.load(r".\images\Pause_menu.png")

resume_button_unpressed = pygame.image.load(r".\images\Resume_Unpressed.png")
resume_button_pressed = pygame.image.load(r".\images\Resume_pressed.png")

quit_button_unpressed = pygame.image.load(r".\images\Quit_Unpressed.png")
quit_button_pressed = pygame.image.load(r".\images\Quit_Pressed.png")

play_again_button_unpressed = pygame.image.load(r".\images\Play_Again_Unpressed.png")

start_button = Button(662, 489, start_button_unpressed_image)
rules_button = Button(782, 803, rules_button_unpressed_image)

resume_button_img = resume_button_unpressed
quit_button_img = quit_button_unpressed

# Variables
game_speed = 10
game_score = 0
game_speed_backup = 0
start_menu = True
menu_close = False
game_pause = False
game_on = True
rules = False

y_pause = 488
x_pause = 659


#######################################################################################################################
############################################### Classe du joueur ######################################################
#######################################################################################################################

class Player:
    # Position du joueur par défaut
    x_pos = 100  # jumping = 83  / running = 40
    y_pos = 795 # jumping = 620 / running = 795

    # Déclarations des variables d'initialisation du joueur
    def __init__(self):
        # Images des différents états du joueur
        self.bending_down_img = bending_down
        self.run_img = running
        self.jump_img = jumping

        self.temp = 0

        # Dans quel état est le joueur
        self.player_bending_down = False
        self.player_run = True
        self.player_jump = False
        self.player_alive = True

        # Positionnement du joueur et l'image affiché
        self.step_index = 0
        self.image = self.run_img[0]
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.x_pos
        self.player_rect.y = self.y_pos

        # Variables pour les parametres du saut
        self.gravity = 0.8
        self.jump_height = 23
        self.velocity = self.jump_height
        self.run_index = 48
        self.index_speed = self.run_index

    # Cette fonction servira à mettre à jour l'état et l'image du personnage en fonction de ce qu'il fait dans le jeu.
    def update(self, user_input):
        if self.player_alive:
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
        if not game_pause:
            self.image = self.bending_down_img[self.step_index // 8]
            self.player_rect = self.image.get_rect()
            self.player_rect.x = self.x_pos
            self.player_rect.y = self.y_pos + 30
            self.step_index += 1
            self.temp += 1

    # Fonction pour courrir
    def run(self):
        if not game_pause:
            self.player_rect.x = 100
            self.player_rect.y = 795
            self.image = self.run_img[self.step_index // 8]
            self.player_rect = self.image.get_rect()
            self.player_rect.x = self.x_pos
            self.player_rect.y = self.y_pos
            self.step_index += 1

    # Fonction pour sauter
    def jump(self):
        if not game_pause:
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
    def draw(self, window):
        screen.blit(self.image[self.type], self.rect)


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
        self.player_alive = True

    def draw(self, window):
        if self.index >= self.index_speed:
            self.index = 0
        screen.blit(self.image[self.index // 6], self.rect)
        if self.player_alive:
            if not game_pause:
                self.index += 1
                self.rect.x -= 4


def quit_game():
    global game_on
    game_on = False


def resume_game():
    global game_pause, game_speed, game_speed_backup
    game_speed = game_speed_backup
    game_pause = False


#######################################################################################################################
########################################## Fonction de lancement du jeu ###############################################
#######################################################################################################################

def Game():
    global obstacles, game_speed, game_speed_backup, game_pause, y_pause, x_pause, resume_button_img, quit_button_img, game_on, obstacle
    timer = pygame.time.Clock()

    # Joueur
    player = Player()

    # Image cordonnées
    sky_bg_x = 0
    city_bg_x = 0
    middle_bg_x = 0
    front_bg_x = 0

    # Liste des obstacles
    obstacles = []

    # Score
    game_score = 0
    font = pygame.font.Font(r".\police\Myfont-Regular.ttf", 50)

    def Score():
        global game_score, game_speed, game_speed_backup, start_menu
        text_x = 1850
        text_score_x = 1685
        text_color = (255, 248, 189)

        if player.player_alive:
            if not game_pause:
                game_score += 1
                game_speed_backup = game_speed

            if game_score % 1000 == 0:
                game_speed += 1
                game_score += 100

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

            text_score = font.render("Score: ", True, text_color)
            text = font.render(str(game_score), True, text_color)
            text_score_rect = text_score.get_rect()
            text_score_rect.center = (text_score_x, 40)

            text_rect = text.get_rect()
            text_rect.center = (text_x, 40) # 100000 = 1670 / 10000 = 1685 / 1000 = 1700 / 100 = 1725
            screen.blit(text_score, text_score_rect)
            screen.blit(text, text_rect)

            return game_score

    # Boucler tant que le jeu n'est pas fini
    while game_on:
        x_quit_coords = 787
        y_quit_coords = 784

        x_resume_coords = 659
        y_resume_coords = 488

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False

        # Keyboard Output
        user_input = pygame.key.get_pressed()

        # Quitter le jeu avec la touche Q
        if user_input[pygame.K_q]:
            game_on = False

        # Affichage de l'arrière plan
        screen.blit(sky, (sky_bg_x, 0))
        screen.blit(city, (city_bg_x, 0))
        screen.blit(middle, (middle_bg_x, 0))
        screen.blit(front, (front_bg_x, 0))
        resume_button = Button(x_resume_coords, y_resume_coords, resume_button_img)
        quit_button = Button(x_quit_coords, y_quit_coords, quit_button_img)

        # Affichage de l'écran et mise à jour des inputs pour vérifier si on doit modifier l'état du personnage.
        player.draw(screen)
        player.update(user_input)

        # Si le joueur est toujours en vie et que l'arrière plan est arrivé à sa limite (-5350), on le reset on le mettant à nouveau au début (-1521)
        if player.player_alive:
            if user_input[pygame.K_ESCAPE]:
                game_pause = True

            game_current_score = Score()

            if not game_pause:
                # Vitesse à laquelle le arrière plan vas défiler
                sky_bg_x += -abs(game_speed) + 3
                city_bg_x += -abs(game_speed) + 2
                middle_bg_x += -abs(game_speed) + 1
                front_bg_x += -abs(game_speed)

            if sky_bg_x <= -1920:
                sky_bg_x = 0
            if city_bg_x <= -1824:
                city_bg_x = 0
            if middle_bg_x <= -1841:
                middle_bg_x = 0
            if front_bg_x <= -1850:
                front_bg_x = 0

            temp = random.randint(0, 3)

            # S'il n'y a aucun obstacle dans la liste ajouter un obstacle aléatoirement
            if len(obstacles) == 0:
                if random.randint(0, 2) == 0:
                    obstacles.append(Box(box_obstacles))
                elif random.randint(0, 2) == 1:
                    obstacles.append(Box(box_obstacles))
                    #obstacles.append(Bird(bird_obstacles[temp]))
                elif random.randint(0, 2) == 2:
                    obstacles.append(Tire(pneu_obstacle))


        # Affiche les obstacles sur l'écran et si le joueur est au même endroit que l'obstacle afficher la heatbox en rouge
        for obstacle in obstacles:
            obstacle.draw(screen)
            obstacle.update()

            if player.player_rect.colliderect(obstacle.rect):
                pygame.draw.rect(screen, (255, 0, 0), player.player_rect, 2)
                player.player_alive = False
                obstacle.player_alive = False
                game_speed = 0

        if game_pause:
            game_speed = 0
            screen.blit(pause_menu, (0, 0))
            resume_button.draw(screen)
            quit_button.draw(screen)

            if resume_button.clicked:
                resume_button_img = resume_button_pressed

                t_resume = Timer(0.15, resume_game)
                t_resume.start()



            if quit_button.clicked:
                quit_button_img = quit_button_pressed
                t_quit = Timer(0.15, quit_game)
                t_quit.start()
        else:
            resume_button_img = resume_button_unpressed

        print(game_current_score)

        if not player.player_alive:
            screen.blit(game_over, (0, 0))
            play_again_button = Button(0, 0, play_again_button_unpressed)
            play_again_button.draw(screen)

            tuple_best_score = search_best_score()
            int_best_score = int(tuple_best_score[0])

            if game_current_score > int_best_score:
                edit_score(int(game_current_score))

            if play_again_button.clicked:
                player.player_alive = True

        # FPS
        timer.tick(fps)

        # Refresh de la page
        pygame.display.update()

    # QUIT
    pygame.quit()


#######################################################################################################################
########################################## Lancement du Menu Personnages ##############################################
#######################################################################################################################

def Choice_Characters_Menu():
    characters_menu = True
    timer = pygame.time.Clock()
    temp = 0

    left_choice = Button(575, 435, left_select_buttons[0])
    right_choice = Button(1175, 439, right_select_buttons[0])
    character_1 = Button(564, 158, character_choice_1[0])
    character_2 = Button(430, 435, character_choice_2[0])
    character_3 = Button(1395, 475, character_choice_3[0])

    # Boucler tant que le jeu n'est pas fini
    while characters_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                characters_menu = False

        # Keyboard Output
        user_input = pygame.key.get_pressed()

        # Quitter le jeu avec la touche Q
        if user_input[pygame.K_q]:
            characters_menu = False

        # Affichage de l'arrière plan
        screen.blit(characters_bg_image, (0, 0))

        left_choice_state = left_choice.draw(screen)
        right_choice_state = right_choice.draw(screen)

        if search_score_to_unlock(2) >= search_best_score():
            screen.blit(pygame.image.load(r".\images\lock.png"), (430, 435))
        else:
            character_2.draw(screen)

        if search_score_to_unlock(3) >= search_best_score():
            screen.blit(pygame.image.load(r".\images\lock.png"), (1395, 475))
        else:
            character_3.draw(screen)

        if temp > 6:
            character_1_state = character_1.draw(screen)
            if character_1_state[1]:
                character_1 = Button(564, 158, character_choice_1[1])
            else:
                character_1 = Button(564, 158, character_choice_1[0])

            if left_choice_state[1]:
                left_choice = Button(575, 435, left_select_buttons[1])
            else:
                left_choice = Button(575, 435, left_select_buttons[0])

            if right_choice_state[1]:
                right_choice = Button(1175, 439, right_select_buttons[1])
            else:
                right_choice = Button(1175, 439, right_select_buttons[0])

            if character_1_state[0]:
                characters_menu = False
                Game()

        if temp <= 6:
            temp += 1

        # FPS
        timer.tick(fps)

        # Refresh de la page
        pygame.display.update()

    # QUIT
    pygame.quit()

#######################################################################################################################
############################################# Lancement du Menu Start #################################################
#######################################################################################################################


def quit_start_menu():
    global start_menu
    start_menu = False


def turn_true_rules():
    global rules
    rules = True


def turn_false_rules():
    global rules
    rules = False


temp_player = Player()

while start_menu:
    timer = pygame.time.Clock()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_menu = False

    game_pause = False

    # Récupere la position de la souris
    mouse_pos = pygame.mouse.get_pos()

    # Ferme le jeu si on appuye sur Q
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_q]:
        start_menu = False

    if not rules:
        # Affichage des images
        screen.blit(start_menu_bg_image, (0, 0))
        screen.blit(start_menu_title_image, (11, 52))
        start_button.draw(screen)
        rules_button.draw(screen)

        # On change l'image du bouton
        if start_button.clicked:
            start_button = Button(602, 489, start_button_pressed_image)
            t_start_menu = Timer(0.15, quit_start_menu)
            t_start_menu.start()
    else:
        screen.blit(bg_rules, (0, 0))
        temp_player.player_rect.x = 830

        temp_player.draw(screen)
        temp_player.update(pressed)

        back_button = Button(1500, 500, quit_button_unpressed)
        back_button.draw(screen)
        if back_button.clicked:
            back_button = Button(1500, 500, quit_button_pressed)
            t_rules = Timer(0.15, turn_false_rules)
            t_rules.start()

    # On change l'image du bouton
    if rules_button.clicked:
        rules_button = Button(782, 803, rules_button_pressed_image)
        t_rules = Timer(0.15, turn_true_rules)
        t_rules.start()
    else:
        rules_button = Button(782, 803, rules_button_unpressed_image)

    # Mets à jour l'affichage
    pygame.display.flip()

    # FPS
    timer.tick(fps)

Choice_Characters_Menu()