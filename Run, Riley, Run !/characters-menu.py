import pygame
from pygame.examples.cursors import image

pygame.init()

#crée la fênetre
pygame.display.set_caption("Run, Riley, Run !")
screen = pygame.display.set_mode((1920, 1080))

#importer les image
background = pygame.image.load("City1.png")

running =True

#boucle pour laisser la fênetre ouverte
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    #mettre a jour
    pygame.display.flip()

pygame.quit()