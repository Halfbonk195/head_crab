import pygame
from constants import SHIP_IMAGE_PATH


class Ship:
    """Класс для управления кораблем."""

    def __init__(self, ts_game):
        """Инициализирует корабль и задает его начальную позицию"""
        self.screen = ts_game.screen
        self.game_settings = ts_game.game_settings
        self.screen_rect = ts_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник.
        self.image = self._load_image(SHIP_IMAGE_PATH)
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у левого края экрана.
        self.rect.midleft = self.screen_rect.midleft

        # Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # Флаг перемещения
        self.moving_up = False
        self.moving_down = False

    def _load_image(self, image_path):
        """Загружает изображение и возвращает поверхность."""
        image = pygame.image.load_extended(image_path)
        return image

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_up:
            self.rect.move_ip(0, -self.game_settings.ship_speed)

        if self.moving_down:
            self.rect.move_ip(0, self.game_settings.ship_speed)

        # Ограничение движения корабля в пределах экрана.
        self.rect.clamp_ip(self.screen_rect)
        self.y = self.rect.y

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль в центре левой стороны."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
