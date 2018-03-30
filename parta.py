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
from search_tree import *
from search_algorithm import *

# Read the initial state of the board from stdin
initial_state = BoardState('I')
command = input()

# If the final 9th line says Moves, count the number of legal moves for
# both players
if command == 'Moves':
    print(count_pos_moves(initial_state, 'W'))
    print(count_pos_moves(initial_state, 'B'))

if command == 'Massacre':
    # Create a massacre problem
    problem = MassacreProblem(initial_state)
    parent = Node(problem.initial_board)
    result = iterative_deepening_search(problem)
    for move in result.solution():
        print(move)
