import sys
import pygame

width = 1200
height = 800
bg_color = (200, 200, 255)

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Target Practice')


while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

    # Updates

    # Draw
    screen.fill(bg_color)
    pygame.display.flip()



