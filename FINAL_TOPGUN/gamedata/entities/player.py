from gamedata.entities.entity import Entity


class Player(Entity):
    def __init__(self, position=..., velocity=..., size=...):
        super().__init__(position, velocity, size)
        self._invincible = False

    def toggle_invincible(self):
        self._invincible = not self._invincible



