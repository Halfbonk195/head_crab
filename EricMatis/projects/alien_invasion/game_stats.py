
class GameStats:
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.ships_left = None
        self.game_settings = ai_game.game_settings
        self.reset_stats()
        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False
        self.menu_state = 'main_menu'
        self.difficulty = 'Normal'

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.game_settings.ship_limit
        self.score = 0
