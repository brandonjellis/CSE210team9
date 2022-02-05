
import word as w
from terminal_display import game_display, game_input

class game:
    
    def __init__(self):
        self.guesses = []
        self.chances = 5
        self.display =  game_display() 
        self.inputs = game_input()
        self.word = w()
        self.is_playing = True

    def start_game(self):
        #loops through game logic defined below
        pass

    def verify_guess(self):
        #checks if the guess is correct or incorrect and appends score accoridingly 
        pass

    def check_gamestate(self):
        #checks all the values in the game to see if the player has won or lost. 
        pass
    
    
        
    
