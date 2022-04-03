from constants import *
from gamedata.scripting.action import Action


class UpdateEnemies(Action):
    def __init__(self):
        pass

    def execute(self, entities, script, callback):
        enemies = entities.get_entities(ENEMY_GROUP)
        for i in enemies:
            i.move_next
            i.fire