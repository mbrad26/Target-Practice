import sys
import pygame


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_LEFT:
                ship.moving_up = True
            elif event.key == pygame.K_RIGHT:
                ship.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                ship.moving_up = False
            elif event.key == pygame.K_RIGHT:
                ship.moving_down = False