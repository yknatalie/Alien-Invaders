import pygame
from stars_settings import Settings
from star import Star
from random import randint
import sys


class StarsGame():
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Stars")
        self.stars = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_fleet(self):
        star = Star(self)
        number_of_cols = self.settings.screen_width // (star.rect.width * 2)
        number_of_rows = self.settings.screen_height // (star.rect.height * 2)
        for row_ind in range(number_of_rows):
            for col_ind in range(number_of_cols):
                a = randint(1, 100)
                if a > 10:
                    self._create_star(row_ind, col_ind)

    def _create_star(self, row_ind, col_ind):
        star = Star(self)
        hor_shift = col_ind * star.rect.width * 2
        ver_shift = row_ind * star.rect.height * 2
        star.rect.x = hor_shift + \
            randint(0, star.rect.width * 2 - star.rect.width)
        star.rect.y = ver_shift + \
            randint(0, star.rect.height * 2 - star.rect.height)
        self.stars.add(star)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    sg = StarsGame()
    sg.run_game()
