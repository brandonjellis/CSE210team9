from constants import *
from gamedata.scripting.action import Action

class BulletOffscreen(Action):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, entities, script, callback):
        bullets = entities.get_entities(BULLET_PLAYER_GROUP)
        for bullet in bullets:
            position = bullet.get_position()
            if position.get_y() < 0:
                entities.remove_entity(BULLET_PLAYER_GROUP, bullet)
        
        bullets = entities.get_entities(BULLET_ENEMY_GROUP)
        for bullet in bullets:
            x_position = bullet.get_position().get_x()
            y_position = bullet.get_position().get_y()
            if (x_position > SCREEN_WIDTH or x_position < 0):
                entities.remove_entity(BULLET_ENEMY_GROUP, bullet)
            if (y_position > SCREEN_HEIGHT or y_position < 0):
                entities.remove_entity(BULLET_ENEMY_GROUP, bullet)


