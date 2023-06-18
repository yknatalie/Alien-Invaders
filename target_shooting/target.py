import pygame


class Target():
    def __init__(self, screen, settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.image = pygame.Surface(
            (self.settings.target_width, self.settings.target_height))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.target_direction = 1

    def update(self):
        if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= self.screen_rect.top:
            self.target_direction *= -1
        self.y += self.settings.target_speed * self.target_direction
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
