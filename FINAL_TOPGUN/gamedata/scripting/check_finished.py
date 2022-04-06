from email.mime import audio
from constants import *
from gamedata.scripting.action import Action


class CheckFinished(Action):
    def __init__(self, scene, audio):
        self._next_scene = scene
        self._as = audio

    def execute(self, entities, script, callback):
        player = entities.get_first_entity(PLAYER_GROUP)
        if player.get_life() <= 0:
            self._as.play_sound(GAME_OVER_SOUND)
            callback.next_state(self._next_scene)
