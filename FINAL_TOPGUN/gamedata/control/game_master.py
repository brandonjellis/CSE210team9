
from constants import *
from gamedata.scripting.GameMasterCallback import Callback
from gamedata.services.video_handler import VideoHandler
from gamedata.services.keyboard_handler import KeyboardHandler
from gamedata.services.physics_handler import PhysicsHandler
from gamedata.services.audio_handler import AudioHandler

from gamedata.control.entity_master import EntityMaster
from gamedata.control.reality_master import RealityMaster

from gamedata.scripting.script import Script

class GameMaster(Callback):
    """
    main control file handling top level game logic
    contains both a script master and a entity master

    in charge of controlling the flow of the game
    in charge of generating entities associated with each scene.
    """
    def __init__(self):
        self._vs = VideoHandler(WINDOW_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)
        self._ks = KeyboardHandler()
        self._ps = PhysicsHandler()
        self._as = AudioHandler()

        self._entlist = EntityMaster()
        self._builder = RealityMaster(self._vs, self._ks, self._ps, self._as, self._entlist)
        self._script = Script()

    def next_state(self, scene):
        self._builder.change_script(scene, self._script)

    def start(self):
        self._builder.change_script(INITIALIZE, self._script)
        self._execute_script(INITIALIZE)
        while self._vs.is_window_open():
            self._execute_script(INPUT)
            self._execute_script(UPDATE)
            self._execute_script(OUTPUT)

    def _execute_script(self,group):
        actions = self._script.get_actions(group)
        for action in actions:
            action.execute(self._entlist, self._script, self)
