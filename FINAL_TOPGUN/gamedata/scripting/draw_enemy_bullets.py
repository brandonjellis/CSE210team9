from constants import *
from gamedata.scripting.action import Action

class DrawEnemyBullets(Action):
    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, entities, script, callback):
        enemy_bullets = entities.get_entities(BULLET_ENEMY_GROUP)

        for bullet in enemy_bullets:
            image = bullet.get_image()
            position = bullet.get_position()
            self._video_service.draw_image(image, position)