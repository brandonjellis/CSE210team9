from gamedata.services.video_service import Video_Service
from gamedata.services.keyboard_service import Keyboard_Service
from gamedata.control.gamemaster import Gamemaster

FRAME_RATE = 30
MAX_X = 1280
MAX_Y = 720

CAPTION = "Greed"


def main():

    keyboard = Keyboard_Service()
    video = Video_Service(CAPTION,MAX_X,MAX_Y,FRAME_RATE)
    master = Gamemaster(keyboard,video)

    master.start_game()

if __name__ == "__main__":
    main()
