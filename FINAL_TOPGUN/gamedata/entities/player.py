
from gamedata.entities.entity import Entity
from time import time

class Player(Entity):
    def __init__(self, position=..., velocity=..., size=...):
        super().__init__(position, velocity, size)
        self._invincible = False
        self._invi_time = time()
        self._lives = 3

    def toggle_invincible(self):
        self._invincible = not self._invincible

    def get_invincible(self):
        return self._invincible

    def got_hit(self):
        self._lives -= 1
        self._invincible = True
        self._invi_time = time()
