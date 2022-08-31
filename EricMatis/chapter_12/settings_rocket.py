class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1900
        self.screen_height = 990
        self.bg_color = (11, 62, 62)
        self.ship_speed = 2.5
