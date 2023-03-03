import pygame.font
from constants import BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_COLOR, TEXT_COLOR, BUTTON_TEXT_PT


class Button:

    def __init__(self, ai_game, msg, position=None, color=BUTTON_COLOR):
        """Инициализирует атрибуты кнопки."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Назначение размеров и свойств кнопок.
        self.width, self.height = BUTTON_WIDTH, BUTTON_HEIGHT
        self.button_color = color
        self.text_color = TEXT_COLOR
        self.font = pygame.font.SysFont(None, BUTTON_TEXT_PT)

        # Построение объекта rect кнопки и выравнивание по центру экрана.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        if position:
            self.rect.center = position
        else:
            self.rect.center = self.screen_rect.center

        # Сообщение кнопки создается только один раз.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Отображение пустой кнопки и вывод сообщения.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

