import sys
import pygame
from settings import Settings


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

    def _create_rain(self):
        pass

    def _update_raindrops(self):
        pass

    def _update_screen(self):
        pass

    def _quit(self):
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    rain = Rain()
    rain.run_rain()
