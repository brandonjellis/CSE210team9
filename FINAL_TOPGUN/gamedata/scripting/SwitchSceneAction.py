
from gamedata.scripting.action import Action


class SwitchScreen(Action):
    
    def __init__(self, next, keyboard, auto = True):
        self._nextScene = next
        self._ks = keyboard
        self._auto = auto
    def execute(self, entities, script, callback):
        if self._auto:
            callback.next_state(self._nextScene)
        else:
            if self._ks.is_key_pressed("enter"):
                callback.next_state(self._nextScene)