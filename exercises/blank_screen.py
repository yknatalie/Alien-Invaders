import pygame
from settings import Settings
import sys


class BlankScreen():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.text = None
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Blank Screen')
        self.screen_rect = self.screen.get_rect()
        self.f1 = pygame.font.Font(None, 100)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.text = self.f1.render(str(event.key), True, (220, 0, 220))

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        if self.text != None:
            (w, h) = self.text.get_size()
            coord = (self.screen_rect.centerx -
                     w/2, self.screen_rect.centery - h/2)
            self.screen.blit(self.text, coord)
        pygame.display.flip()


if __name__ == '__main__':
    bs = BlankScreen()
    bs.run_game()
