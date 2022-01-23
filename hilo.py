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

    #get inputs

    #outputs

    

class card:
    def __init__(self):
        self.value = r(1,13)