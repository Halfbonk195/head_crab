import sys
import pygame

import setting
from game_stats import GameStats
from ship import Ship
from target import Target
from button import Button
from bullet import Bullet


class TargetShooting:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.screen_settings = setting.ScreenSettings(screen_width=1500, screen_height=800)
        self.game_settings = setting.GameSettings()

        self.screen = pygame.display.set_mode(self.screen_settings.screen_size)
        pygame.display.set_caption('Target Shooting')

        # Создание экземпляра для хранения игровой статистики.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)

        # Создание кнопки Play.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_target()

            self._update_screen()

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.screen_settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.target.draw_target()

        # Кнопка Play отображается в том случае, если игра неактивна.
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        # Обновление позиций снарядов.
        self.bullets.update()

        # Удаление снарядов участвующих в коллизиях и вышедших за край экрана.
        collisions = 0
        for bullet in self.bullets.copy():
            if bullet.rect.colliderect(self.target):
                # Проверка столкновения с мишенью
                self.bullets.remove(bullet)
                self.game_settings.increase_speed()
                collisions += 1

            elif bullet.rect.left >= self.screen_settings.screen_width:
                # Проверка выхода снаряда за экран
                self.bullets.remove(bullet)
                if self.stats.shots_left > 1:
                    self.stats.shots_left -= 1
                else:
                    self.stats.game_active = False
                    pygame.mouse.set_visible(True)

    def _update_target(self):
        """Обновляет позицию мишени"""
        self._check_target_edges()
        self.target.update()

    def _check_target_edges(self):
        """Реагирует на достижение мишенью края экрана"""
        if self.target.check_edges():
            self.game_settings.target_direction *= -1

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Движение корабля
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            # Движение мыши
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True     # Переместить корабль вверх.
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True   # Переместить корабль вниз.
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()            # Выпустить снаряд.
        elif event.key == pygame.K_p:
            self._start_game()             # Начать новую игру.
        elif event.key == pygame.K_q:
            sys.exit()                     # Выход из игры.

    def _check_play_button(self, mouse_pos):
        """Проверяет нажатие кнопки Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _start_game(self):
        """Запускает новую игру"""
        # Сброс игровой статистики.
        self.stats.reset_stats()
        self.stats.game_active = True
        # Очистка списков пришельцев и снарядов.
        self.bullets.empty()
        # Создание новой мишени и размещение корабля в центре.
        self.target = Target(self)
        self.ship.center_ship()
        # Привидение динамических параметров к значениям по умолчанию
        self.game_settings.initialize_dynamic_settings()
        # Указатель мыши скрывается.
        pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        if self.stats.game_active:
            if len(self.bullets) < self.game_settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ts = TargetShooting()
    ts.run_game()