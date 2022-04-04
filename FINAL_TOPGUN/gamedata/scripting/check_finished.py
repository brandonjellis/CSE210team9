from constants import *
from gamedata.scripting.action import Action


class CheckFinished(Action):
    def __init__(self, scene):
        self._next_scene = scene

    def execute(self, entities, script, callback):
        player = entities.get_first_entity(PLAYER_GROUP)
        if player.get_life() <= 0:
            callback.next_state(self._next_scene)