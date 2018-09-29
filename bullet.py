import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, settings, screen, ship):

        super().__init__()

        self.ship = ship
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/laserGreen12.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = ship.rect.center
        self.rect.centery = ship.rect.centery
        self.center = float(self.rect.x)

    def update(self):
        self.center += self.settings.bullet_speed
        self.rect.x = self.center
        if self.rect.left >= self.settings.screen_width:
            self.kill()
            self.settings.missed -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

