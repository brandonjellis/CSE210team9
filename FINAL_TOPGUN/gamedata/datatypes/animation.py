
from gamedata.datatypes.image import Image
import time

class Animation:
    '''
    Animation datatype. contains a list of several image datatypes 
    plus several parameters for switching the current frame
    '''
    def __init__(self, delay = 1, loop = False, images = [Image(None)]):
        self._images = images
        self._frame = self._images[0]
        self._index = 0
        self._delay = delay
        self._loop = loop
        self._start = time.time()
        self._looptime = time.time()

    def next(self):
        #switches current image to next image based on parameters.
        next_index = self._index + 1
        if self._loop:
            now = time.time()
            d_time = now - self._looptime
            if d_time >= self._delay:
                if next_index >= len(self._images):
                    next_index = 0
        else:
            if next_index >= len(self._images):
                next_index = len(self._images) - 1
        self._index = next_index
        self._frame = self._images[self._index]

    def previous(self):
        next_index = self._index - 1
        if next_index < 0:
            next_index = 0
        self._index = next_index
        self._frame = self._images[self._index]

    def set_frame(self,index):
        if index >= 0 and index < len(self._images):
            self._index = index
            self._frame = self._images[index]

    
    def add_image(self,image):
        #appends passed image into stored images
        self._images.append(image)

    def get_frame(self):
        return self._frame