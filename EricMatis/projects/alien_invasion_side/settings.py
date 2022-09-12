class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Настройки пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        # Параметры экрана
        self.screen_width = 1900
        self.screen_height = 990
        self.bg_color = (11, 62, 62)
        # Параметры корабля
        self.ship_speed = 2.5
        # Параметры снаряда
        self.bullet_speed = 2
        self.bullet_width = 15
        self.bullet_height = 100
        self.bullet_color = (238, 241, 34)
        self.bullet_allowed = 50
