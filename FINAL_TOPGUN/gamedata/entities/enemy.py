from time import time
from constants import *
from gamedata.datatypes.animation import Animation

from gamedata.entities.entity import Entity
from gamedata.datatypes.point import Point

class Enemy(Entity):
    """
    base enemy class template used for other enemy types
    """
    def __init__(self,pos,vel,size):
        super().__init__(pos,vel,size)
        self._life = 10
        self._lifetime = time()
        
    def _xmove(self,dt):
        pass

    def _ymove(self,dt):
        pass

    def move_next(self):
        now = time()
        dt = now - self._lifetime
        x = self._xmove(dt)
        y = self._ymove(dt)
        newpos = Point(x,y)
        self._position = newpos

    def fire(self,entlist):
        pass
    pass

class Type1(Enemy):
     
    def __init__(self,pos,vel):
        super().__init__(pos,vel,T1_SIZE)
        self._animation = Animation()
        self.fire_delay = 15

    def _xmove(self, dt):
        pass

    def _ymove(self, dt):
        pass

    def fire(self,entlist):
        pass

class Type2:
    pass


class Type3:
    pass


class TypeBoss:
    pass