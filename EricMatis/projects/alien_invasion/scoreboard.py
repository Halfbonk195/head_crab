import pygame.font
from pygame.sprite import Group

import constants as const
from ship import Ship


class Scoreboard:
    """Класс для вывода игровой информации"""

    def __init__(self, ai_game):
        """Инициализирует атрибуты подсчета очков."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.screen_settings
        self.stats = ai_game.stats

        # Настройки шрифта для вывода счета.
        self.text_color = const.COLOR_WHITE
        self.high_score_text_color = const.COLOR_LEMON_YELLOW
        self.numbers_font = pygame.font.SysFont(None, const.SB_NUMBERS_PT)
        self.label_font = pygame.font.SysFont(None, const.SB_TEXT_PT)

        # Подготовка изображений счетов.
        self.prep_score(self.text_color)
        self.prep_high_score()
        self.prep_level()
        self.prep_labels()
        self.prep_ships()

    def prep_score(self, text_color=const.COLOR_GRAY):
        """Преобразует текущий счет в графическое изображение."""
        rounded_score = round(self.stats.score, -1)
        score_str = f'{rounded_score:,}'.replace(',', ' ')
        self.score_image = self.numbers_font.render(score_str, True, text_color)

        # Вывод счета в правой верхней части экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Преобразует рекордный счет в графическое изображение."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f'{high_score:,}'.replace(',', ' ')
        self.high_score_image = self.numbers_font.render(high_score_str, True, self.high_score_text_color)

        # Рекорд выравнивается по центру верхней стороны.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx + 100
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Преобразует уровень в графическое изображение."""
        level_str = f'{self.stats.level}'
        self.level_image = self.numbers_font.render(level_str, True, self.text_color)

        # Уровень выводится под текущим счетом.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_labels(self):
        """Создание надписей на панале счета"""

        labels = {
            'high_score': 'High score',
            'score': 'Score',
            'level': 'Level'
        }

        self.label_images = {}
        self.label_rects = {}

        for label_name, label_text in labels.items():
            label_image = self.label_font.render(label_text, True, self.text_color)
            label_rect = label_image.get_rect()

            setattr(self, f"{label_name}_label_image", label_image)
            setattr(self, f"{label_name}_label_rect", label_rect)

            self.label_images[label_name] = label_image
            self.label_rects[label_name] = label_rect

        self.high_score_label_rect.centery = self.high_score_rect.centery
        self.high_score_label_rect.right = self.high_score_rect.left - 15

        self.score_label_rect.centery = self.score_rect.centery
        self.score_label_rect.right = self.score_rect.left - 15

        self.level_label_rect.centery = self.level_rect.centery
        self.level_label_rect.right = self.level_rect.left - 15

    def prep_ships(self):
        """Сообщает количество оставшихся кораблей."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Выводит текущий счет, рекорд и число оставшихся кораблей."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.high_score_label_image, self.high_score_label_rect)
        self.screen.blit(self.score_label_image, self.score_label_rect)
        self.screen.blit(self.level_label_image, self.level_label_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """Проверяет, появился ли новый рекорд."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            # Меняем цвет текущего счета в соответствии с цветом рекордного счета
            self.prep_score(self.high_score_text_color)
            self.prep_high_score()
            self.prep_labels()
        else:
            self.prep_score(self.text_color)

