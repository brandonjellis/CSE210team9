#Child class of "entity" containing aditional functionality for the player character such as movement restrictions and collisions.

from entity import Entity

class Player(Entity):
    def __init__(self):
        super.__init__()
        