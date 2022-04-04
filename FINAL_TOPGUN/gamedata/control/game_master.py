
from gamedata.scripting.GameMasterCallback import Callback
from gamedata.services.video_handler import VideoHandler
from gamedata.services.keyboard_handler import KeyboardHandler
from gamedata.services.physics_handler import PhysicsHandler
from gamedata.services.audio_handler import AudioHandler

from gamedata.control.entity_master import EntityMaster
from gamedata.control.reality_master import RealityMaster

class GameMaster(Callback):
    """
    main control file handling top level game logic
    contains both a script master and a entity master

    in charge of controlling the flow of the game
    in charge of generating entities associated with each scene.
    """
    def __init__(self):
        self._vs = VideoHandler()
        self._ks = KeyboardHandler()
        self._ps = PhysicsHandler()
        self._as = AudioHandler()

        self._entlist = EntityMaster()
        self._builder = RealityMaster()

    def next_state(self):
        self._builder.change_script()

    def start(self):
        pass

    def _execute_script(self):
        pass
