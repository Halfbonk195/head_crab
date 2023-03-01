class GameStats:
    """Отслеживание статистики для игры Target Shooting"""

    def __init__(self, ts_game):
        """Инициализирует статистику"""
        self.shots_left = None
        self.game_settings = ts_game.game_settings
        self.reset_stats()
        # Игра Target Shooting запускается в неактивном состоянии.
        self.game_active = False

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.shots_left= self.game_settings.shots_limit
