import pygame


class Button:

    def __init__(self, screen, msg):

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.bg_color = (25, 89, 255)
        self.text_color = (200, 150, 150)
        self.font = pygame.font.SysFont(None, 45)

        self.rect = pygame.Rect(0, 0, 150, 50)
        self.rect.center = self.screen_rect.center

        self.msg_image = self.font.render(msg, True, self.text_color, self.bg_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_play_button(self):
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
