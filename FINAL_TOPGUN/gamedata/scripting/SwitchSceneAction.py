
from gamedata.scripting.action import Action


class SwitchScreen(Action):
    
    def __init__(self, next):
        self._nextScene = next
    def execute(self, entities, script, callback):
        callback.next_scene()