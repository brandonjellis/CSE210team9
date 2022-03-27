from gamedata.datatypes.point import Point
from gamedata.entities.bullet import Bullet
from gamedata.scripting.action import Action
from constants import *


class PlayerBullets(Action):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, entities, script, callback):
        player = entities.get_first_entity(PLAYER_GROUP)
        player_position = player.get_position()
        x = player_position.get_x() + PLAYER_WIDTH/2
        y = player_position.get_y()

        bullet_position = Point(x,y)
        bullet_size = Point(BULLET_WIDTH,BULLET_HEIGHT)
        bullet_velocity = Point(0, -BULLET_VELOCITY)

        new_bullet = Bullet()
        new_bullet.set_position(bullet_position)
        new_bullet.set_velocity(bullet_velocity)
        new_bullet.set_size(bullet_size)
        new_bullet.set_animation(images = BULLET_IMAGE)

        bullet = entities.add_entity(BULLET_PLAYER_GROUP, new_bullet)
        

        

    

