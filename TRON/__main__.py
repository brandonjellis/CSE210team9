import constants as c

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
    script.add_action("gameloop",ControlActorsAction(ks))
    script.add_action("gameloop",MoveActorsAction())
    script.add_action("gameloop",HandleCollisionsAction())
    script.add_action("gameloop",DrawActorsAction(vs))
    return script


def start_round(ent_list, script):
    p1_pos = Point(c.P1_STARTX,c.STARTY)
    p2_pos = Point(c.P2_STARTX,c.STARTY)
    p1_vel = Point(0,-c.CELL_SIZE)
    p2_vel = Point(0,c.CELL_SIZE)
    p1 = Cycle(c.BLUE, p1_pos, p1_vel)
    p2 = Cycle(c.YELLOW, p2_pos, p2_vel)

    ent_list.add_actor("p1",p1)
    ent_list.add_actor("p2",p2)
    
    ent_list.remove_actor("messages",ent_list.get_first_actor("messages"))

    game_over = False
    while game_over != True:
        actions = script.get_actions("gameloop")
        for action in actions:
            game_over = action.execute(ent_list,script)
    

def main():
    ent_list = Entity_Manager()
    ent_list.add_actor("scores",Score())
    ent_list.add_actor("scores",Score())
    ks = KeyboardService()
    vs = VideoService()

    script = build_script(ks,vs)

    vs.open_window()

    op_msg = Score()
    op_msg.set_text("Welcome!\nPress SPACE to begin.")
    op_msg.set_position(Point(c.MAX_X/2,c.MAX_Y/2))
    vs.draw_actor(op_msg)

    while vs.is_window_open():
        if ks.is_key_down("space"):
            start_round(ent_list,script)
    vs.close_window()
    





if __name__ == "main":
    main()