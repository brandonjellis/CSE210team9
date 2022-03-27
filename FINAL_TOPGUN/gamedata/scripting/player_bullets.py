import imp
from gamedata.datatypes.point import Point
from gamedata.entities.bullet import Bullet
from gamedata.scripting.action import Action
from constants import *


class PlayerBullets(Action):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, entities, script, callback):
        player = entities.get_first_entity("player")
        player_position = player.get_position()
        x = player_position.get_x() + PLAYER_WIDTH/2
        y = player_position.get_y()
        bullet_position = Point(x,y)
        bullet_size = Point(BULLET_WIDTH,BULLET_HEIGHT)

        bullet = entities.get_first_entity("bullet")
        bullet.set_position(bullet_position)
        bullet.set_velocity(BULLET_VELOCITY)
        bullet.set_size(bullet_size)
        bullet.set_animation(BULLET_IMAGE)


        

    

