from constants import *
from gamedata.scripting.action import Action

class DrawPlayerBullets(Action):
    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, entities, script, callback):
        player_bullets = entities.get_entities(BULLET_PLAYER_GROUP)

        for bullet in player_bullets:
            image = bullet.get_image()
            position = bullet.get_position()
            #self._video_service.draw_image(image, position)
            if DEBUG:
                hitbox = bullet.get_hitbox()
                self._video_service.draw_rectangle(hitbox, BULLET_DEBUG, filled = True)