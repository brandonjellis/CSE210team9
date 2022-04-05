from time import time
from gamedata.entities.bullet import Bullet
from gamedata.datatypes.animation import Animation
from constants import *
import math

from gamedata.entities.entity import Entity
from gamedata.datatypes.point import Point

class Enemy(Entity):
    """
    base enemy class template used for other enemy types
    """
    def __init__(self,pos,vel,size):
        super().__init__(pos,vel,size)
        self._life = 10
        self._lifetime = time()
        self._fire_delay = 10
        self._last_fire = time()
        
    def _xmove(self,dt):
        pass

    def _ymove(self,dt):
        pass

    def move_next(self):
        now = time()
        dt = now - self._lifetime
        x = self._xmove(dt)
        y = self._ymove(dt)
        newpos = Point(x,y)
        self._position = newpos

    def fire(self,entlist):
        pass

    def take_damage(self, damage):
        self._life -= damage  

    def get_life(self):
        return self._life

    pass

class Type1(Enemy):
    def __init__(self, pos, vel, size):
        super().__init__(pos, vel, size)

    def _xmove(self, dt):
        return round(CONSTANT_FUNCTION*math.log10(dt))

    def _ymove(self, dt):
        return self._position.get_y()

    def fire(self, entlist):
        current = time()
        if current - self._last_fire > self._fire_delay:
            self._last_fire = current
            player = entlist.get_first_entity(PLAYER_GROUP)
            player_position = player.get_position()
            x2 = player_position.get_x()
            y2 = player_position.get_y()

            enemy = entlist.get_first_entity(ENEMY_GROUP)
            enemy_position = enemy.get_position()
            x1 = enemy_position.get_x()
            y1 = enemy_position.get_y()

            x = x1 + ENEMY_WIDTH/2
            y = y1 + ENEMY_HEIGHT

            magnitude = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            unit_vector = Point((x2-x1)/magnitude,(y2-y2)/magnitude)
            velocity = BULLET_VELOCITY * unit_vector

            bullet_position = Point(x,y)
            bullet_size = Point(BULLET_WIDTH,BULLET_HEIGHT)
            bullet_velocity = velocity

            new_bullet = Bullet()
            new_bullet.set_position(bullet_position)
            new_bullet.set_velocity(bullet_velocity)
            new_bullet.set_size(bullet_size)
            new_bullet.set_animation(Animation(BULLET_IMAGE1))
            bullet = entlist.add_entity(BULLET_ENEMY_GROUP, new_bullet)


class Type2(Enemy):
    def __init__(self, pos, vel, size):
        super().__init__(pos, vel, size)

    def _xmove(self, dt):
        return round(CONSTANT_FUNCTION*math.cos(dt))

    def _ymove(self, dt):
        return round(CONSTANT_FUNCTION*math.sin(dt) + 100)

    def fire(self, entlist):
        current = time()
        if current - self._last_fire > self._fire_delay:
            self._last_fire = current
            enemy = entlist.get_first_entity(ENEMY_GROUP)
            enemy_position = enemy.get_position()
            x = enemy_position.get_x() + ENEMY_WIDTH/2
            y = enemy_position.get_y() + ENEMY_HEIGHT

            velocity = [Point(1,0), Point(-1,0), Point(0, 1), Point(math.sqrt(3)/2, 1/2), Point(math.sqrt(2)/2, math.sqrt(2)/2), Point(1/2, math.sqrt(3)/2), Point(-1/2, math.sqrt(3)/2), Point(-math.sqrt(2)/2, math.sqrt(2)/2), Point(-math.sqrt(3)/2, 1/2)]

            bullet_position = Point(x,y)
            bullet_size = Point(BULLET_WIDTH,BULLET_HEIGHT)

            for i in range(0,9):
                new_bullet = Bullet()
                new_bullet.set_position(bullet_position)
                new_bullet.set_velocity(BULLET_VELOCITY * velocity[i])
                new_bullet.set_size(bullet_size)
                new_bullet.set_animation(Animation(BULLET_IMAGE2))
                bullet = entlist.add_entity(BULLET_ENEMY_GROUP, new_bullet)



class Type3(Enemy):
    def __init__(self, pos, vel, size):
        super().__init__(pos, vel, size)

    def _xmove(self, dt):
        return round(CONSTANT_FUNCTION*math.sin(2*dt))

    def _ymove(self, dt):
        return round(CONSTANT_FUNCTION*math.sin(dt) + 100)

class TypeBoss(Enemy):
    def __init__(self, pos, vel, size):
        super().__init__(pos, vel, size)
        self._current_loop = 0

    def _xmove(self, dt):
        return round((CONSTANT_FUNCTION*4)*math.sin(0.01*dt))

    def _ymove(self, dt):
        return round((CONSTANT_FUNCTION/2)*math.log10(dt+1))

    def fire(self, entlist):
        current = time()
        if current - self._last_fire > self._fire_delay:
            self._last_fire = current
            enemy = entlist.get_first_entity(ENEMY_GROUP)
            enemy_position = enemy.get_position()
            x = enemy_position.get_x() + ENEMY_WIDTH/2
            y = enemy_position.get_y() + ENEMY_HEIGHT

            velocity = [Point(1,0), Point(-1,0), Point(0, 1), Point(math.sqrt(3)/2, 1/2), Point(math.sqrt(2)/2, math.sqrt(2)/2), Point(1/2, math.sqrt(3)/2), Point(-1/2, math.sqrt(3)/2), Point(-math.sqrt(2)/2, math.sqrt(2)/2), Point(-math.sqrt(3)/2, 1/2)]

            bullet_position = Point(x,y)
            bullet_size = Point(BULLET_WIDTH,BULLET_HEIGHT)

            
            new_bullet = Bullet()
            new_bullet.set_position(bullet_position)
            new_bullet.set_velocity(BULLET_VELOCITY * velocity[self._current_loop])
            new_bullet.set_size(bullet_size)
            new_bullet.set_animation(Animation(BULLET_IMAGE4))
            bullet = entlist.add_entity(BULLET_ENEMY_GROUP, new_bullet)
            self._current_loop += 1
            if self._current_loop == 9:
                self._current_loop = 0


    

    
