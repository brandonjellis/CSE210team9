from constants import *
from gamedata.scripting.action import Action

class DrawScoreBanner(Action):
    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, entities, script, callback):
        score = entities.get_first_entity(SCORE)
        text = score.get_text()
        position = score.get_position()
        self._video_service.draw_text(text, position)