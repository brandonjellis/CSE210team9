import constants
from gamedata.control.action import Action
from gamedata.misc.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        cycle_1 = cast.get_first_actor("p1")
        p1_vel = cycle_1.get_velocity()

        # left
        if self._keyboard_service.is_key_down('a'):
            p1_vel = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            p1_vel = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            p1_vel = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            p1_vel = Point(0, constants.CELL_SIZE)
        
        cycle_1.turn_head(p1_vel)


        cycle_2 = cast.get_first_actor("p2")
        p2_vel = cycle_2.get_velocity() 

        # left
        if self._keyboard_service.is_key_down('j'):
            p2_vel = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            p2_vel = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            p2_vel = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            p2_vel = Point(0, constants.CELL_SIZE)
        
        cycle_2.turn_head(p2_vel)