
from word import word as w
from terminal_display import game_display, game_input

class game:
    
    def __init__(self, db = False):
        self.debug = db
        self._guesses = []
        self._chances = 4
        self._display = game_display()
        self._inputs = game_input()
        self._word = w()
        self._is_playing = True

    def start_game(self):
        #loops through game logic defined below

        self._word.choose_word()

        if(self.debug):
            print(self.word.get_word()) #debug print
            
        self.__game_out()
        while(self.is_playing):
            self.__game_in()
            self.__check_gamestate()
            self.__game_out()



    def __game_in(self):
        self._inputs.input(self._guesses)
        self._guesses.append(self._inputs.get_input())

    def __check_gamestate(self):
        #checks all the values in the game to see if the player has won or lost. 
        if not(self._word.check_char(self._guesses[-1])):
            self._chances -= 1
        if self._chances <= 0:
            self.is_playing = False
            self._display.print_defeat(self._word.get_word())
        all_guessed = True
        for c in self._word.get_word():
            if c not in self.guesses:
                all_guessed = False
        if all_guessed:
            self.is_playing = False
            self._display.print_win()

    def __game_out(self):
        self._display.draw_display(self._chances, self._guesses, self._word.get_word())

    
    
        
    
