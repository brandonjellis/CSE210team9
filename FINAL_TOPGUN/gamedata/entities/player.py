
from gamedata.entities.entity import Entity
import time

class Player(Entity):
    def __init__(self, position=..., velocity=..., size=...):
        super().__init__(position, velocity, size)
        self._invincible = False
        self._invi_time = time.time()

    def toggle_invincible(self):
        self._invincible = not self._invincible



