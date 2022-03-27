
import constants
from gamedata.datatypes.point import Point
from gamedata.datatypes.animation import Animation

class Entity:
    """
    contains basic parameters for anything on the screen.
    """
    def __init__(self, position = Point(0,0), velocity = Point(0,0), size = Point(0,0)): 
        self._position = position
        self._velocity = velocity
        self._size = size
        self._animation = Animation()


    def get_position(self):
        return self._position

    def get_velocity(self):
        return self._velocity

    def get_size(self):
        return self._size

    def get_animation(self):
        return self._animation

    def get_image(self):
        return self._animation.get_image()

    def move_next(self):
        x = (self._position.get_x() + self._velocity.get_x()) % constants.MAX_X
        y = (self._position.get_x() + self._velocity.get_x()) % constants.MAX_Y 
        self._position = Point(x,y)

    def set_position(self, position):
        self._position = position

    def set_velocity(self, velocity):
        self._velocity = velocity  

    def set_size(self, size):
        self._size = size

    def set_animation(self, animation):
        self._animation = animation
        
    def get_hitbox(self):
        x = self._position.get_x()
        y = self._position.get_y()
        width = self._size.get_x()
        height = self._size.get_y()

        return (x,y,width,height)