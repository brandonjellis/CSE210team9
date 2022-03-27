
from gamedata.datatypes.point import Point
from gamedata.scripting.action import Action
from FINAL_TOPGUN.constants import *


class BorderCollision(Action):
    def __init__(self, physics_service):
        self._physics_service = physics_service

    def execute(self, entities, script, callback):
        player = entities.get_first_entity("player")
        position = player.get_position()
        x = position.get_x()
        y = position.get_y()

        if x < FIELD_LEFT:
            player.stop_x()
            velocity = Point(0,0)
            player.set_velocity(velocity)

        elif x >= (FIELD_RIGHT - PLAYER_WIDTH):
            player.stop_x()
            velocity = Point(0,0)
            player.set_velocity(velocity)

        if y < FIELD_TOP:
            player.stop_y()
            velocity = Point(0,0)
            player.set_velocity(velocity)

        elif y >= (FIELD_BOTTOM - PLAYER_WIDTH):
            player.stop_y()
            velocity = Point(0,0)
            player.set_velocity(velocity)


        

        

