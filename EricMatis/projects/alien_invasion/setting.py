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
        self.speedup_scale = const.SPEEDUP_SCALE

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = const.SHIP_SPEED
        self.bullet_speed_factor = const.BULLET_SPEED
        self.alien_speed_factor = const.ALIEN_SPEED
        self.fleet_direction = 1  # fleet_direction = 1 обозначает движение вправо, а -1 - влево

    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale


