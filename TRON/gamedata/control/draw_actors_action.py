from gamedata.entites.cycle import Cycle
from gamedata.control.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service, game = False):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
        self._game = game

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._video_service.clear_buffer()

        if self._game:
            cycle_1 = [cast.get_first_actor("p1")]
            cycle_2 = [cast.get_first_actor("p2")]
            if cycle_1[0] != None:
                cycle_1.extend(cycle_1[0].get_trail())
                self._video_service.draw_actors(cycle_1)
            if cycle_2[0] != None:
                cycle_2.extend(cycle_2[0].get_trail())
                self._video_service.draw_actors(cycle_2)

        
        scores = cast.get_actors("scores")
        messages = cast.get_actors("banners")
        self._video_service.draw_actors(scores)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()