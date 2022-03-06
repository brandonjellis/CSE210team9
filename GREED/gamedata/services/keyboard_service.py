#Handles keyboard input from the user.
import pyray 
from gamedata.misc.datatypes import Point


class Keyboard_Service:
    def __init__(self, cell_size = 1):
        self._cell_size = cell_size
    
    

    def get_position(self):
        dx = 0
        dy = 0
        s = 8
    
        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -s

        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = s

        if pyray.is_key_down(pyray.KEY_UP):
            dy = -s

        if pyray.is_key_down(pyray.KEY_DOWN):
            dy = s

        position = Point(dx, dy)

        return position
        
    

    