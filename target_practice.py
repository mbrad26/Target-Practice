import pygame
import game_functions as gf
from ship import Ship
from settings import Settings
from target import Target
from pygame.sprite import Group
from button import Button


pygame.init()
pygame.mixer.init()
settings = Settings()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption('Target Practice')
bullet_sound = pygame.mixer.Sound('sounds/Laser_Shoot.ogg')
target_sound = pygame.mixer.Sound('sounds/Pickup_Coin4.wav')
play_button = Button(screen, 'Play')

target = Target(settings, screen)
ship = Ship(settings, screen)
bullets = Group()


while True:
    # Events
    gf.check_events(ship, settings, screen, bullets, play_button, bullet_sound)

    # Updates)

    if settings.start_game:
        gf.target_edges(settings, target)
        bullets.update()
        target.update()
        ship.update()
        # gf.check_bullet_target(bullets, target, settings, target_sound)

    # Draw
    screen.fill(settings.screen_color)
    bullets.draw(screen)
    ship.blitme()
    target.draw_target()
    if not settings.start_game:
        play_button.draw_play_button()
    pygame.display.flip()




