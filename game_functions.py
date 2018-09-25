import sys
import pygame
from bullet import Bullet


def fire_bullets(settings, screen, ship, bullets):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def check_key_down_events(event, ship, settings, screen, bullets):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_LEFT:
        ship.moving_up = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(settings, screen, ship, bullets)


def check_key_up_events(event, ship):
    if event.key == pygame.K_LEFT:
        ship.moving_up = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_down = False


def check_events(ship, settings, screen, bullets, play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ship, settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_x, mouse_y):
                settings.draw_button = False
                settings.start_game = True


def target_edges(settings, target):
    if target.rect.bottom >= target.screen_rect.bottom:
        settings.change_direction *= -1
    if target.rect.top <= target.screen_rect.top:
        settings.change_direction *= -1



