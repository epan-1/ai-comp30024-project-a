###
# This file will run the code to test different sections of Part A
###

from move import *
from board_state import *
from search_tree import *

initial_state = BoardState('I')
command = input()

parent = Node(initial_state)
problem = MassacreProblem(initial_state)
# tree = Stack()
# tree.push(parent)
# print(tree.size())
# new_nodes = parent.expand(problem)
# for node in new_nodes:
#     # print(node)
#     tree.push(node)
#
# print(tree.size())

# move = Move(initial_state, 1, 1, 1, 2)
# output_state = BoardState(other_state=initial_state)
# output_state.move_piece(move)
# move = Move(output_state, 1, 2, 1, 3)
# output_state.move_piece(move)
# print(initial_state)
# print(output_state)
#
# output_state.eliminate_piece()
#
# print(output_state)
