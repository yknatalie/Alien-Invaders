import pygame


class GameStats():
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True
        self.hit_ships = 0
        self.hit_aliens = 0
        self.spawned_alien_count = 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
