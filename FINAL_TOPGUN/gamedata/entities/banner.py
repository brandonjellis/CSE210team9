
from gamedata.entities.entity import Entity

class Banner(Entity):
    def __init__(self, position=..., velocity=..., size=..., text=""):
        super().__init__(position, velocity, size)
        self._text = text
        self._font_size = 15
        self._value = 0

    def get_font_size(self):
        return self._font_size
    
    def get_text(self):
        msg = self._text + str(self._value)
        return msg

    def set_font_size(self, font_size):
        self._font_size = font_size

    def set_text(self, text):
        self._text = text

    def add_point(self, points):
        self._value += points
        
