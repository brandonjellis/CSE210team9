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

    def get_inputs(self):
        first_card = self.old_card
        print(f"The car is: {first_card}")
        user_guess = input("Higher or lower? [h/l] ")
        if first_card == user_guess :
            return True
        else:
            return False

    def get_outputs(self):
        print(f"Next card was: {self.new_card.value}")
        
        print(f"Your score is: {self.score}")
        


    

class card:
    def __init__(self):
        self.value = 1
        self.new_value()

    def new_value(self):
        self.value = r(1,13)


