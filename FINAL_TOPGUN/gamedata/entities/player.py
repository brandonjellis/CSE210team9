from gamedata.entities.entity import Entity


class Player(Entity):
    def __init__(self, position=..., velocity=...):
        super().__init__(position, velocity)
        self._invincible = False

    def toggle_invincible(self):
        self._invincible = not self._invincible



    

    