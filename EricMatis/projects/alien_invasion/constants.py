import os

# Цвета
COLOR_LEMON_YELLOW = (238, 241, 34)
COLOR_DARK_TEAL = (11, 62, 62)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_LIME_GREEN = (50, 200, 100)
COLOR_GRAY = (128, 128, 128)
COLOR_DARK_GRAY = (41, 49, 51)
COLOR_BLACK_GRAY = (20, 20, 20)

# Параметры снаряда
BULLET_SPEED = 2
BULLET_WIDTH = 4
BULLET_HEIGHT = 20
BULLET_COLOR = COLOR_LEMON_YELLOW
BULLETS_ALLOWED = 3  # Максимальное количество снарядов на экране

# Параметры пришельцев
ALIEN_IMAGE_PATH = os.path.join(os.path.dirname(__file__), 'images', 'alien_ship.png')
ALIEN_SPEED = 1.0
DROP_SPEED = 15
ALIEN_POINTS = 50

# Параметры корабля
SHIP_IMAGE_PATH = os.path.join(os.path.dirname(__file__), 'images', 'space_ship.png')
SHIP_SPEED = 2.5
SHIP_LIMIT = 3  # Максимальное количество кораблей за игру

# Параметры экрана
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
BG_COLOR = COLOR_DARK_TEAL

# Параметры кнопки
BUTTON_WIDTH = 240
BUTTON_HEIGHT = 60
BUTTON_COLOR = COLOR_LIME_GREEN
TEXT_COLOR = COLOR_WHITE
BUTTON_TEXT_PT = 60

# Параметры игры
SPEEDUP_SCALE = {
    'alien': {
        'Easy': 1.05,
        'Normal': 1.1,
        'Hard': 1.3,
        'Impossible': 1.6,
    },
    'ship': {
        'Easy': 1.02,
        'Normal': 1.05,
        'Hard': 1.08,
        'Impossible': 1.1,
    },
    'bullet': {
        'Easy': 1.05,
        'Normal': 1.1,
        'Hard': 1.2,
        'Impossible': 1.3,
    }
}

# Параметры таблицы счета
SB_TEXT_PT = 70
SCORE_SCALE = 1.5
