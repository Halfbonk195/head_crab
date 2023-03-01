from constants import ALIEN_SPEED, DROP_SPEED
from constants import SHIP_SPEED, SHIP_LIMIT
from constants import BULLET_SPEED, BULLET_WIDTH, BULLET_HEIGHT, BULLET_COLOR, BULLETS_ALLOWED
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR


class ScreenSettings:
    """Класс для хранения настроек экрана игры Alien Invasion."""

    def __init__(self, screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT):
        """Инициализирует настройки экрана"""
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_size = (self.screen_width, self.screen_height)
        self.bg_color = BG_COLOR


class GameSettings:
    """Класс для хранения настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Настройки пришельцев
        self.alien_speed = ALIEN_SPEED
        self.fleet_drop_speed = DROP_SPEED
        self.fleet_direction = 1  # fleet_direction = 1 обозначает движение вправо, а -1 - влево

        # Параметры корабля
        self.ship_speed = SHIP_SPEED
        self.ship_limit = SHIP_LIMIT  # Максимальное количество кораблей за игру

        # Параметры снаряда
        self.bullet_speed = BULLET_SPEED
        self.bullet_width = BULLET_WIDTH
        self.bullet_height = BULLET_HEIGHT
        self.bullet_color = BULLET_COLOR
        self.bullets_allowed = BULLETS_ALLOWED  # Максимальное количество снарядов на экране
