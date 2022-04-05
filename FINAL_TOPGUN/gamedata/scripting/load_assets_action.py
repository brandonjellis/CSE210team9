from gamedata.scripting.action import Action
from constants import *

class LoadAssetsAction(Action):

    def __init__(self, audio_service, video_service):
        self._audio_service = audio_service
        self._video_service = video_service

    def execute(self, cast, script, callback):
        self._audio_service.load_sounds(PATH + "FINAL_TOPGUN\\assets\\sounds")
        self._video_service.load_fonts(PATH + "FINAL_TOPGUN\\assets\\fonts")
        self._video_service.load_images(PATH + "FINAL_TOPGUN\\assets\\images")
        