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
import sys

# Read the initial state of the board from stdin
initial_state = BoardState('I')
command = input()

# If the final 9th line says Moves, count the number of legal moves for
# both players
if command == 'Moves':
    print(count_pos_moves(initial_state, 'W'))
    print(count_pos_moves(initial_state, 'B'))


def depth_limited_search(problem, limit=1):
    """
    This function performs a depth limited search of the tree. NOTE: Function
    adapted from library of classes provided by the AIMA textbook
    :param problem:
    :param limit:
    :return:
    """

    frontier = Stack()  # Stack
    visited = set()
    root = Node(problem.initial_board)
    frontier.push(root)
    while frontier.size() != 0:
        node = frontier.pop()
        print(node)
        if problem.goal_test(node.board_state):
            return node
        elif limit == node.depth:
            print('reached cutoff')
            return node
        else:
            visited.add(node.board_state)
            for child in node.expand(problem):
                if child not in visited and not frontier.exists(child):
                    frontier.push(child)
    return None


def rec_depth_first(problem, visited):

    def recursive_dfs(node, problem):
        visited.add(node)
        if problem.goal_test(node.board_state):
            return node
        else:
            for child in node.expand(problem):
                if child not in visited:
                    return recursive_dfs(child, problem)

    return recursive_dfs(Node(problem.initial_board), problem)


def rec_depth_limited(problem, limit=50):

    def recursive_dls(node, problem, limit):
        print(node)
        if problem.goal_test(node.board_state):
            return node
        elif limit == 0:
            return 'cutoff'
        else:
            cutoff_occurred = False
            for child in node.expand(problem):
                result = recursive_dls(child, problem, limit - 1)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
            return 'cutoff' if cutoff_occurred else None

    # Body of depth_limited_search:
    return recursive_dls(Node(problem.initial_board), problem, limit)


def iterative_deepening_search(problem):
    for depth in range(sys.maxsize):
        result = rec_depth_limited(problem, depth)
        if result != 'cutoff':
            return result

if command == 'Massacre':
    # Create a massacre problem
    problem = MassacreProblem(initial_state)
    parent = Node(problem.initial_board)
    visited = set()
    # result = rec_depth_first(problem, visited)
    # result = depth_limited_search(problem, 500)
    # result = rec_depth_limited(problem)
    result = iterative_deepening_search(problem)
    # size = stack.size()
    # for x in range(size):
    #     print(stack.pop())
    print(len(result.solution()))
    # for move in result.solution():
        # print(move)

