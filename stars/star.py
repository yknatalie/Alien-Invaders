import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self, stars_game):
        super().__init__()
        self.sreen = stars_game.screen
        self.image = pygame.image.load('stars/images/star.jpg')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
