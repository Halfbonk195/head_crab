import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """Класс капли дождя"""

    def __init__(self, ai_rain):
        super().__init__()
