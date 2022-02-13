


class game_display:
    def __init__(self):
        self.character_list = []
        pass

    def draw_display(self, chances, guesses, word):
        #Call all the other draw methods to display the whole picture of the board.

        self.draw_word(word, guesses)
        print()
        self.draw_parachute(chances)
        self.draw_constant()
        print()
        game_input.get_input(guesses)
        
        

    def draw_word(self, word, guesses):
        #Get the word from self and draw the undercores necessary for the specific each letter.
        #If the user guesses one letter, it's going to draw the letter instead of an underscore
        #and draw underscore for the rest of the letters the user has guessed."
        
        for c in word:
            if c in guesses:
                print(c, end = " ")
            else:
                print("_", end = " ")



    def draw_parachute(self, chances):
        #Get the amount of guesses left. It runs a loop to draw the parachute. 
        #Depending of how many guesses the user have left, it is the amount of time that is going to loop. 
        #Every time the user guesses incorrectly, the program will skip first component in the array."
        parachute = ["  ___  "," /___\ "," \   / ","  \ /  "]

        
            
        x = 4 - chances
        for i in range(chances):
            i += x
            print(parachute[i])
        

        if chances == 0:
            print("   x   ")

        else:
            print("   0   ")


    def draw_constant(self):
        print("  /|\  ")
        print("  / \  ")
        print()
        print("^^^^^^^")
        

    def print_defeat(self):
        #Print a defeat message if the user losses
        print("You Lose!")
        pass

    def print_win(self):
        #Print a winner message if the user wins
        print ('You Win!')
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
                valid = False

            if self.verify_repeat(user_input, guesses):
                valid = True
            
            else:
                print("That's a repeated character. Please, type in a different character. ")
                valid = False

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
        return self._input
