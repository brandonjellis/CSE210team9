
from gamedata.entities.entity import Entity

class Bullet(Entity):
    def __init__(self, position=..., velocity=..., size=...):
        super().__init__(position, velocity, size)
        self._damage = 10


