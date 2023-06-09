import pygame
from settings import Settings
from drop import Drop
from random import randint
import sys


class DropsGame():
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Drops")
        self.drops = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self._update_drops()

            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_fleet(self):
        drop = Drop(self)
        drop_width, drop_height = drop.rect.size
        available_space_x = self.settings.screen_width - (2 * drop_width)
        number_drops_x = available_space_x // (2 * drop_width)
        available_space_y = (self.settings.screen_height -
                             (3 * drop_height))
        number_rows = available_space_y // (2 * drop_height)

        for row_number in range(number_rows):
            for drop_number in range(number_drops_x):
                self._create_drop(drop_number, row_number)

    def _create_drop(self, drop_number, row_number):
        drop = Drop(self)
        drop_width, drop_hight = drop.rect.size
        drop.x = drop_width + 2 * drop_width * drop_number
        drop.rect.x = drop.x
        drop.y = drop.rect.height + 2 * drop.rect.height * row_number
        self.drops.add(drop)

    def _update_drops(self):

        self.drops.update()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.drops.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    game = DropsGame()
    game.run_game()
