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
SCREEN_WIDTH = 900
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

# PLAYER
PLAYER_GROUP = "player"
PLAYER_IMAGE = "assets/images/player.png"
PLAYER_BULLET_IMAGE = "assets/images/player_bullet.png"
PLAYER_WIDTH = 28
PLAYER_HEIGHT = 28
PLAYER_VELOCITY = 6

# ENEMY
ENEMY_WIDTH = 28
ENEMY_HEIGHT = 28
ENEMY_VELOCITY = 6
ENEMY_IMAGE1 = "assets/images/enemy1.png"
ENEMY_IMAGE2 = "assets/images/enemy2.png"
ENEMY_IMAGE3 = "assets/images/enemy3.png"
ENEMY_IMAGE4 = "assets/images/enemy4.png"
ENEMY_IMAGE5 = "assets/images/enemy5.png"
ENEMY_IMAGE6 = "assets/images/enemy6.png"

# BULLET
BULLET_ENEMY_GROUP = "e_bullet"
BULLET_PLAYER_GROUP = "p_bullet"
BULLET_VELOCITY = 6
BULLET_IMAGE1 = "assets/images/enemy_bullet1.png"
BULLET_IMAGE2 = "assets/images/enemy_bullet2.png"
BULLET_IMAGE3 = "assets/images/enemy_bullet3.png"
BULLET_IMAGE4 = "assets/images/enemy_bullet4.png"
BULLET_WIDTH = 1
BULLET_HEIGHT = 1

#SOUND
BACKGROUND1_SOUND = "assets/sounds/background1.wav"
BACKGROUND2_SOUND = "assets/sounds/background2.wav"
BACKGROUND3_SOUND = "assets/sounds/background3.wav"
BONUS1_SOUND = "assets/sounds/bonus1.wav"
BONUS2_SOUND = "assets/sounds/bonus2.wav"
EXPLOSION_SOUND = "assets/sounds/explosion.wav"
FINAL_SCORE_SOUND = "assets/sounds/final_score.wav"
GAME_OVER_SOUND = "assets/sounds/game_over.wav"
LASER_SHOT1_SOUND = "assets/sounds/laser_shot_1.wav"
LASER_SHOT2_SOUND = "assets/sounds/laser_shot_2.wav"
SPACESHOOTER_DEAD_SOUND = "assets/sounds/space_shooter_dead.wav"

#EXPLOSION
EXPLOSION_IMAGES = {f"assets/images/explosion{i:01}.png" for i in range(1,7)}
EXPLOSION_SIZE = 28
EXPLOSION_DELAY = 0.5
EXPLOSION_GROUP = "explosion"


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