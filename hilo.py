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

    #new card

    #scoring

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
        self.value = r(1,13)