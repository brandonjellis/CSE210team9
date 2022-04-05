import imp
from constants import *
from gamedata.scripting.action import Action

class DrawPlayer(Action):
    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, entities, script, callback):
        player = entities.get_first_entity(PLAYER_GROUP)

        image = player.get_image()
        position = player.get_position()
        self._video_service.draw_image(image, position)

