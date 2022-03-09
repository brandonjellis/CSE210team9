from gamedata.entites.cycle import Cycle
from gamedata.control.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score_1 = cast.get_actors("scores")[0]
        score_2 = cast.get_actors("scores")[1]
        cycle_1 = cast.get_first_actor("p1")
        cycle_2 = cast.get_first_actor("p2")
        segments_1 = cycle_1.get_segments()
        segments_2 = cycle_2.get_segments()

        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actors(segments_1)
        self._video_service.draw_actors(segments_2)
        self._video_service.draw_actor(cycle_1)
        self._video_service.draw_actor(cycle_2)
        self._video_service.draw_actor(score_1)
        self._video_service.draw_actor(score_2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()