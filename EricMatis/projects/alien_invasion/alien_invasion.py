import sys
from time import sleep

import pygame

from setting import ScreenSettings, GameSettings, MenuSettings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
import constants as const


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()

        screen_info = pygame.display.Info()
        width = screen_info.current_w - 100
        height = screen_info.current_h - 100

        self.screen_settings = ScreenSettings(screen_width=width, screen_height=height)
        self.menu_settings = MenuSettings(screen_width=width, screen_height=height)
        self.game_settings = GameSettings()

        self.screen = pygame.display.set_mode(self.screen_settings.screen_size)
        self.screen_settings.screen_width = self.screen.get_rect().width
        self.screen_settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')

        # Создание экземпляра для хранения игровой статистики.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.buttons_main_menu = {}

        self._create_fleet()

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.screen_settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Кнопка Play отображается в том случае, если игра неактивна.
        if not self.stats.game_active:
            self._create_main_menu()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()

    def _create_main_menu(self):
        self._create_buttons_dicts()

        if self.stats.menu_state == 'main_menu':
            for button in self.buttons_main_menu.values():
                button.draw_button()
        elif self.stats.menu_state == 'settings_menu':
            for button in self.buttons_settings.values():
                button.draw_button()
            self.back_button.draw_button()
        elif self.stats.menu_state == 'resolution_menu':
            self.back_button.draw_button()
        elif self.stats.menu_state == 'difficulty_menu':
            for button in self.buttons_difficulty.values():
                button.draw_button()
            self.back_button.draw_button()

    def _create_buttons_dicts(self):
        """Создание словарей всех кнопок в игре"""
        coordinates = self.menu_settings.buttons_coord

        # Создание кнопок для главного меню
        self.buttons_main_menu = {
            'play_button': Button(self, 'Play', coordinates['play_button']),
            'settings_button': Button(self, 'Settings', coordinates['settings_button'], const.COLOR_GRAY),
            'exit_button': Button(self, 'Exit', coordinates['exit_button'], const.COLOR_GRAY),
        }

        # Создание кнопок для меню настроек.
        self.buttons_settings = {
            'difficulty_button': Button(self, 'Difficulty', coordinates['difficulty_button'], const.COLOR_GRAY),
            'resolution_button': Button(self, 'Resolution', coordinates['resolution_button'], const.COLOR_GRAY),
        }

        # Создание кнопок для уровней сложности, выделяем цветом текущий уровень сложности.
        current_difficulty_button = f'{self.stats.difficulty.lower()}_button'
        self.buttons_difficulty = {
            'easy_button': Button(self, 'Easy', coordinates['easy_button'], const.COLOR_GRAY),
            'normal_button': Button(self, 'Normal', coordinates['normal_button'], const.COLOR_GRAY),
            'hard_button': Button(self, 'Hard', coordinates['hard_button'], const.COLOR_GRAY),
            'impossible_button': Button(self, 'Impossible', coordinates['impossible_button'], const.COLOR_GRAY),
            current_difficulty_button: Button(self, self.stats.difficulty, coordinates[current_difficulty_button],
                                              const.COLOR_DARK_GRAY)
        }

        # Создание вспомогательных кнопок для меню.
        self.back_button = Button(self, 'Back', self.menu_settings.buttons_coord['back_button'], const.COLOR_DARK_GRAY)

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        # Обновление позиций снарядов.
        self.bullets.update()
        # Удаление снарядов, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Обработка коллизий снарядов с пришельцами"""
        # Удаление снарядов и пришельцев, участвующих в коллизиях.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Уничтожение существующих снарядов и создание нового флота
            self.bullets.empty()
            self._create_fleet()
            self.game_settings.increase_speed()

    def _update_aliens(self):
        """Обновляет позиции всех пришельцев во флоте."""
        self._check_fleet_edges()
        self.aliens.update()

        # Проверка коллизий "пришелец - корабль".
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Проверить, добрались ли пришельцы до нижнего края экрана.
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Обрабатывает столкновение коробля с пришельцем"""
        # Уменьшение ships_left.
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            # Очистка списков пришельцев и снарядов.
            self.aliens.empty()
            self.bullets.empty()

            # Создание нового флота и размещение коробля в центре.
            self._create_fleet()
            self.ship.center_ship()

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _create_fleet(self):
        """Создание флота вторжения."""
        # Создание пришельца и вычисление количества пришельцев в ряду
        # Интервал между соседними пришельцами равен ширине пришельца.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.screen_settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        available_space_y = (self.screen_settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Создание флота вторжения
        aliens = pygame.sprite.Group()
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number, aliens)
        self.aliens = aliens

    def _create_alien(self, alien_number, row_number, aliens):
        """Создание пришельца и размещение его в ряду."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        aliens.add(alien)

    def _check_aliens_bottom(self):
        """Проверяет, добрались ли пришельцы до нижнего края экрана."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Происходит то же, что при столкновении с кораблем.
                self._ship_hit()
                break

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление флота."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.game_settings.fleet_drop_speed
        self.game_settings.fleet_direction *= -1

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
                # self._check_play_button(mouse_pos)
                self._check_button_press(mouse_pos)

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True  # Переместить корабль вправо.
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True  # Переместить корабль влево.
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()  # Выпустить пулю.
        elif event.key == pygame.K_p:
            self._start_game()  # Начать новую игру.
        elif event.key == pygame.K_q:
            sys.exit()  # Выход из игры.

    def _check_button_press(self, mouse_pos):
        """Проверяет нажатие кнопок в меню"""
        if not self.stats.game_active:
            if self.stats.menu_state == 'main_menu':  # Главное меню
                self._handle_main_menu_click(mouse_pos)

            elif self.stats.menu_state == 'settings_menu':  # Меню настроек
                self._handle_settings_click(mouse_pos)

            elif self.stats.menu_state == 'resolution_menu':  # Меню разрешения экрана
                self._handle_resolution_click(mouse_pos)

            elif self.stats.menu_state == 'difficulty_menu':  # Меню изменения уровня сложности
                self._handle_difficulty_click(mouse_pos)

    def _handle_difficulty_click(self, mouse_pos):
        """Обработка нажатия кнопок в меню сложности игры"""
        buttons = self.buttons_difficulty
        # Нажатие кнопки Back.
        if self.back_button.rect.collidepoint(mouse_pos):
            self.stats.menu_state = 'settings_menu'
            self._update_screen()
        # Нажатие кнопки Easy
        elif buttons['easy_button'].rect.collidepoint(mouse_pos):
            self._change_difficulty_state('Easy')
        # Нажатие кнопки Normal
        elif buttons['normal_button'].rect.collidepoint(mouse_pos):
            self._change_difficulty_state('Normal')
        # Нажатие кнопки Hard
        elif buttons['hard_button'].rect.collidepoint(mouse_pos):
            self._change_difficulty_state('Hard')
        # Нажатие кнопки Impossible
        elif buttons['impossible_button'].rect.collidepoint(mouse_pos):
            self._change_difficulty_state('Impossible')

    def _handle_resolution_click(self, mouse_pos):
        """Обработка нажатия кнопок в меню изменения разрешения экрана"""
        # Нажатие кнопки Back.
        if self.back_button.rect.collidepoint(mouse_pos):
            self._change_menu_state('settings_menu')

    def _handle_settings_click(self, mouse_pos):
        """Обработка нажатия кнопок в меню настроек"""
        buttons = self.buttons_settings
        # Нажатие кнопки Back.
        if self.back_button.rect.collidepoint(mouse_pos):
            self._change_menu_state('main_menu')
        # Нажатие кнопки Resolution
        elif buttons['resolution_button'].rect.collidepoint(mouse_pos):
            self._change_menu_state('resolution_menu')
        # Нажатие кнопки Difficulty
        elif buttons['difficulty_button'].rect.collidepoint(mouse_pos):
            self._change_menu_state('difficulty_menu')

    def _handle_main_menu_click(self, mouse_pos):
        """Обработка нажатия кнопок в главном меню"""
        buttons = self.buttons_main_menu
        # Нажатие кнопки Play
        if buttons['play_button'].rect.collidepoint(mouse_pos):
            self._start_game()
        # Нажатие кнопки Settings
        elif buttons['settings_button'].rect.collidepoint(mouse_pos):
            self._change_menu_state('settings_menu')
        # Выход из игры
        elif buttons['exit_button'].rect.collidepoint(mouse_pos):
            sys.exit()

    def _change_menu_state(self, state_menu):
        """Изменяет состояние меню"""
        self.stats.menu_state = state_menu
        self._update_screen()

    def _change_difficulty_state(self, difficulty_state):
        """Изменяет уровень сложности игры"""
        self.stats.difficulty = difficulty_state
        self.game_settings.ship_speedup_scale = const.SPEEDUP_SCALE['ship'][difficulty_state]
        self.game_settings.alien_speedup_scale = const.SPEEDUP_SCALE['alien'][difficulty_state]
        self.game_settings.bullet_speedup_scale = const.SPEEDUP_SCALE['bullet'][difficulty_state]
        self._update_screen()

    def _start_game(self):
        """Запускает новую игру"""
        # Сброс игровой статистики.
        self.stats.reset_stats()
        self.stats.game_active = True
        # Очистка списков пришельцев и снарядов.
        self.aliens.empty()
        self.bullets.empty()
        # Создание нового флота и размещение корабля в центре.
        self._create_fleet()
        self.ship.center_ship()
        # Привидение динамических параметров к значениям по-умолчанию
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
    ai = AlienInvasion()
    ai.run_game()
