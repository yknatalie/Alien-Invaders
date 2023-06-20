import pygame
import sys
from settings import Settings
from bullets import Bullet
from ship import Ship
from button import Button
from target import Target
from game_stats import GameStats


class TargetShooting():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Target Shooting")
        self.stats = GameStats(self)
        self.ship = Ship(self.screen, self.settings)
        self.bullets = pygame.sprite.Group()
        self.play_button = Button(self, "Play")
        self.bullets = pygame.sprite.Group()
        self.target = Target(self.screen, self.settings)

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.target.update()
                self.ship.update()
                self._update_bullets()
                self._finish()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _collision_bullet_target(self):
        collision = pygame.sprite.spritecollideany(self.target, self.bullets)
        for bullet in self.bullets.sprites():
            if bullet == collision:
                self.bullets.remove(bullet)

    def _start_game(self):
        self.stats.reset_stats()
        self.stats.game_active = True
        self.bullets.empty()
        pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.settings.screen_width:
                self.bullets.remove(bullet)
                self.stats.miss_number -= 1
                self.settings.increase_speed()
        self._collision_bullet_target()

    def _finish(self):
        if self.stats.miss_number <= 0:
            self.stats.game_active = False
            self.bullets.empty()
            self.stats.reset_stats()
            pygame.mouse.set_visible(True)
            self.settings.initialize_dynamic_settings()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.target.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()


if __name__ == '__main__':
    ts = TargetShooting()
    ts.run_game()
