import pygame
from constants import SHIP_IMAGE_PATH


class Ship:
    """Класс для управления кораблем."""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию"""
        self.screen = ai_game.screen
        self.game_settings = ai_game.game_settings
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник.
        self.image = self._load_image(SHIP_IMAGE_PATH)
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)
        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def _load_image(self, image_path):
        """Загружает изображение и возвращает поверхность."""
        image = pygame.image.load_extended(image_path)
        return image

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right:
            self.rect.move_ip(self.game_settings.ship_speed, 0)

        if self.moving_left:
            self.rect.move_ip(-self.game_settings.ship_speed, 0)

        # Ограничение движения корабля в пределах экрана.
        self.rect.clamp_ip(self.screen_rect)

        self.x = self.rect.x

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
