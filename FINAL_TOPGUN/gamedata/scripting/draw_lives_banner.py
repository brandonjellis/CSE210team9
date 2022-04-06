from turtle import position
from constants import *
from gamedata.scripting.action import Action

class DrawLivesBanner(Action):
    def __init__(self, video_service):
        self._video_service = video_service
    
    def execute(self, entities, script, callback):
        player = entities.get_first_entity(PLAYER)
        lives = entities.get_first_entity(LIVES)
        position = lives.get_position()
        life = player.get_life()

        msg = lives._dtxt + str(life)
        lives.set_text(msg)
        text = lives.get_text()

        self._video_service.draw_text(text, position)

        