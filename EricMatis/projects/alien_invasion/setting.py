import constants as const


class ScreenSettings:
    """Класс для хранения настроек экрана игры Alien Invasion."""

    def __init__(self, screen_width=const.SCREEN_WIDTH, screen_height=const.SCREEN_HEIGHT):
        """Инициализирует настройки экрана"""
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_size = (self.screen_width, self.screen_height)
        self.bg_color = const.BG_COLOR


class GameSettings:
    """Класс для хранения настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Настройки пришельцев
        self.fleet_drop_speed = const.DROP_SPEED

        # Параметры корабля
        self.ship_limit = const.SHIP_LIMIT  # Максимальное количество кораблей за игру

        # Параметры снаряда
        self.bullet_width = const.BULLET_WIDTH
        self.bullet_height = const.BULLET_HEIGHT
        self.bullet_color = const.BULLET_COLOR
        self.bullets_allowed = const.BULLETS_ALLOWED  # Максимальное количество снарядов на экране

        # Темп ускорения игры
        self.alien_speedup_scale = const.SPEEDUP_SCALE['alien']['Normal']
        self.ship_speedup_scale = const.SPEEDUP_SCALE['ship']['Normal']
        self.bullet_speedup_scale = const.SPEEDUP_SCALE['bullet']['Normal']
        # Темп роста стоимости пришельцев
        self.score_scale = const.SCORE_SCALE

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = const.SHIP_SPEED
        self.bullet_speed_factor = const.BULLET_SPEED
        self.alien_speed_factor = const.ALIEN_SPEED
        self.fleet_direction = 1  # fleet_direction = 1 обозначает движение вправо, а -1 - влево
        self.alien_points = const.ALIEN_POINTS

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев."""
        self.ship_speed_factor *= self.ship_speedup_scale
        self.bullet_speed_factor *= self.bullet_speedup_scale
        self.alien_speed_factor *= self.alien_speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


class MenuSettings:
    """Класс для хранения настроек главного меню"""

    def __init__(self, screen_width=const.SCREEN_WIDTH, screen_height=const.SCREEN_HEIGHT):
        """Инициализирует настройки главного меню"""
        self.buttons_coord = {}
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.delta_x, self.delta_y = self.screen_width // 8, self.screen_height // 8
        self.center_x, self.center_y = self.screen_width // 2, self.screen_height // 2

        self._calculate_main_menu_button_coordinates()
        self._calculate_settings_button_coordinates()
        self._calculate_difficulty_button_coordinates()
        self._calculate_other_button_coordinates()

    def _calculate_main_menu_button_coordinates(self):
        """Вычисляет координаты кнопок главного меню"""
        self.buttons_coord['play_button'] = (self.center_x, self.center_y - self.delta_y // 2)
        self.buttons_coord['settings_button'] = (self.center_x, self.center_y + self.delta_y // 2)
        self.buttons_coord['exit_button'] = (self.center_x, self.center_y + 3 * self.delta_y)

    def _calculate_settings_button_coordinates(self):
        """Вычисляет координаты кнопок меню настроек"""
        self.buttons_coord['resolution_button'] = (self.center_x, self.center_y - self.delta_y // 2)
        self.buttons_coord['difficulty_button'] = (self.center_x, self.center_y + self.delta_y // 2)

    def _calculate_difficulty_button_coordinates(self):
        """Вычисляет координаты кнопок настроек сложности"""
        self.buttons_coord['easy_button'] = (self.center_x, self.center_y - 3 * self.delta_y // 2)
        self.buttons_coord['normal_button'] = (self.center_x, self.center_y - self.delta_y // 2)
        self.buttons_coord['hard_button'] = (self.center_x, self.center_y + self.delta_y // 2)
        self.buttons_coord['impossible_button'] = (self.center_x, self.center_y + 3 * self.delta_y // 2)

    def _calculate_other_button_coordinates(self):
        """Вычисляет координаты вспомогательных кнопок меню"""
        self.buttons_coord['back_button'] = (self.center_x - 3 * self.delta_x, self.center_y - 3 * self.delta_y)
