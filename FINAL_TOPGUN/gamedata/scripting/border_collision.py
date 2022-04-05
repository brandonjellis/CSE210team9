
from gamedata.datatypes.point import Point
from gamedata.scripting.action import Action
from constants import *


class BorderCollision(Action):
    def __init__(self, physics_service):
        self._physics_service = physics_service

    def execute(self, entities, script, callback):
        player = entities.get_first_entity(PLAYER_GROUP)
        position = player.get_position()
        current_vel = player.get_velocity()
        x = position.get_x()
        y = position.get_y()

        if x < FIELD_LEFT:
            velocity = Point(0,current_vel.get_y())
            player.set_velocity(velocity)

        elif x >= (FIELD_RIGHT - PLAYER_WIDTH):
            velocity = Point(0,current_vel.get_y())
            player.set_velocity(velocity)

        if y < FIELD_TOP:
            velocity = Point(current_vel.get_x(),0)
            player.set_velocity(velocity)

        elif y >= (FIELD_BOTTOM - PLAYER_WIDTH):
            velocity = Point(current_vel.get_x(),0)
            player.set_velocity(velocity)


        

        

