from constants import *
from gamedata.entities.entity import Entity
from gamedata.datatypes.point import Point
from gamedata.datatypes.animation import Animation
from time import time


class Explosion(Entity):
    def __init__(self,pos):
        size = Point(EXPLOSION_SIZE,EXPLOSION_SIZE)
        super().__init__(pos,size=size)
        self._animation = Animation(EXPLOSION_IMAGES, EXPLOSION_DELAY, True)
        self._created = time()

    def update(self):
        self._animation.next()
        current = time()
        if ((current - self._created) > self._lifespan):
            self.finished = True

    def get_finished(self):
        if ((len(EXPLOSION_IMAGES) -1) >= self._animation.get_index()):
            return True
        else:
            return False
