import pygame
import game_functions as gf
from ship import Ship
from settings import Settings
from target import Target


pygame.init()
settings = Settings()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption('Target Practice')

target = Target(settings, screen)
ship = Ship(settings, screen)


while True:
    # Events
    gf.check_events(ship)

    # Updates)
    target.update()
    ship.update()

    # Draw
    screen.fill(settings.screen_color)
    ship.blitme()
    target.draw_target()
    pygame.display.flip()




