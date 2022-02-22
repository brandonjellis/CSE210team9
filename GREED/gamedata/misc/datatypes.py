#Contains classes defining specialty datatypes used throughout the program.
import math

class Vector:
    def __init__(self,x = 0, y = 0, z = 0):
        self._xdir = x
        self._ydir = y
        self._zdir = z

    def get_magnitude(self):
        m = math.sqrt((self._xdir)**2 + (self._ydir)**2 + (self._zdir)**2)
        return m

    def get_component(self):
        return (self._xdir, self._ydir, self._zdir)

    def set_x(self,x):
        self._xdir = x

    def set_y(self,y):
        self._ydir = y

    def set_z(self,z):
        self._zdir = z


class Color:
    def __init__(self, red = 255, green = 255, blue = 255, alpha = 255):
        self._red = red
        self._green = green
        self._blue = blue
        self._alpha = alpha

    def set_color(self,RGBA):
        self._red = 255 if RGBA[0] >= 255 else RGBA[0]
        self._green = 255 if RGBA[1] >= 255 else RGBA[1]
        self._blue = 255 if RGBA[2] >= 255 else RGBA[2]
        self._alpha = 255 if RGBA[3] >= 255 else RGBA[3]

    def get_color(self):
        return (self._red, self._blue, self._green, self._alpha)

