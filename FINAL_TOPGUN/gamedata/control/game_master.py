
from gamedata.scripting.GameMasterCallback import Callback
from gamedata.services.video_handler import VideoHandler
from gamedata.services.keyboard_handler import KeyboardHandler
from gamedata.services.physics_handler import PhysicsHandler
from gamedata.services.audio_handler import AudioHandler

class GameMaster(Callback):
    """
    main control file handling top level game logic
    contains both a script master and a entity master

    in charge of controlling the flow of the game
    in charge of generating entities associated with each scene.
    """
    def __init__(self):
        pass
