import json
import os

from constants import SAVE_PATH


class LoadSave:
    """Класс для записи в файл и чтения из файла рекорда игры."""

    def __init__(self, ai_game):
        """Инициализирует настройки записи и чтения, необходимо отправить экземпляр GameStats"""
        self.file_name = SAVE_PATH
        self.save_path = 'ai_saves'
        self.game_stats = ai_game.stats

    def read_high_score(self):
        """Читает из файла лучший счет"""

        try:
            with open(self.file_name, 'r') as file:
                self.game_stats.high_score = json.load(file)
        except FileNotFoundError:
            self.game_stats.high_score = 0

    def save_high_score(self):
        """Сохраняет в файл лучший счет"""
        # Проверям существует ли директория с сохранениями
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

        with open(self.file_name, 'w') as file:
            json.dump(self.game_stats.high_score, file)
