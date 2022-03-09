import constants

from gamedata.entites.entity_manager import Entity_Manager
from gamedata.entites.entity import Entity
from gamedata.entites.cycle import Cycle
from gamedata.entites.banner import Score

from gamedata.control.script import Script
from gamedata.control.control_actors_action import ControlActorsAction
from gamedata.control.move_actors_action import MoveActorsAction
from gamedata.control.handle_collisions_action import HandleCollisionsAction
from gamedata.control.draw_actors_action import DrawActorsAction

from gamedata.services.keyboard_service import KeyboardService
from gamedata.services.video_service import VideoService

from gamedata.misc.color import Color
from gamedata.misc.point import Point


def build_script(ks,vs):
    script = Script()
    script.add_action("inputs",ControlActorsAction(ks))
    script.add_action("updates",MoveActorsAction())
    script.add_action("updates",HandleCollisionsAction())
    script.add_action("Outputs",DrawActorsAction(vs))
    return script


def start_round(ent_list, script):
    
    p1 = Cycle()
    p2 = Cycle(constants.YELLOW,)


def main():
    ent_list = Entity_Manager()
    ent_list.add_actor("scores",Score())
    ent_list.add_actor("scores",Score())
    ks = KeyboardService()
    vs = VideoService()

    #p1_pos = 

    script = build_script(ks,vs)

    vs.open_window()
    while vs.is_window_open():
        start_round(ent_list,script)
    vs.close_window()
    





if __name__ == "main":
    main()