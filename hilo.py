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
        self.new_card = card()

    #gameloop
    def run_game(self):
        while(self.gameloop):
            guess = self.get_inputs()
            self.draw_card()
            self.count_score(guess)
            self.get_outputs()
            self.check_continue()

    def check_continue(self):
        if self.score <= 0:
            self.gameloop = False
            print("Score too low... GAME OVER!")
        else:
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
        self.old_card.value = self.new_card.value
        self.new_card.new_value()

    #scoring
    def count_score(self,guess):
        if self.old_card.value < self.new_card.value:
            if guess:
                self.score += 100
            elif not guess:
                self.score -= 75
        elif self.old_card.value > self.new_card.value:
            if guess:
                self.score -= 75
            elif not guess: 
                self.score += 100

    def get_inputs(self):
        print(f"The card is: {self.new_card.value}")
        user_guess = input("Higher or lower? [h/l] ").lower
        if user_guess == 'h':
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

def main():
    g = game()
    g.run_game()


if __name__ == "__main__":
    main()

