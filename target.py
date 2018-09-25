import pygame


class Target:

    def __init__(self, settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.rect = pygame.Rect(0, 0, 30, 100)
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right - 10
        self.center = float(self.rect.y)
        # self.speedy = 1

    def update(self):

        self.center -= self.settings.target_speed * self.settings.change_direction
        self.rect.y = self.center

    def draw_target(self):
        pygame.draw.rect(self.screen, (60, 60, 60), self.rect)