import sys

import pygame

from settings_sky import Settings
from character import Character
from stars import Star

class BlueSkyWithStars:
    """Отрисовывает окно pygame с синим фоном"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Blue sky')
        self.character = Character(self)
        self.stars = pygame.sprite.Group()

        self._create_stars()

    def run_sky(self):
        while True:
            self._check_events()
            self._update_screen()

    def _create_stars(self):
        """Создание набора звезд"""
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        character_height = self.character.rect.height
        available_space_y = (self.settings.screen_height - (2 * star_height) - character_height)
        number_rows = available_space_y // star_height

        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Создание Звезды и размещение ее в ряду."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star_height + 2 * star_height * row_number
        self.stars.add(star)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.character.blitme()
        self.stars.draw(self.screen)
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == '__main__':
    bs = BlueSkyWithStars()
    bs.run_sky()
