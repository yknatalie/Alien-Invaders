import pygame
from pygame.sprite import Sprite
from settings import Settings


class Drop(Sprite):
    def __init__(self, drops_game):
        super().__init__()
        self.screen = drops_game.screen
        self.image = pygame.image.load('drops/images/drop.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.settings = drops_game.settings

    def update(self):
        self.y += self.settings.drop_speed
        self.rect.y = self.y
        if self.check_edges():
            self.y = 0

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            return True
