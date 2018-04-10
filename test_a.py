###
# This file will run the code to test different sections of Part A
###

from move import *
from board_state import *
from search_tree import *
from search_algorithm import *

test_board = [['-' for j in range(8)] for i in range(8)]
test_board[0][0] = 'X'
test_board[7][7] = 'X'
test_board[7][0] = 'X'
test_board[0][7] = 'X'
test_board[0][4] = 'O'
test_board[2][6] = 'O'
test_board[3][4] = '@'
test_board[5][4] = '@'

# initial_state = BoardState(temp=test_board)
output_state = BoardState('I')
command = input()

parent = Node(output_state)
problem = MassacreProblem(output_state)
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
# output_state.move_piece(move)
# move = Move(output_state, 1, 2, 1, 3)
# output_state.move_piece(move)
# print(initial_state)
# print(output_state)

# print(check_suicide(output_state, 1, 3))
# output_state.eliminate_piece()
#
# for tile in match_white_and_goal_tile(output_state):
#     print(tile)

# for tile in match_white_and_black(output_state):
#     print(tile)
#
# poss = sorted_generate_moves(output_state)
# for move in poss:
#     print(move)


# goal_tiles = find_goal_tiles(output_state)
# print(goal_tiles)
# for spot in goal_tiles:
#     output_state.board[spot[0]][spot[1]] = 'G'
#
# print(output_state)

    # result = breadth_first(problem)
    # result = depth_first(problem)
    # result = rec_depth_first(problem, visited)
    # result = depth_limited_search(problem, 4)
    # result = rec_depth_limited(problem, 5)
    # print(result)
    # print(len(result.solution()))


def execute_move_sequence(input_state, move_list):
    """
    This function simply executes a given move sequence to check if it actually
    does kill all the pieces
    :param input_state:
    :param move_list:
    :return: None
    """
    print(input_state)

    for move in move_list:
        print(move)
        input_state.move_piece(move)
        input_state.eliminate_piece()
        print(input_state)

    return None

result = iterative_deepening_search(problem)
execute_move_sequence(output_state, result.solution())
