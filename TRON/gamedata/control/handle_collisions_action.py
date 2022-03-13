import constants
from gamedata.entites.entity import Entity
from gamedata.control.action import Action
from gamedata.misc.point import Point
from gamedata.entites.banner import Banner

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._winner = ""

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._is_game_over = False
        self._winner = ""

        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_score_collision(cast)
            self._handle_game_over(cast)
        return self._is_game_over

    def _handle_score_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score_1 = cast.get_actors("scores")[0]
        score_2 = cast.get_actors("scores")[1]
        points = 1


        if self._winner == "p1":
            score_1.add_points(points)
        
        elif self._winner == "p2":
            score_2.add_points(points)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments or other snake's segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle_1_head = cast.get_first_actor("p1")
        segments_1 = cycle_1_head.get_trail()

        cycle_2_head = cast.get_first_actor("p2")
        segments_2 = cycle_2_head.get_trail()
        
        for segment in segments_1:
            if cycle_1_head.get_position() == segment.get_position():
                self._is_game_over = True
                self._winner = "p2"

            elif cycle_2_head.get_position() == segment.get_position():
                self._is_game_over = True
                self._winner = "p1"

        for segment in segments_2:
            if cycle_2_head.get_position() == segment.get_position():
                self._is_game_over = True
                self._winner = "p1"

            elif cycle_1_head.get_position() == segment.get_position():
                self._is_game_over = True
                self._winner = "p2"
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the loser snake white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycle_1 = cast.get_first_actor("p1")
            segments_1 = cycle_1.get_trail()
            
            cycle_2 = cast.get_first_actor("p2")
            segments_2 = cycle_2.get_trail()

            if self._winner == "p1":
                for segment in segments_2:
                    segment.set_color(constants.WHITE)

                winner = "Player 1"

            if self._winner == "p2":
                for segment in segments_1:
                    segment.set_color(constants.WHITE)

                winner = "Player 2"

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message_1 = "Game Over\n" + winner + "Wins!\n" + "Press SPACE to play again! "
            message = Entity()
            message.set_text(message_1)
            message.set_position(position)
            cast.add_actor("banners", message)
            