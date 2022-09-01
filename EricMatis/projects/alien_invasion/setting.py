class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1900
        self.screen_height = 990
        self.bg_color = (11, 62, 62)
        # Параметры корабля
        self.ship_speed = 2.5
        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (238, 241, 34)
        self.bullets_allowed = 5
