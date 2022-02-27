CSC210 Team 9
Brandon Ellis, Luis Cardenas, David Watkins

Requires up to date version of raylib
Run the main function to start the program. 

Greed
Control the Prospector "#" as he tries to collect gems "*" while avoiding falling rocks "o" !
Controls:
Arrow keys for movement


Class structure and Options:
Game structure is as follows:

main:
*initializes keyboard and video managers and creates the window
*creates a gamemaster and runs the game

gamemaster:
* controls game logic and dataflow
* creates player and other game objects stored in an entity manager
* stores overall score and creates score display


entity_manager:
*contains methods used for managing a dictionary of game objects

entity:
*contains base abtributes for a game object including its color, location, velocity.

falling_objects:
*child class of entity storing an aditional point value.

keyboard_service:
*reads keyboard input and generates a velocity value for the player character

video_service:
*handles raylib calls and draws the game to the screen.

datatypes:
-Point
*datatype for a 2 or 3 dimensional point in space
*used for the position and velocity values

-Color:
*datatype for a RGBA format color




