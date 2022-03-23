
from gamedata.entities.entity import Entity

class Bullet(Entity):
    def __init__(self, position=..., velocity=...):
        super().__init__(position, velocity)
        self._invincible = False
        self._damage = 10


