from constants import *
from gamedata.scripting.action import Action

class DrawExplosions(Action):
    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, entities, script, callback):
        explosions = entities.get_entities(EXPLOSION_GROUP)

        for explosion in explosions:
            image = explosion.get_image()
            position = explosion.get_position()
            self._video_service.draw_image(image, position)