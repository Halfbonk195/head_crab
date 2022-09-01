import sys
import pygame
from settings import Settings
from raindrop import Raindrop
from random import randint


class Rain:
    """Создает дождь на экране"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_width()
        self.settings.screen_height = self.screen.get_height()
        pygame.display.set_caption('Rain')

        self.raindrops = pygame.sprite.Group()
        self.raindrops_tmp = pygame.sprite.Group()
        self.number_raindrops_x, self.raindrop_width = self._params_raindrop()
        self._create_rain()

    def run_rain(self):
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_q, pygame.K_ESCAPE]:
                    self._quit()

    def _update_raindrops(self):
        self._check_raindrop_exist()
        self.raindrops.update()

    def _check_raindrop_exist(self):
        """Реагирует на достижение каплей конца экрана."""
        for raindrop in self.raindrops_tmp.sprites():
            if raindrop.rect.y == 0:
                self._create_rain()
                break
        for raindrop in self.raindrops.copy():
            if raindrop.rect.top >= self.screen.get_height():
                self.raindrops.remove(raindrop)

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.screen_color)
        self.raindrops.draw(self.screen)
        pygame.display.flip()

    def _create_rain(self):
        """Создает набор капель"""
        # Создание капли и вычисление количества капель в ряду
        # Интервал между соседними каплями равен 3 * ширину капли.

        self.raindrops_tmp = pygame.sprite.Group()
        for raindrop_number in range(self.number_raindrops_x):
            self._create_raindrops(raindrop_number, self.raindrop_width)
        for raindrop in self.raindrops_tmp.sprites():
            self.raindrops.add(raindrop)

    def _params_raindrop(self):
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.settings.screen_width - raindrop_width
        number_raindrops_x = available_space_x // (4 * raindrop_width)
        return number_raindrops_x, raindrop_width

    def _create_raindrops(self, raindrop_number, raindrop_width):
        """Создание капли и размещение ее в ряду"""
        raindrop = Raindrop(self)
        delta = randint(-60, 60)

        raindrop.x = raindrop_width + 4 * raindrop_number * raindrop_width + delta
        raindrop.y += delta
        raindrop.rect.x = raindrop.x
        raindrop.rect.y = raindrop.y
        self.raindrops_tmp.add(raindrop)

    def _quit(self):
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    rain = Rain()
    rain.run_rain()
