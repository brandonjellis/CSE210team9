from constants import *
from gamedata.scripting.action import Action

class DrawEnemies(Action):
    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, entities, script, callback):
        enemies = entities.get_entities(ENEMY_GROUP)

        for enemy in enemies:
            image = enemy.get_image()
            position = enemy.get_position()
            self._video_service.draw_image(image, position)