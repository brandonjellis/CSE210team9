import constants as c

from gamedata.entites.entity_manager import Entity_Manager
from gamedata.entites.entity import Entity
from gamedata.entites.cycle import Cycle
from gamedata.entites.banner import Banner

from gamedata.control.script import Script
from gamedata.control.control_actors_action import ControlActorsAction
from gamedata.control.move_actors_action import MoveActorsAction
from gamedata.control.handle_collisions_action import HandleCollisionsAction
from gamedata.control.draw_actors_action import DrawActorsAction

from gamedata.services.keyboard_service import KeyboardService
from gamedata.services.video_service import VideoService

from gamedata.misc.color import Color
from gamedata.misc.point import Point

ks = KeyboardService()
vs = VideoService()

def build_script():
    script = Script()
    script.add_action("gameloop",ControlActorsAction(ks))
    script.add_action("gameloop",MoveActorsAction())
    script.add_action("gameloop",HandleCollisionsAction())
    script.add_action("gameloop",DrawActorsAction(vs))

    script.add_action("menu",ControlActorsAction(ks))
    script.add_action("menu",DrawActorsAction(vs))
    
    return script


def start_game(ent_list, script):
    p1_score = Banner(Color(), Point(0,0), Point(0,0), "Player 1 Score: ")
    p2_score = Banner(Color(), Point(0,15), Point(0,0), "Player 2 Score: ")
    ent_list.add_actor("scores",p1_score)
    ent_list.add_actor("scores",p2_score)

    def execute(act_list):
        actions = script.get_actions(act_list)
        for action in actions:
            game = action.execute(ent_list,script)

    def reset():
        ent_list.remove_actors("p1")
        ent_list.remove_actors("p2")

        p1_pos = Point(c.P1_STARTX,c.STARTY)
        p2_pos = Point(c.P2_STARTX,c.STARTY)
        p1_vel = Point(0,c.CELL_SIZE)
        p2_vel = Point(0,c.CELL_SIZE*-1)
        p1 = Cycle(c.BLUE, p1_pos, p1_vel,"@")
        p2 = Cycle(c.YELLOW, p2_pos, p2_vel,"@")

        ent_list.add_actor("p1",p1)
        ent_list.add_actor("p2",p2)
    pass


def main():
    ent_list = Entity_Manager()
    ent_list.add_actor("Banners",Banner())
    ent_list.add_actor("Banners",Banner())
    


    script = build_script()
    
    vs.open_window()

    op_msg = Banner()
    op_msg.set_text("Welcome!\nPress SPACE to begin.")
    op_msg.set_position(Point(c.MAX_X/2,c.MAX_Y/2))

    ent_list.add_actor("messages",op_msg)

    start_game(ent_list,script)
    





if __name__ == "__main__":
    main()