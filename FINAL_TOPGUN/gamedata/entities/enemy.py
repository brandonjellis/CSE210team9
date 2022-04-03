from time import time
from constants import *
import math

from gamedata.entities.entity import Entity
from gamedata.datatypes.point import Point

class Enemy(Entity):
    """
    base enemy class template used for other enemy types
    """
    def __init__(self,pos,vel,size):
        super.__init__(pos,vel,size)
        self._life = 10
        self._lifetime = time()
        self._fire_delay = 10
        
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
    def __init__(self, pos, vel, size):
        super().__init__(pos, vel, size)

    def _xmove(self, dt):
        return round(CONSTANT_FUNCTION*math.log10(dt))

    def _ymove(self, dt):
        return self._position.get_y()

class Type2(Enemy):
    def __init__(self, pos, vel, size):
        super().__init__(pos, vel, size)

    def _xmove(self, dt):
        return round(CONSTANT_FUNCTION*math.cos(dt))

    def _ymove(self, dt):
        return round(CONSTANT_FUNCTION*math.sin(dt) + 100)

class Type3(Enemy):
    def __init__(self, pos, vel, size):
        super().__init__(pos, vel, size)

    def _xmove(self, dt):
        return round(CONSTANT_FUNCTION*math.sin(2*dt))

    def _ymove(self, dt):
        return round(CONSTANT_FUNCTION*math.sin(dt) + 100)

class TypeBoss(Enemy):
    def __init__(self, pos, vel, size):
        super().__init__(pos, vel, size)

    def _xmove(self, dt):
        return round((CONSTANT_FUNCTION*4)*math.sin(0.01*dt))

    def _ymove(self, dt):
        return round((CONSTANT_FUNCTION/2)*math.log10(dt+1))