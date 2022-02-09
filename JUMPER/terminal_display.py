
class game_display:
    def __init__(self):
        self.character_list = []
        pass

    def draw_display(self):
        #Call all the other draw methods to display the whole picture of the board.
        pass

    def draw_word(self, word, guesses):
        #Get the word from self and draw the undercores necessary for the specific each letter.
        #If the user guesses one letter, it's going to draw the letter instead of an underscore
        #and draw underscore for the rest of the letters the user has guessed."
        pass

    def draw_parachute(self, chances):
        #Get the amount of guesses left. It runs a loop to draw the parachute. 
        #Depending of how many guesses the user have left, it is the amount of time that is going to loop. 
        #Every time the user guesses incorrectly, the program will skip first component in the array."

        pass

    def draw_constant(self):
        print("  /|\  ")
        print("  / \  ")
        print()
        print("^^^^^^^")
        

    def print_defeat(self):
        #Print a defeat message if the user losses
        pass

    def print_win(self):
        #Print a winner message if the user wins
        pass

class game_input:
    def __init__(self):
        self._input = ""
    
        pass
    
    def input(self, guesses):
        #Get an input from the user. Looping until the input is valid and store the value into self.input. Call the verifying methods.
       
        valid = False
        while not valid:
            user_input = input("Guess a letter [a-z]: ")
            if self.verify_valid(user_input):
                self._input = user_input
                valid = True

            else:
                print("Invalid input. Try again.")

            if self.verify_repeat(user_input, guesses):
                valid = True
            
            else:
                print("That's a repeated character. Please, type in a different character. ")

                


    def verify_valid(self, user_input):
        #Print a message for the user that he used an invalid input
        if user_input.isalpha():
            if len(user_input) == 1:
                return True
        return False


    def verify_repeat(self, user_input, guesses):
        #Print a message for the user that he already used that letter
        if user_input in guesses:
            return False
        return True

        

    def get_input(self):
        #returns self.input
        pass