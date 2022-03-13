from gamedata.control.action import Action
from gamedata.services.keyboard_service import KeyboardService

class HandleMenu(Action):
    
    def __init__(self,keyboard):
        self._ks = keyboard

    def execute(self, cast, script):
        if self._ks.is_key_pressed("space"):
            cast.remove_actors("banners")
            return True