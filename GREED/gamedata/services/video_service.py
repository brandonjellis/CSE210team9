#Uses pyray to generate the game window and display the game to the user.

import pyray 

class Video_Service:
    def __init__(self, caption, width, height, frame_rate):
        self._caption = caption
        self._width = width
        self._height = height
        self._frame_rate = frame_rate
    
    def close_window(self):
        pyray.close_window()

    def clear_buffer(self):
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()
    
    def draw_actor(self, entity):
        text = entity.get_icon()
        point = entity.get_position().point_2d()
        font_size = entity.get_size()
        color = entity.get_color().get_color()
        pyray.draw_text(text, point[0], point[1], font_size, color)
        
    def draw_actors(self, entities):
        for entity in entities:
            self.draw_actor(entity)
    
    def flush_buffer(self):
        pyray.end_drawing()


    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def is_window_open(self):
        return not pyray.window_should_close()

    def open_window(self):
        pyray.init_window(self._width, self._height, self._caption)
        pyray.set_target_fps(self._frame_rate)
