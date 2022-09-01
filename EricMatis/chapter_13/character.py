import pygame


class Character:
    """Класс персонажа"""
    def __init__(self, bs):
        self.screen = bs.screen
        self.screen_rect = bs.screen.get_rect()

        self.image = pygame.image.load('images/Gordon_Freeman_modified.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Отрисовывает персонажа в текущей позиции"""
        self.screen.blit(self.image, self.rect)
