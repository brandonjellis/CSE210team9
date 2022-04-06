from constants import *
from gamedata.datatypes.animation import Animation
from gamedata.datatypes.point import Point
from gamedata.scripting.action import Action
from gamedata.entities.enemy import Type1,Type2,Type3,TypeBoss
from time import time

class SpawnEnemy(Action):
    """
    Reads data from level file and spawns enemies
    at the specified time and location
    """
    def __init__(self, levelfile, next):
        self._data = levelfile
        self._start = time()
        self._next = next
        


    def execute(self, entities, script, callback):
        current = time()
        dt = (current - self._start)
        for line in self._data:
            t = float(line[0])
            if (dt >= t and line[3] == False):
                line[3] = True
                new_enemy = None
                x = int(line[1])
                pos = Point(x,-10)
                enemy_type = int(line[2])

                if enemy_type == 1:
                    new_enemy = Type1(pos,Point(0,0),Point(ENEMY_WIDTH,ENEMY_HEIGHT))
                    new_enemy.set_animation(Animation(ENEMY_IMAGE1))
                elif enemy_type == 2:
                    new_enemy = Type2(pos,Point(0,0),Point(ENEMY_WIDTH,ENEMY_HEIGHT))
                    new_enemy.set_animation(Animation(ENEMY_IMAGE6))
                elif enemy_type == 3:
                    new_enemy = Type3(pos,Point(0,0),Point(ENEMY_WIDTH,ENEMY_HEIGHT))
                    new_enemy.set_animation(Animation(ENEMY_IMAGE2))
                elif enemy_type == 4:
                    new_enemy = TypeBoss(pos,Point(0,0),Point(ENEMY_WIDTH,ENEMY_HEIGHT))
                    new_enemy.set_animation(Animation(ENEMY_IMAGE1))
                elif enemy_type == 5:
                    self._start = time()
                    for line in self._data:
                        line[3] = False
                    
                if new_enemy != None:
                    entities.add_entity(ENEMY_GROUP, new_enemy)




