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
from gamedata.control.handle_menu_action import HandleMenu

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
    script.add_action("gameloop",DrawActorsAction(vs,True))

    script.add_action("menu",DrawActorsAction(vs))
    script.add_action("menu",HandleMenu(ks))
    
    return script


def start_game(ent_list, script):
    
    def execute(act_list):
        actions = script.get_actions(act_list)
        gamestate = False
        while not gamestate:
            for action in actions:
                status = action.execute(ent_list,script)
                if status != None:
                    gamestate = status


    def reset():
        p1_pos = Point(c.P1_STARTX,c.STARTY)
        p2_pos = Point(c.P2_STARTX,c.STARTY)
        p1_vel = Point(0,c.CELL_SIZE)
        p2_vel = Point(0,c.CELL_SIZE)
        ent_list.remove_actors("p1")
        ent_list.remove_actors("p2")
        p1 = Cycle(c.BLUE, p1_pos, p1_vel,"@")
        p2 = Cycle(c.YELLOW, p2_pos, p2_vel,"@")
        ent_list.add_actor("p1",p1)
        ent_list.add_actor("p2",p2)

    reset()
    while vs.is_window_open():
        execute("menu")
        reset()
        execute("gameloop")
    
    pass


def main():
    ent_list = Entity_Manager()
    p1_score = Banner(Color(255,255,255), Point(0,0), Point(0,0), "Player 1 Score: ")
    p2_score = Banner(Color(255,255,255), Point(0,15), Point(0,0), "Player 2 Score: ")
    open_msg = Banner(Color(255,255,255), Point(c.MAX_X/2,c.MAX_Y/2), Point(0,0), "Welcome!\nPress SPACE to Start!")
    ent_list.add_actor("banners",open_msg)
    ent_list.add_actor("scores",p1_score)
    ent_list.add_actor("scores",p2_score)
    script = build_script()
    
    vs.open_window()
    start_game(ent_list,script)
    vs.close_window()





if __name__ == "__main__":
    main()