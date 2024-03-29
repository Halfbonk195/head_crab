# Цвета
COLOR_LEMON_YELLOW = (238, 241, 34)
COLOR_DARK_TEAL = (11, 62, 62)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_LIME_GREEN = (50, 200, 100)

# Параметры экрана
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
BG_COLOR = COLOR_DARK_TEAL

# Параметры мишени
TARGET_COLOR = COLOR_GREEN
TARGET_WIDTH = 30
TARGET_HEIGHT = 150
TARGET_SPEED = 0.2

# Параметры снаряда
BULLET_SPEED = 1.7
BULLET_WIDTH = 15
BULLET_HEIGHT = 3
BULLET_COLOR = COLOR_LEMON_YELLOW
BULLETS_ALLOWED = 3  # Максимальное количество снарядов на экране

# Параметры корабля
SHIP_IMAGE_PATH = 'images/space_ship.png'
SHIP_SPEED = 1.5
SHOTS_LIMIT = 3  # Максимальное количество промахов за игру

# Параметры кнопки
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_COLOR = COLOR_LIME_GREEN
TEXT_COLOR = COLOR_WHITE
TEXT_PT = 60

# Параметры игры
SPEEDUP_SCALE = {
    'SHIP': 1.02,
    'BULLET': 1.06,
    'TARGET': 1.4,
}
