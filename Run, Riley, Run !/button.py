"""
Auteur : Carlos Ferreira & Théo Nussbaum
Date : 04.09.2024
Projet : Run, Riley, Run!
Description : Création d'une classe qui crée un bouton
"""
import pygame


class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.image_state = False

    # Dessine le bouton et gère les clics
    def draw(self, screen):
        # print(pos)
        pos = pygame.mouse.get_pos()
        self.image_state = False

        if self.rect.collidepoint(pos):
            self.image_state = True
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return self.clicked, self.image_state
