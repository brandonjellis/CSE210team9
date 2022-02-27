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
        self._max_x = 0
        self._min_x = 0
        self._max_y = 0
        self._min_y = 0

    
    def get_icon(self):
        return self._icon

    def get_size(self):
        return self._size

    def get_color(self):
        return self._color

    def get_positon(self):
        return self._position

    def get_velocity(self):
        return self._velocity

    def set_icon(self, icon):
        self._icon = icon

    def set_size(self, size):
        self._size = size 
    
    def set_color(self, color):
        self._color = color

    def set_position(self, pos):
        self._position = pos 

    def set_velocity(self, v):
        self._velocity = v

    def set_max(self, x, y):
        self._max_x = x
        self._max_y = y

    def set_min(self, x, y):
        self._min_x = x
        self._min_y = y

    def update_pos(self):
        new_pos = self._position.point_2d()
        new_pos[0] += self._velocity.point_2d()[0]
        new_pos[1] += self._velocity.point_2d()[1]
        
        if (new_pos[0] > self._max_x):
            new_pos[0] = self._max_x
        elif (new_pos[0] < self._min_x):
            new_pos[0] = self._min_x
        
        if (new_pos[1] > self._max_y):
            new_pos[1] = self._max_y
        elif (new_pos[1] < self._min_y):
            new_pos[1] = self._min_y
        
        



