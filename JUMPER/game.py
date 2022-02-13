
from word import word as w
from terminal_display import game_display, game_input

class game:
    
    def __init__(self):
        self.guesses = []
        self.chances = 4
        self.display =  game_display()
        self.inputs = game_input()
        self.word = w()
        self.is_playing = True

    def start_game(self):
        #loops through game logic defined below

        self.word.choose_word()
        print(self.word.get_word())
        self.game_out()
        while(self.is_playing):
            self.game_in()
            self.check_gamestate()
            self.game_out()



    def game_in(self):
        self.inputs.input(self.guesses)
        self.guesses.append(self.inputs.get_input())

    def check_gamestate(self):
        #checks all the values in the game to see if the player has won or lost. 
        if not(self.word.check_char(self.guesses[-1])):
            self.chances -= 1
        if self.chances <= 0:
            self.is_playing = False
            self.display.print_defeat(self.word.get_word())
        all_guessed = True
        for c in self.word.get_word():
            if c not in self.guesses:
                all_guessed = False
        if all_guessed:
            self.is_playing = False
            self.display.print_win()

    def game_out(self):
        self.display.draw_display(self.chances, self.guesses, self.word.get_word())

    
    
        
    
