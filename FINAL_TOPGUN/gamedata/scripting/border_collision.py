
from argparse import Action


class BorderCollision(Action):
    def __init__(self, physics_service):
        self._physics_service = physics_service

    
        

