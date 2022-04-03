"""
contains a list of constants to be used by the entire program
if a piece of data does not change, put it here!
"""
from raylib import KEY_S
from gamedata.datatypes.color import Color
#----------------------------------------
#GAME CONSTANTS
#----------------------------------------

# WINDOW
WINDOW_NAME = ""
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900
CENTER_X = SCREEN_WIDTH /2
CENTER_Y = SCREEN_HEIGHT /2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

#COLORS
BLACK = Color(0,0,0)
WHITE = Color(255,255,255)

# PLAYER
PLAYER_GROUP = "player"
PLAYER_IMAGES = None
PLAYER_WIDTH = 28
PLAYER_HEIGHT = 28
PLAYER_VELOCITY = 6

# ENEMY
ENEMY_GROUP = "enemy"
T1_IMAGES = None
T2_IMAGES = None
T3_IMAGES = None
T1_SIZE = 10
T2_SIZE = 10
T3_SIZE = 10
BOSS_SIZE = 40

# BULLET
BULLET_ENEMY_GROUP = "e_bullet"
BULLET_PLAYER_GROUP = "p_bullet"
BULLET_VELOCITY = 6
BULLET_IMAGE = " "
BULLET_WIDTH = 1
BULLET_HEIGHT = 1

#SOUND

#IMAGES

#KEYBINDS
LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
SPACE = "space"
KEY_W = "w"
KEY_A = "a"
KEY_S = "s"
KEY_D = "d"


#ENTITY GROUPS
PLAYER = "player"
ENEMY_GROUP = "enemy"
BACKGROUND_GROUP = "background"


#SCRIPT GROUPS
INPUT = "input"
UPDATE = "update"
OUTPUT = "output"