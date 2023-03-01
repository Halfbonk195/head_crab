class ScreenSettings:
    """Класс для хранения настроек экрана игры Alien Invasion."""

    def __init__(self, screen_width=1600, screen_height=900):
        """Инициализирует настройки экрана"""
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_size = (screen_width, screen_height)
        self.bg_color = (11, 62, 62)


class GameSettings:
    """Класс для хранения настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Настройки пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # fleet_direction = 1 обозначает движение вправо, а -1 - влево

        # Параметры корабля
        self.ship_speed = 2.5
        self.ship_limit = 3  # Максимальное количество кораблей за игру

        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (238, 241, 34)
        self.bullets_allowed = 500  # Максимальное количество снарядов на экране
