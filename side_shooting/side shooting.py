import pygame
from sibe_bullets import Bullet
from settings import Settings
import sys
from ship_side import Ship
from side_alien import Alien
from time import sleep
from game_stats import GameStats


class SideShooting():
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Side Shooting")
        self.stats = GameStats(self)
        self.ship = Ship(self.screen, self.settings)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self.finish()
                if self.stats.game_active:
                    self._update_aliens()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.screen_rect.width:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        for bullet, aliens in collisions.items():
            self.stats.hit_aliens += len(aliens)
        if not self.aliens:
            self.bullets.empty()

    def _update_aliens(self):
        if not self.aliens:
            self._create_fleet()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _ship_hit(self):
        self.stats.ships_left -= 1
        self.stats.hit_ships += 1
        self.aliens.empty()
        self.bullets.empty()
        self._create_fleet()
        sleep(0.5)

    def finish(self):
        if self.stats.hit_aliens >= self.stats.spawned_alien_count:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.left <= screen_rect.left:
                self._ship_hit()
                break

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        ship_height = self.ship.rect.height
        available_space_x = (self.settings.screen_width -
                             (3 * alien_width) - ship_height)
        available_space_y = self.settings.screen_height - (2 * alien_height)

        number_aliens_x = available_space_x // (2 * alien_width)

        number_rows = available_space_y // (2 * alien_height)
        self.stats.spawned_alien_count = number_rows * number_aliens_x
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        alien.y = alien_height + 2 * alien_height * row_number
        alien.x = self.settings.screen_width - \
            2 * alien_width * (alien_number + 1)

        alien.rect.y = alien.y
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    ss = SideShooting()
    ss.run_game()
