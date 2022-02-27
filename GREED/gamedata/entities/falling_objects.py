#Child class to "entity" which contains additional information relating to the falling rocks and gems
#such as the score value, icon, etc.

from entity import Entity

class Object(Entity):
    def __init__(self):
        super().__init__()
        self._points = 100

    def get_points(self):
        return self._points

    def set_points(self, points):
        self._points = points