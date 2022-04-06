from constants import *
from gamedata.scripting.action import Action


class UpdateExplosions(Action):
    def __init__(self):
        pass

    def execute(self, entities, script, callback):
        explosions = entities.get_entities(EXPLOSION_GROUP)
        for i in entities.get_entities(EXPLOSION_GROUP):
            if i.get_finished():
                entities.remove_entity(EXPLOSION_GROUP,i)
            else:
                i.update()