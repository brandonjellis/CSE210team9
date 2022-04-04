from constants import *
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
        dt = current - self._start
        for line in self._data:
            t = line[0]
            if dt == t:
                new_enemy = None
                pos = Point(line[1],-10)
                enemy_type = line[2]

                if enemy_type == 1:
                    new_enemy = Type1(pos,Point(0,0),Point(ENEMY_WIDTH,ENEMY_HEIGHT))
                elif enemy_type == 2:
                    new_enemy = Type2(pos,Point(0,0),Point(ENEMY_WIDTH,ENEMY_HEIGHT))
                elif enemy_type == 3:
                    new_enemy = Type3(pos,Point(0,0),Point(ENEMY_WIDTH,ENEMY_HEIGHT))
                elif enemy_type == 4:
                    new_enemy = TypeBoss(pos,Point(0,0),Point(ENEMY_WIDTH,ENEMY_HEIGHT))
                elif enemy_type == 5:
                    callback.next_state(self._next)
                    
                if new_enemy != None:
                    entities.add_entity(ENEMY_GROUP, new_enemy)


