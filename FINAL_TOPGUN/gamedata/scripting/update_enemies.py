from constants import *
from gamedata.scripting.action import Action


class UpdateEntities(Action):
    def __init__(self):
        pass

    def execute(self, entities, script, callback):
        enemies = entities.get_entities(ENEMY_GROUP)
        player_bullets = entities.get_entities(BULLET_PLAYER_GROUP)
        enemy_bullets = entities.get_entities(BULLET_ENEMY_GROUP)
        player = entities.get_first_entity(PLAYER_GROUP)
        for i in enemies:
            i.move_next()
            i.fire(entities)
        for i in player_bullets:
            i.move_next()
        for i in enemy_bullets:
            i.move_next()
        player.move_next()