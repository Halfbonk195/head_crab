import sys

import pygame

from settings_sky import Settings


class BlueSky:
    """Отрисовывает окно pygame с синим фоном"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Blue sky')

    def run_sky(self):
        while True:
            self._check_events()
            self._update_screen()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == '__main__':
    bs = BlueSky()
    bs.run_sky()
