
from constants import *
from gamedata.scripting.action import Action
from gamedata.datatypes.point import Point

class DrawPlayer(Action):
    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, entities, script, callback):
        player = entities.get_first_entity(PLAYER_GROUP)

        image = player.get_image()
        position = player.get_position()
        x = position.get_x() #- PLAYER_OFFSET
        y = position.get_y() - PLAYER_OFFSET
        image_pos = Point(x,y)
        self._video_service.draw_image(image, image_pos)
        if DEBUG:
            hitbox = player.get_hitbox()
            self._video_service.draw_rectangle(hitbox, PLAYER_DEBUG, filled = True)

