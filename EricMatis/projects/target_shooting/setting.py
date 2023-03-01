import pygame
import constants as const


class ScreenSettings:
    """Класс для хранения настроек экрана игры Target Shooting"""

    def __init__(self, screen_width=const.SCREEN_WIDTH, screen_height=const.SCREEN_HEIGHT):
        """Инициализирует настройки экрана"""
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_size = (self.screen_width, self.screen_height)
        self.bg_color = const.BG_COLOR


class GameSettings:
    """Класс для хранения настроек игры Target Shooting"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры корабля
        self.ship_speed = const.SHIP_SPEED
        self.shots_limit = const.SHOTS_LIMIT

        # Параметры мишени
        self.target_color = const.TARGET_COLOR
        self.target_width = const.TARGET_WIDTH
        self.target_height = const.TARGET_HEIGHT
        self.target_speed = const.TARGET_SPEED
        self.target_direction = 1  # target_direction = 1 обозначает движение вниз, а -1 - вверх

        # Параметры снаряда
        self.bullet_speed = const.BULLET_SPEED
        self.bullet_width = const.BULLET_WIDTH
        self.bullet_height = const.BULLET_HEIGHT
        self.bullet_color = const.BULLET_COLOR
        self.bullets_allowed = const.BULLETS_ALLOWED  # Максимальное количество снарядов на экране
