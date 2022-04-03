from constants import *
from gamedata.scripting.action import Action
from gamedata.entities.explosion import Explosion


class EnemyCollisions(Action):
    def __init__(self, physics):
        self._ps = physics

    def execute(self, entities, script, callback):
        enemies = entities.get_entities(ENEMY_GROUP)
        bullets = entities.get_entities(BULLET_PLAYER_GROUP)

        for enemy in enemies:
            for bullet in bullets:
                if self._ps.has_collided(enemy, bullet):
                    enemy.take_damage(bullet.get_damage())
                    entities.remove_entitiy(BULLET_PLAYER_GROUP,bullet)
                    if enemy.get_life <= 0:
                        pos = enemy.get_position
                        entities.remove_entitiy(ENEMY_GROUP, enemy)
                        entities.add_entity(EXPLOSION_GROUP, Explosion(pos))
