import csv
from constants import *
from gamedata.datatypes.animation import Animation
from gamedata.datatypes.point import Point


from gamedata.entities.player import Player
from gamedata.entities.bullet import Bullet
from gamedata.entities.enemy import Enemy

from gamedata.scripting.GameMasterCallback import Callback
from gamedata.scripting.border_collision import BorderCollision
#from gamedata.scripting.control_player_action import 
from gamedata.scripting.initialize_handlers import InitializeDevicesAction
from gamedata.scripting.control_player_action import ControlPlayer

class RealityMaster:
    """
    generates the loop script for each state of the game and creates initial entities, returns script to be run to game master. 
    """
    def __init__(self,video,keyboard,physics,audio):
        self._vs = video
        self._ks = keyboard
        self._ps = physics
        self._as = audio

    def change_script(self,gamestate,entlist,script):
        if gamestate == "level1":
            self._build_lv1(entlist,script)
        elif gamestate == "level2":
            self._build_lv2(entlist, script)
        elif gamestate == "level3":
            self._build_lv3(entlist, script)
        elif gamestate == "init":
            self._build_init(entlist, script)

    #SCENE BUILDER METHODS

    def _build_init(self,entlist,script):
        pass

    def _build_lv1(self,entlist,script):
        pass
        #entities
        self._create_player(entlist)
        #script
        self._input_script(script)



    def _build_lv2():
        pass
    def _build_lv3():
        pass
    def _build_menu():
        pass

    #ENTITY METHODS
    def _create_player(self, entlist):
        entlist.remove_entities(PLAYER)
        x = CENTER_X - PLAYER_WIDTH/2
        y = CENTER_Y - PLAYER_HEIGHT/2
        start_pos = Point(x,y)
        start_vel = Point(0,0)
        ent_size = Point(PLAYER_WIDTH,PLAYER_HEIGHT)
        player = Player(start_pos,start_vel,ent_size)
        player_animation = Animation(images = PLAYER_IMAGES)
        player.set_animation(player_animation)

    #SCRIPT METHODS
    def _input_script(self, script):
        script.clear_actions(INPUT)
        script.add_action(INPUT, ControlPlayer(self._ks))
        script.add_action()

    def _update_script(self, script):
        pass
    
    def _output_script(self, script):
        pass

    def _initialize_script(self, script):
        pass

    #LEVEL DATA METHODS