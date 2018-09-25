import pygame


class Ship:

    def __init__(self, settings, screen):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        self.image = pygame.image.load('images/blueship.png').convert_alpha()
        self.image.set_colorkey((200, 200, 255))
        self.rect = self.image.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery
        self.speedy = float(self.rect.centery)
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top >= 0:
            self.speedy -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.speedy += self.settings.ship_speed
        self.rect.centery = self.speedy

    def blitme(self):
        self.screen.blit(self.image, self.rect)