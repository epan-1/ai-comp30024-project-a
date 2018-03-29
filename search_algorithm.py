###
# This Python module contains implementations of different search algorithms
# used to implement the Massacre functionality of the program
###

import sys
from search_tree import *


def rec_depth_limited(problem, limit=50):
    """
    NOTE: Function taken from library of classes provided by AIMA textbook
    :param problem:
    :param limit:
    :return:
    """

    def recursive_dls(node, problem, limit):
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
    """
    NOTE: Function taken from library of classes provided by AIMA textbook
    :param problem:
    :return:
    """
    for depth in range(sys.maxsize):
        result = rec_depth_limited(problem, depth)
        if result != 'cutoff':
            return result


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
        print(node)
        if problem.goal_test(node.board_state):
            return node
        else:
            for child in node.expand(problem):
                if child not in visited:
                    return recursive_dfs(child, problem)

    return recursive_dfs(Node(problem.initial_board), problem)