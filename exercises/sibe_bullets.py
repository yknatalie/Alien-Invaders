import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ss):
        super().__init__()
        self.screen = ss.screen
        self.settings = ss.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_height,
                                self.settings.bullet_width)

        self.rect.midright = ss.ship.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
