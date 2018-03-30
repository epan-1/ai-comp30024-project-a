###
# This Python module contains implementations of different search algorithms
# used to implement the Massacre functionality of the program
###

import sys
from search_tree import *
from collections import deque


def rec_depth_limited(problem, limit=50):
    """
    NOTE: Function taken from library of classes provided by AIMA textbook
    :param problem:
    :param limit:
    :return:
    """

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
    """
    NOTE: Function taken from library of classes provided by AIMA textbook
    :param problem:
    :return:
    """
    for depth in range(sys.maxsize):
        result = depth_limited_search(problem, depth)
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

    frontier = Stack((Node(problem.initial_board)))
    explored = set()
    while frontier.size() != 0:
        node = frontier.pop()
        print(node)
        if problem.goal_test(node.board_state):
            return node
        elif node.depth == limit:
            # Don't expand and get the next node from the Stack
            continue
        else:
            explored.add(node.board_state)
            frontier.extend(child for child in node.expand(problem)
                            if child.board_state not in explored and
                            not frontier.exists(child))

    return 'cutoff'


def breadth_first(problem):
    """
    Function taken from AIMA's library of classes
    :param problem:
    :return:
    """
    node = Node(problem.initial_board)
    if problem.goal_test(node.board_state):
        return node
    frontier = deque([node])
    explored = set()
    while frontier:
        print(node)
        node = frontier.popleft()
        explored.add(node.board_state)
        for child in node.expand(problem):
            if child.board_state not in explored and child not in frontier:
                if problem.goal_test(child.board_state):
                    return child
                frontier.append(child)
    return None


def depth_first(problem):
    """
    Function taken from AIMA's library of classes
    :param problem:
    :return:
    """
    frontier = Stack((Node(problem.initial_board)))
    explored = set()
    while frontier.size() != 0:
        node = frontier.pop()
        print(node)
        if problem.goal_test(node.board_state):
            return node
        explored.add(node.board_state)
        frontier.extend(child for child in node.expand(problem)
                        if child.board_state not in explored and
                        not frontier.exists(child))
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

