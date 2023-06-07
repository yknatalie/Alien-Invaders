import pygame


class Gamer():
    def __init__(self, screen):
        self.screen = screen
        self.gamer_rect = screen.get_rect()

        self.image = pygame.image.load('alien_invasion/images/gamer.png')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = self.gamer_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
