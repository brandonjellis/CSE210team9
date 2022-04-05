from constants import *
from gamedata.entities.explosion import Explosion
from gamedata.scripting.action import Action


class PlayerCollisions(Action):
    def __init__(self,physics, audio_service):
        self._ps = physics
        self._as = audio_service

    def execute(self, entities, script, callback):
        player = entities.get_first_entity(PLAYER_GROUP)
        bullets = entities.get_entities(BULLET_ENEMY_GROUP)

        for i in bullets:
            if (player.get_invincible() == False):
                if(self._ps.has_collided(player,i)):
                    player.got_hit()
                    pos = player.get_position
                    entities.remove_entity(BULLET_ENEMY_GROUP, i)
                    entities.add_entity(EXPLOSION_GROUP, Explosion(pos))
                    self._as.play_sound(EXPLOSION_SOUND)

