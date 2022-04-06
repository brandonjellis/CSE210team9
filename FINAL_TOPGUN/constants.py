"""
contains a list of constants to be used by the entire program
if a piece of data does not change, put it here!
"""
from gamedata.datatypes.color import Color
from gamedata.datatypes.image import Image
from gamedata.datatypes.sound import Sound
import os
#----------------------------------------
#GAME CONSTANTS
#----------------------------------------

PATH = "C:\\Programming\\git\\CSE210team9\\"
DEBUG = True

# WINDOW
WINDOW_NAME = ""
FRAME_RATE = 60


# SCREEN
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
CENTER_X = SCREEN_WIDTH /2
CENTER_Y = SCREEN_HEIGHT /2
CONSTANT_FUNCTION = 100

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

#COLORS
BLACK = Color(0,0,0)
WHITE = Color(255,255,255)
BULLET_DEBUG = Color(255,0,0,100)
PLAYER_DEBUG = Color(255,0,255,100)
ENEMY_DEBUG = Color(0,0,255,100)

#TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# FONT
FONT_FILE = "FINAL_TOPGUN\\assets\\fonts\\zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48


# PLAYER
PLAYER_GROUP = "player"
PLAYER_IMAGE = Image("assets\\images\\player.png",0.20)
PLAYER_BULLET_IMAGE = Image("assets\\images\\player_bullet.png")
PLAYER_WIDTH = 28
PLAYER_HEIGHT = 28
PLAYER_VELOCITY = 6

# ENEMY
ENEMY_WIDTH = 28
ENEMY_HEIGHT = 28
ENEMY_VELOCITY = 6
ENEMY_IMAGE1 = Image("assets\\images\\enemy1.png")
ENEMY_IMAGE2 = Image("assets\\images\\enemy2.png")
ENEMY_IMAGE3 = Image("assets\\images\\enemy3.png",0.05)
ENEMY_IMAGE4 = Image("assets\\images\\enemy4.png")
ENEMY_IMAGE5 = Image("assets\\images\\enemy5.png")
ENEMY_IMAGE6 = Image("assets\\images\\enemy6.png")

# BULLET
BULLET_ENEMY_GROUP = "e_bullet"
BULLET_PLAYER_GROUP = "p_bullet"
BULLET_VELOCITY = 6
PLAYER_BULLET_VELOCITY = 12
BULLET_IMAGE1 = Image("assets\\images\\enemy_bullet1.png")
BULLET_IMAGE2 = Image("assets\\images\\enemy_bullet2.png")
BULLET_IMAGE3 = Image("assets\\images\\enemy_bullet3.png")
BULLET_IMAGE4 = Image("assets\\images\\enemy_bullet4.png")
BULLET_WIDTH = 10
BULLET_HEIGHT = 10

#SOUND
BACKGROUND1_SOUND = Sound("assets\\sounds\\background1.wav")
BACKGROUND2_SOUND = Sound("assets\\sounds\\background2.wav")
BACKGROUND3_SOUND = Sound("assets\\sounds\\background3.wav")
BONUS1_SOUND = Sound("assets\\sounds\\bonus1.wav")
BONUS2_SOUND = Sound("assets\\sounds\\bonus2.wav")
EXPLOSION_SOUND = Sound("assets\\sounds\\explosion.wav")
FINAL_SCORE_SOUND = Sound("assets\\sounds\\final_score.wav")
GAME_OVER_SOUND = Sound("assets\\sounds\\game_over.wav")
LASER_SHOT1_SOUND = Sound("assets\\sounds\\laser_shot_1.wav")
LASER_SHOT2_SOUND = Sound("assets\\sounds\\laser_shot_2.wav")
SPACESHOOTER_DEAD_SOUND = Sound("assets\\sounds\\space_shooter_dead.wav")

#EXPLOSION
EXPLOSION_IMAGES = {Image(f"assets\\images\\explosion{i:01}.png") for i in range(1,7)}
EXPLOSION_SIZE = 28
EXPLOSION_DELAY = 1
EXPLOSION_GROUP = "explosion"

#OTHER
DEFAULT_IMAGE = Image("assets\\images\\default.png")

#LEVELS
LEVEL1 = f"assets\\levels\\lv1.txt"

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
INITIALIZE = "init"

