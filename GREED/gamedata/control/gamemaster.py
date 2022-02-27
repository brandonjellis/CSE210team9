#primary game logic class. Contains scoring logic and handles the other classes.
#It's only going to call entity_manager, datatypes, keyboard_service and video_service.

from gamedata.entities.entity_manager import Entity_Manager
from gamedata.entities.entity import Entity
from gamedata.entities.falling_objects import Object

from gamedata.misc.datatypes import Color, Point

from random import randint



class Gamemaster:
    
    def __init__(self, keyboard, video):
        self._keyboard = keyboard
        self._video = video
        self._entities = Entity_Manager()
        self._score = 0
        self._max_objects = 20
        

    def start_game(self):
        self._video.open_window()
        self.initialize()
        while self._video.is_window_open():
            self.inputs()
            self.update_gamestate()
            self.outputs()
        self._video.close_window()


    def create_player(self):
        player = Entity(True)
        mx = self._video.get_width()
        my = self._video.get_height() /2
        player.set_max(mx, my)
        player.set_icon("#")
        player.set_color(Color())
        player.set_size(15)
        mx /= 2
        player.set_position(Point(mx,my))

        self._entities.add_entitiy("player",player)

    def create_gem(self):
        gem = Object()
        y = 0
        x = randint(0, self._video.get_width())
        gem.set_velocity(Point(0,randint(-3,-1)))
        gem.set_position(Point(x,y))
        r = randint(150,255)
        g = randint(150,255)
        b = randint(150,255)
        color = Color(r,g,b)
        gem.set_color(color)
        gem.set_icon("*")
        gem.set_size(20)
        gem.set_points(100)

        self._entities.add_entitiy("objects",gem)

    def create_rock(self):
        rock = Object()
        y = 0
        x = randint(0, self._video.get_width())
        rock.set_velocity(Point(0,randint(-3,-1)))
        rock.set_position(Point(x,y))
        r = randint(50,150)
        g = randint(50,150)
        b = randint(50,150)
        color = Color(r,g,b)
        rock.set_color(color)
        rock.set_icon("o")
        rock.set_size(15)
        rock.set_points(-150)

        self._entities.add_entitiy("objects",rock)

    def initialize(self):
        self.create_player()

    def inputs(self):
        player = self._entities.get_first_entity("player")
        velocity = self._keyboard.get_position()
        player.set_velocity(velocity)

    def update_gamestate(self):
        player = self._entities.get_first_entity("player")
        objects = self._entities.get_entities("objects")

        player.update_pos()

        for object in objects:
            if (object.get_position.point_2d[1] < self._video.get_height()):
                self._entities.del_entity(object)
            elif (player.get_position.distance(object.get_position.point_2d()) < 15):
                self._score += object.get_points()
                self._entities.del_entity(object)

        while(len(self._entities.get_entities("objects")) < self._max_objects):
            self.create_gem()
            self.create_rock()

    def outputs(self):
        self._video.clear_buffer()
        entities = self._entities.get_all()
        self._video.draw_actors(entities)
        self._video.flush_buffer()


        
