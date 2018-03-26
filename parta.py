###
# Main entry point into the program for Part A of the project
# Contains the code which will utilise the other modules written and run
# the code to:
#   Read in the board from an input file
#   Print out the number of moves available for each player
#   Print out the sequence of moves to eliminate all black pieces on the board
###

# Import all related modules
from board_state import *

# Read the initial state of the board from stdin
initial_state = BoardState('I')
command = input()
