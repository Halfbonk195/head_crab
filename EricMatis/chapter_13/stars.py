import pygame
from pygame.sprite import Sprite
from random import choice

class Star(Sprite):
    """Класс, представляющий одну звезду"""

    def __init__(self, ai_game):
        """Инициализирует звезду и задает его начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen

        # Загрузка изображения пришельца и назначение атрибута rect.
        list_images = ['images/star.png', 'images/star_2.png']
        self.image = pygame.image.load(choice(list_images))
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизонтальной позиции пришельца.
        self.x = float(self.rect.x)