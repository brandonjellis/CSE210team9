from cgitb import text
import csv
from turtle import position
from gamedata.entities.banner import Banner
from gamedata.scripting.draw_score_banner import DrawScoreBanner
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
from gamedata.scripting.update_enemies import UpdateEntities
from gamedata.scripting.update_explosions import UpdateExplosions
from gamedata.scripting.check_finished import CheckFinished


class RealityMaster:
    """
    generates the loop script for each state of the game and creates initial entities, returns script to be run to game master. 
    """
    def __init__(self,video,keyboard,physics,audio, entlist):
        self._vs = video
        self._ks = keyboard
        self._ps = physics
        self._as = audio
        self._entlist = entlist

    def change_script(self,gamestate,script):
        if gamestate == "level1":
            self._build_lv1(script)
        elif gamestate == "level2":
            self._build_lv2(script)
        elif gamestate == "level3":
            self._build_lv3(script)
        elif gamestate == INITIALIZE:
            self._build_init(script)

    #SCENE BUILDER METHODS

    def _build_init(self,script):
        self._initialize_script(script)

    def _build_lv1(self,script):
        pass
        #entities
        self._create_player()
        self._create_score_banner()
        #script
        level = self._read_level_data(LEVEL1)
        self._input_script(script)
        self._update_script(script, level, "level1")
        self._output_script(script)

    def _build_game_over():
        pass

    #ENTITY METHODS
    def _create_player(self):
        self._entlist.remove_entities(PLAYER)
        x = CENTER_X - PLAYER_WIDTH/2
        y = CENTER_Y - PLAYER_HEIGHT/2
        start_pos = Point(x,y)
        start_vel = Point(0,0)
        ent_size = Point(PLAYER_WIDTH,PLAYER_HEIGHT)
        player = Player(start_pos,start_vel,ent_size)
        player_animation = Animation(PLAYER_IMAGE)
        player.set_animation(player_animation)
        self._entlist.add_entity(PLAYER_GROUP, player)

    def _create_score_banner(self):
        self._entlist.remove_entities(SCORE)
        position = Point(15,15)
        score = Banner(position,text="SCORE: ")
        self._entlist.add_entity(SCORE, score)
        

    #SCRIPT METHODS
    def _input_script(self, script):
        script.clear_actions(INPUT)
        script.add_action(INPUT, ControlPlayer(self._ks))
        script.add_action(INPUT, PlayerBullets(self._ks, self._as))

    def _update_script(self, script, level, next):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, UpdateEntities())
        script.add_action(UPDATE, UpdateExplosions())
        script.add_action(UPDATE, BorderCollision(self._ps))
        script.add_action(UPDATE, EnemyCollisions(self._ps, self._as))
        script.add_action(UPDATE, PlayerCollisions(self._ps, self._as))
        script.add_action(UPDATE, BulletOffscreen())
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
        script.add_action(OUTPUT, DrawScoreBanner(self._vs))
        script.add_action(OUTPUT, EndDrawingAction(self._vs))
        
        pass

    def _initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, InitializeDevicesAction(self._as,self._vs))
        script.add_action(INITIALIZE, LoadAssetsAction(self._as,self._vs))
        script.add_action(INITIALIZE, SwitchScreen("level1"))
        pass

    #LEVEL DATA METHODS
    def _read_level_data(self, level_file):
        data = []
        with open(level_file) as file:
            reader = csv.reader(file)
            next(reader)
            for line in reader:
                line.append(False)
                data.append(line)
        return data

