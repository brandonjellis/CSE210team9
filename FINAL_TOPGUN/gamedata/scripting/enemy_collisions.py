from constants import *
from gamedata.scripting.action import Action
from gamedata.entities.explosion import Explosion


class EnemyCollisions(Action):
    def __init__(self, physics, audio):
        self._ps = physics
        self._as = audio

    def execute(self, entities, script, callback):
        enemies = entities.get_entities(ENEMY_GROUP)
        bullets = entities.get_entities(BULLET_PLAYER_GROUP)
        score = entities.get_first_entity(SCORE)
        points = 1

        for enemy in enemies:
            for bullet in bullets:
                if self._ps.has_collided(enemy, bullet):
                    enemy.take_damage(bullet.get_damage())
                    entities.remove_entity(BULLET_PLAYER_GROUP,bullet)
                    if enemy.get_life() <= 0:
                        pos = enemy.get_position()
                        entities.remove_entity(ENEMY_GROUP, enemy)
                        entities.add_entity(EXPLOSION_GROUP, Explosion(pos))
                        self._as.play_sound(EXPLOSION_SOUND)
                        score.add_point(points)
                        

