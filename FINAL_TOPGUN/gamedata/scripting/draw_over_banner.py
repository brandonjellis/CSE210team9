from constants import *
from gamedata.scripting.action import Action


class drawOverBanner(Action):
    def __init__(self, video):
        self._vs = video

    def execute(self, entities, script, callback):
        banner = entities.get_first_entity(GAME_OVER)
        position = banner.get_position()

        msg = banner.get_text()

        self._vs.draw_text(msg, position)