import pygame
from pygame.sprite import Sprite


class Target(Sprite):
    """Класс для управления мишенью"""

    def __init__(self, ts_game):
        """Инициализирует мишень и задает ее начальную позицию"""
        super().__init__()
        self.screen = ts_game.screen
        self.screen_rect = self.screen.get_rect()
        self.game_settings = ts_game.game_settings
        self.color = self.game_settings.target_color

        # Создание мишени в центре правой границы экрана
        self.rect = pygame.Rect(0, 0, self.game_settings.target_width, self.game_settings.target_height)
        self.rect.midright = self.screen_rect.midright

        self.y = float(self.rect.y)

    def update(self):
        """Перемещает мишень вертикально"""
        self.y += (self.game_settings.target_speed * self.game_settings.target_direction)
        self.rect.y = self.y

    def check_edges(self):
        """Возвращает True, если мишень находится у края экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.top <= 0 or self.rect.bottom >= screen_rect.bottom:
            return True

    def draw_target(self):
        """Вывод мишени на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)


