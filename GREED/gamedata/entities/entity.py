#Handles basic logic associated with the specific objects involved with the game.
#Parent to: "falling_objects" and "player"

from gamedata.misc.datatypes import Color, Point

class Entity:
    def __init__(self):
        self._icon = ""
        self._size = 15
        self._color = Color()
        self._position = Point()
        self._velocity = Point()
    
    def get_color(self):
        return self._color

    def get_size(self):
        return self._size