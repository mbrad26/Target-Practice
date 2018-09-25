import pygame
import game_functions as gf
from ship import Ship
from settings import Settings
from target import Target
from pygame.sprite import Group
from button import Button


pygame.init()
settings = Settings()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption('Target Practice')
play_button = Button(screen, 'Play')

target = Target(settings, screen)
ship = Ship(settings, screen)
bullets = Group()


while True:
    # Events
    gf.check_events(ship, settings, screen, bullets, play_button)

    # Updates)

    gf.target_edges(settings, target)
    if settings.start_game:
        bullets.update()
        target.update()
    ship.update()

    # Draw
    screen.fill(settings.screen_color)
    bullets.draw(screen)
    ship.blitme()
    target.draw_target()
    if settings.draw_button:
        play_button.draw_play_button()
    pygame.display.flip()




