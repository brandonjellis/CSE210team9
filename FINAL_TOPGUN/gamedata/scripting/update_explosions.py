from constants import *
from gamedata.scripting.action import Action


class UpdateExplosions(Action):
    def __init__(self):
        pass

    def execute(self, entities, script, callback):
        explosions = entities.get_entities(EXPLOSION_GROUP)
        for i in explosions:
            if i.get_finished():
                entities.remove_entitiy(EXPLOSION_GROUP,i)
            else:
                i.update()