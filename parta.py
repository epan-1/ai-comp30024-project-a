###
# Main entry point into the program for Part A of the project
# Contains the code which will utilise the other modules written and run
# the code to:
#   Read in the board from an input file
#   Print out the number of moves available for each player
#   Print out the sequence of moves to eliminate all black pieces on the board
###

# Import all related modules
from move import *
from board_state import *

# Read the initial state of the board from stdin
initial_state = BoardState('I')
command = input()

# If the final 9th line says Moves, count the number of legal moves for
# both players
if command == 'Moves':
    print(count_pos_moves(initial_state, 'W'))
    print(count_pos_moves(initial_state, 'B'))

# test_move = Move(initial_state, 3, 3, 3, 4)
# print(Move.check_right(initial_state, 3, 3))
