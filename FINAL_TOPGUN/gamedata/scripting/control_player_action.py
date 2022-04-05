

from constants import *
from gamedata.scripting.action import Action
from gamedata.datatypes.point import Point

class ControlPlayer(Action):

    def __init__(self, keyboard):
        self._ks = keyboard

    def execute(self, entlist, script, callback):
        player = entlist.get_first_entity(PLAYER_GROUP)
        x = 0
        y = 0
        if self._ks.is_key_down(KEY_W):
            y = -PLAYER_VELOCITY
        if self._ks.is_key_down(KEY_S):
            y = PLAYER_VELOCITY
        
        if self._ks.is_key_down(KEY_A):
            x = -PLAYER_VELOCITY
        if self._ks.is_key_down(KEY_D):
            x = PLAYER_VELOCITY

        new_vel = Point(x,y)
        player.set_velocity(new_vel)

