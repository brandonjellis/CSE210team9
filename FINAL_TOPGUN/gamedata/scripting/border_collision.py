
from gamedata.datatypes.point import Point
from gamedata.scripting.action import Action
from constants import *


class BorderCollision(Action):
    def __init__(self, physics_service):
        self._physics_service = physics_service

    def execute(self, entities, script, callback):
        player = entities.get_first_entity(PLAYER_GROUP)
        position = player.get_position()
        x = position.get_x()
        y = position.get_y()

        if x < FIELD_LEFT:
            pos = Point(0,y)
            player.set_position(pos)

        if x > (FIELD_RIGHT - PLAYER_WIDTH):
            pos = Point(FIELD_RIGHT-PLAYER_WIDTH, y)
            player.set_position(pos)

        if y < FIELD_TOP:
            pos = Point(x,0+PLAYER_WIDTH)
            player.set_position(pos)

        if y > (FIELD_BOTTOM - PLAYER_WIDTH):
            pos = Point(x, FIELD_BOTTOM - PLAYER_WIDTH)
            player.set_position(pos)


        

        

