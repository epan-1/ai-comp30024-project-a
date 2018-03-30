###
# This Python module contains implementations of different search algorithms
# used to implement the Massacre functionality of the program
###

import sys
from search_tree import *
from collections import deque


def rec_depth_limited(problem, limit=50):
    """
    NOTE: Function taken from library of classes provided by AIMA textbook.
    This does a recursive depth limited search
    :param problem: A Problem object containing information on how to solve the
                    problem
    :param limit: The depth limit to search for
    :return: The node containing the solution or a string detailing the cutoff
             has been reached
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
    NOTE: Function taken from library of classes provided by AIMA textbook that
    implements an iterative deepening search
    :param problem: A Problem object containing information on how to solve the
                    problem
    :return: The node that contains the solution
    """
    for depth in range(sys.maxsize):
        # Run a DLS for current limit
        result = depth_limited_search(problem, depth)
        # If it hasn't been cutoff then this must be the result node
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
    # A set to contain nodes that have already been visited
    explored = set()
    while frontier.size() != 0:
        node = frontier.pop()
        # print(node)  # For visualisation only
        if problem.goal_test(node.board_state):
            return node
        elif node.depth == limit:
            # Don't expand and get the next node from the Stack
            continue
        else:
            # Add the node to explored set
            explored.add(node.board_state)
            # Check if the child node has already been explored or if it
            # already exists as a frontier node. Prevents infinite cycling
            frontier.extend(child for child in node.expand(problem)
                            if child.board_state not in explored and
                            not frontier.exists(child))

    return 'cutoff'


def breadth_first(problem):
    """
    Function taken from AIMA's library of classes that implements a BFS
    :param problem: A Problem object describing the problem to solve
    :return: The node if it matches
    """
    node = Node(problem.initial_board)
    if problem.goal_test(node.board_state):
        return node
    # Use a double ended queue to implement FIFO ordering
    frontier = deque([node])
    explored = set()
    while frontier:
        node = frontier.popleft()
        explored.add(node.board_state)
        for child in node.expand(problem):
            # Make sure the node hasn't been visited yet
            if child.board_state not in explored and child not in frontier:
                if problem.goal_test(child.board_state):
                    return child
                frontier.append(child)
    return None


def depth_first(problem):
    """
    Function taken from AIMA's library of classes that implements a depth
    first search
    :param problem: A Problem object describing the problem to solve
    :return: The result node or None if no solution was found
    """
    frontier = Stack((Node(problem.initial_board)))
    explored = set()
    while frontier.size() != 0:
        node = frontier.pop()
        if problem.goal_test(node.board_state):
            return node
        explored.add(node.board_state)
        frontier.extend(child for child in node.expand(problem)
                        if child.board_state not in explored and
                        not frontier.exists(child))
    return None


