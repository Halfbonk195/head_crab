import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """Класс капли дождя"""

    def __init__(self, ai_rain):
        super().__init__()
        self.screen = ai_rain.screen
        self.settings = ai_rain.settings
        self.image = pygame.image.load('images/raindrop.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 20, self.image.get_height() // 20))
        self.rect = self.image.get_rect()

        # Каждая капля появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = -5 * self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает каплю по вертикали."""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y
