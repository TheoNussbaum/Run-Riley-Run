"""
Auteur : Carlos Ferreira & Théo Nussbaum
Date : 06.09.2024
Projet : Run, Riley, Run!
"""
import pygame

pygame.init()

class Button():
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False


        def draw(self):
            image_state = False
            action = False
            pos = pygame.mouse.get_pos()
            #print(pos)

            if self.rect.collidepoint(pos):
                image_state = True
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True

            if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False

            screen.blit(self.image, (self.rect.x, self.rect.y))
            return action, image_state


screen_width = 1920
screen_height = 1080

screen = pygame.display.set_mode((screen_width, screen_height))
game_on = True

timer = pygame.time.Clock()

bg_image = pygame.image.load(r".\images\bg_city_menu.png").convert()
title_image = pygame.image.load(r".\images\title.png")
start_unpressed_image = pygame.image.load(r".\images\start_button_unpressed.png")
start_pressed_image = pygame.image.load(r".\images\start_button_pressed.png")
rules_unpressed_image = pygame.image.load(r".\images\rules_button_unpressed.png")
rules_pressed_image = pygame.image.load(r".\images\rules_button_pressed.png")

x = 330
y = 522

start_button = Button(662, 489, start_unpressed_image)
rules_button = Button(330, 522, rules_unpressed_image)


while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

    mouse_pos = pygame.mouse.get_pos()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        x -= 1
    if pressed[pygame.K_RIGHT]:
        x += 1
    if pressed[pygame.K_UP]:
        y -= 1
    if pressed[pygame.K_DOWN]:
        y += 1
    if pressed[pygame.K_q]:
        game_on = False

    print(f"x = {x} & y = {y}")

    screen.blit(bg_image, (0, 0))
    screen.blit(title_image, (11, 52))
    state = start_button.draw()
    rules = rules_button.draw()

    print(start_button.clicked)

    if start_button.clicked:
        start_button = Button(665, 504, start_pressed_image)
    else:
        start_button = Button(665, 504, start_unpressed_image)

    if rules_button.clicked:
        rules_button = Button(782, 803, rules_pressed_image)
    else:
        rules_button = Button(782, 803, rules_unpressed_image)


    pygame.display.flip()

    timer.tick(60)


pygame.quit()
