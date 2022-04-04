import csv
from constants import *
from gamedata.datatypes.animation import Animation
from gamedata.datatypes.point import Point


from gamedata.entities.player import Player
from gamedata.entities.bullet import Bullet
from gamedata.entities.enemy import Enemy

from gamedata.scripting.border_collision import BorderCollision
from gamedata.scripting.bullet_offscreen import BulletOffscreen
from gamedata.scripting.control_player_action import ControlPlayer
from gamedata.scripting.draw_enemies import DrawEnemies
from gamedata.scripting.draw_enemy_bullets import DrawEnemyBullets
from gamedata.scripting.draw_player import DrawPlayer
from gamedata.scripting.draw_player_bullets import DrawPlayerBullets
from gamedata.scripting.draw_explosionS import DrawExplosions
from gamedata.scripting.end_drawing_action import EndDrawingAction
from gamedata.scripting.enemy_collisions import EnemyCollisions
from gamedata.scripting.GameMasterCallback import Callback
from gamedata.scripting.initialize_handlers import InitializeDevicesAction
from gamedata.scripting.load_assets_action import LoadAssetsAction
from gamedata.scripting.player_bullets import PlayerBullets
from gamedata.scripting.player_collisions import PlayerCollisions
from gamedata.scripting.release_devices_action import ReleaseDevicesAction
from gamedata.scripting.spawn_enemy import SpawnEnemy
from gamedata.scripting.start_drawing_action import StartDrawingAction
from gamedata.scripting.SwitchSceneAction import SwitchScreen
from gamedata.scripting.update_enemies import UpdateEnemies
from gamedata.scripting.update_explosions import UpdateExplosions
from gamedata.scripting.check_finished import CheckFinished


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
        elif gamestate == INITIALIZE:
            self._build_init(entlist, script)

    #SCENE BUILDER METHODS

    def _build_init(self,entlist,script):
        self._initialize_script(script)

    def _build_lv1(self,entlist,script):
        pass
        #entities
        self._create_player(entlist)
        #script
        level = self._read_level_data(LEVEL1)
        self._input_script(script)
        self._update_script(script, "level1")
        self._output_script(script)



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
        player_animation = Animation(images = PLAYER_IMAGE)
        player.set_animation(player_animation)

    #SCRIPT METHODS
    def _input_script(self, script):
        script.clear_actions(INPUT)
        script.add_action(INPUT, ControlPlayer(self._ks))
        script.add_action(INPUT, PlayerBullets(self._ks))

    def _update_script(self, script, level, next):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, UpdateEnemies(self._ps))
        script.add_action(UPDATE, UpdateExplosions(self._ps))
        script.add_action(UPDATE, BorderCollision(self._ps))
        script.add_action(UPDATE, BulletOffscreen(self._ps))
        script.add_action(UPDATE, EnemyCollisions(self._ps))
        script.add_action(UPDATE, PlayerCollisions(self._ps))
        script.add_action(UPDATE, SpawnEnemy(level,next))
        script.add_action(UPDATE, CheckFinished(next))
        pass
    
    def _output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, StartDrawingAction(self._vs))
        script.add_action(OUTPUT, DrawEnemies(self._vs))
        script.add_action(OUTPUT, DrawEnemyBullets(self._vs))
        script.add_action(OUTPUT, DrawExplosions(self._vs))
        script.add_action(OUTPUT, DrawPlayerBullets(self._vs))
        script.add_action(OUTPUT, DrawPlayer(self._vs))
        script.add_action(OUTPUT, EndDrawingAction(self._vs))
        
        pass

    def _initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, InitializeDevicesAction(self._as,self._vs))
        script.add_action(INITIALIZE, LoadAssetsAction(self._as,self._vs))
        script.add_action(INITIALIZE, SwitchScreen(LEVEL1))
        pass

    #LEVEL DATA METHODS
    def _read_level_data(self, level_file):
        data = []
        with open(level_file) as file:
            next(file)
            for line in file:
                data.append(line)
        return data

