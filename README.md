# CSE210team9
Team repo for cse 210 for w22

Brandon Ellis   [ell20018@byui.edu]
Luis Cardenas   [car20116@byui.edu]
David Watkins   [wat15020@byui.edu]

#######################################################################
HILO
game class methods:

#gameloop: (Brandon)
loop while gameloop is true
runs other methods
gameloop order
-get imputs
-new card
-scoring
-outputs

new card: (David)
move current card to old card
genereate new card

#scoring (David)
compare old and new card to user guess
append score

#get inputs (Luis)
print value of old card
ask user for guess and save

#outputs  (Luis)
print new card 
print if guess was correct
print new score
#####################################################################################
JUMPER 
classes:
"game_master"
-in charge of external program controls ie. starting/ending the game

"game"
-contains overall game logic,
-tracks remaining guesses, previous guesses, 
-implements overall game rules. 

"word"
-contains list of possible words,
-can pick a word at random as the chosen word
-can return t/f if given letter is in the chosen word
-can provide the chosen word to other programs

"input"
-gets guess from terminal input
-filters invalid inputs or letters already chosen

"display"
-prints current game state to terminal