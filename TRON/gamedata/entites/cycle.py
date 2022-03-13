import constants
from gamedata.entites.entity import Entity
from gamedata.misc.point import Point


class Cycle(Entity):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self,color,position,velocity,text = ""):
        super().__init__(color,position,velocity,text)
        self._segments = []

    def move_next(self):

        light_seg = Entity(color=self._color,position=self._position, text = "#")
        self._segments.append(light_seg)
        x = (self._position.get_x() + self._velocity.get_x()) % constants.MAX_X
        y = (self._position.get_y() + self._velocity.get_y()) % constants.MAX_Y
        self._position = Point(x, y)

    def get_trail(self):
        return self._segments

    def turn_head(self, velocity):
        self.set_velocity(velocity)
    