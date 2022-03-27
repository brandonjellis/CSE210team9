"""
contains a list of constants to be used by the entire program
if a piece of data does not change, put it here!
"""
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
PLAYER_IMAGE = ""
PLAYER_WIDTH = 28
PLAYER_HEIGHT = 28
PLAYER_VELOCITY = 6

# BULLET
BULLET_VELOCITY = 6
BULLET_IMAGE = " "
BULLET_WIDTH = 1
BULLET_HEIGHT = 1

#SOUND

#IMAGES

#KEYBINDS

#ENTITY GROUPS
PLAYER = "player"
ENEMY = "enemy"
BULLET_PLAYER = "p_bullet"
BULLET_ENEMY = "e_bullet"
BACKGROUND = "background"


#SCRIPT GROUPS
INPUT = "input"
UPDATE = "update"
OUTPUT = "output"