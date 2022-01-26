'''
HILO CARD GAME
CSE210 TEAM 9 01/22/2022
Brandon Ellis, Luis Cardenas, David Watkins

'''
from random import randint as r

class game:
    def __init__(self):
        self.score = 0
        self.round = 1
        self.gameloop = True
        self.old_card = card()
        self.new_card = None

    #gameloop
    def run_game(self):
        while(self.gameloop):
            self.get_inputs()
            self.draw_card()
            self.count_score()
            self.get_outputs()
            self.check_continue()

    def check_continue(self):
        response = (input("Continue playing?\nY/N\n> ")).lower()
        if response == "y":
            self.gameloop = True
        elif response == "n":
            self.gameloop = False
        else:
            print("Error: Invalid Response")
            self.check_continue()

    #new card
    def draw_card(self):
        pass

    #scoring
    def count_score(self):
        pass

    #get inputs
    def get_inputs(self):
        pass

    #outputs
    def get_outputs(self):
        pass

    

class card:
    def __init__(self):
        self.value = 1
        self.new_value()

    def new_value(self):
        self.value = r(1,13)


