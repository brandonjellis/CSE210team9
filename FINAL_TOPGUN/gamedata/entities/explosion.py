from constants import *
from gamedata.entities.entity import Entity
from gamedata.datatypes.point import Point
from gamedata.datatypes.animation import Animation
from time import time


class Explosion(Entity):
    def __init__(self,pos):
        size = Point(EXPLOSION_SIZE,EXPLOSION_SIZE)
        super().__init__(pos,size=size)
        self._animation = Animation(EXPLOSION_DELAY, True, EXPLOSION_IMAGES)
        self._lifespan = EXPLOSION_DELAY * 6
        self._created = time()
        self._finished = False

    def update(self):
        self._animation.next()
        current = time()
        if ((current - self._created) > self._lifespan):
            self.finished = True

    def get_finished(self):
        return self._finished
