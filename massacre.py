# Massacre

from search_tree import *
from board_state import *

# This is a linked list (for storing board states for DFS

'''
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.first_child = None
        self.parent = None

    def get_data(self):
        return self.data

    def get_first_child(self):
        return self.first_child

    def get_next_sibling(self):
        return self.next_sibling

    def set_data(self, newdata):
        self.data = newdata

    def set_first_child(self, first_child):
        self.first_child = first_child

    def get_parent(self):
        return self.get_parent
'''


def print_move(from_x, from_y, to_x, to_y):
    print('({}, {}) -> ({}, {})'.format(from_x, from_y, to_x, to_y))


def check_up_for_white(coordinates, i, j):
    if i != 0 and coordinates[i - 1][j] == 'O' or 'X':
        return 1


def check_down_for_white(coordinates, i, j):
    if i != 7 and coordinates[i + 1][j] == 'O' or 'X':
        return 1


def check_left_for_white(coordinates, i, j):
    if j != 0 and coordinates[i][j - 1] == 'O' or 'X':
        return 1


def check_right_for_white(coordinates, i, j):
    if j != 7 and coordinates[i][j + 1] == 'O' or 'X':
        return 1


def check_killed(coordinates, i, j):
    # For this assignment, we only need to kill blacks
    if coordinates[i][j] != '@':
        return 0
    if check_up_for_white(coordinates, i, j) and check_down_for_white(coordinates, i, j):
        return 1
    if check_left_for_white(coordinates, i, j) and check_right_for_white(coordinates, i, j):
        return 1


def kill(coordinates, i, j):
    coordinates[i][j] = '-'
    return


def number_of_blacks(coordinates):
    no_of_blacks = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if coordinates[i][j] == '@':
                no_of_blacks += 1
    return no_of_blacks


def number_of_whites(coordinates):
    no_of_whites = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if coordinates[i][j] == 'O':
                no_of_whites += 1
    return no_of_whites

# Whites and blacks are going to decrease


def get_white_positions(coordinates):
    white_pos = [[0 for x in range(number_of_whites(coordinates))] for y in range(2)]
    white_number = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if coordinates[i][j] == 'O':
                white_pos[white_number][0] = i
                white_pos[white_number][1] = j
                white_number += 1
    return white_pos


def get_black_positions(coordinates):
    black_pos = [[0 for x in range(number_of_blacks(coordinates))] for y in range(2)]
    black_number = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if coordinates[i][j] == '@':
                black_pos[black_number][0] = i
                black_pos[black_number][1] = j
                black_number += 1
    return black_pos


def distance_to_black(coordinates, i, j, all_blacks):
    distance = 100
    marker = [0 for x in range(2)]
    for x in range(number_of_blacks(coordinates)):
        marker[0] = -1
        marker[1] = -1
        # Check all directions for existing whites (to set closest spot)
        if check_right_for_white(coordinates, all_blacks[x][0], all_blacks[x][1]):
            marker[0] = all_blacks[x][0]
            marker[1] = all_blacks[x][1] + 1
        if check_left_for_white(coordinates, all_blacks[x][0], all_blacks[x][1]):
            marker[0] = all_blacks[x][0]
            marker[1] = all_blacks[x][1] - 1
        if check_up_for_white(coordinates, all_blacks[x][0], all_blacks[x][1]):
            marker[0] = all_blacks[x][0] - 1
            marker[1] = all_blacks[x][1]
        if check_down_for_white(coordinates, all_blacks[x][0], all_blacks[x][1]):
            marker[0] = all_blacks[x][0] + 1
            marker[1] = all_blacks[x][1]
        # If there are no adjacent whites
        if marker[0] == -1 and marker[1] == -1:
            if abs(all_blacks[x][0] - i) + abs(all_blacks[x][1] - j) < distance:
                distance = abs(all_blacks[x][0] - i) + abs(all_blacks[x][1] - j)
        else:
            if abs(marker[0] - i) + abs(marker[1] - j) + 1 < distance:
                distance = abs(marker[0] - i) + abs(marker[1] - j) + 1
    return distance


def find_most_relevant_white(coordinates):
    whites = get_white_positions(coordinates)
    blacks = get_black_positions(coordinates)
    lowest_distance = 100
    for x in range(number_of_whites(coordinates)):
        # Do not move pieces that are adjacent to a black piece
        if distance_to_black(coordinates, whites[x][0], whites[x][1], blacks) > 1:
            if distance_to_black(coordinates, whites[x][0], whites[x][1], blacks) < lowest_distance:
                lowest_distance = distance_to_black(coordinates, whites[x][0], whites[x][1])
                lowest_distance_white = whites[x]
    return lowest_distance_white


def check_closer_up(temp_coordinates, i, j, blacks):
    current_coordinates = temp_coordinates
    checker = distance_to_black(temp_coordinates, i, j, blacks)
    new_coords = move_up(temp_coordinates, i, j)
    if distance_to_black(temp_coordinates, new_coords[0], new_coords[1], blacks) < checker:
        return temp_coordinates
    else:
        return current_coordinates

def check_closer_down(temp_coordinates, i, j, blacks):
    current_coordinates = temp_coordinates
    checker = distance_to_black(temp_coordinates, i, j, blacks)
    new_coords = move_down(temp_coordinates, i, j)
    if distance_to_black(temp_coordinates, new_coords[0], new_coords[1], blacks) < checker:
        return temp_coordinates
    else:
        return current_coordinates

def check_closer_left(temp_coordinates, i, j, blacks):
    current_coordinates = temp_coordinates
    checker = distance_to_black(temp_coordinates, i, j, blacks)
    new_coords = move_left(temp_coordinates, i, j)
    if distance_to_black(temp_coordinates, new_coords[0], new_coords[1], blacks) < checker:
        return temp_coordinates
    else:
        return current_coordinates


def check_closer_right(temp_coordinates, i, j, blacks):
    current_coordinates = temp_coordinates
    checker = distance_to_black(temp_coordinates, i, j, blacks)
    new_coords = move_right(temp_coordinates, i, j)
    if distance_to_black(temp_coordinates, new_coords[0], new_coords[1], blacks) < checker:
        return temp_coordinates
    else:
        return current_coordinates


def dls(temp_coordinates, depth):
    search_list = Stack()
    node = Node(temp_coordinates)
    search_list.push(node)
    problem = MassacreProblem(temp_coordinates)
    # While Stack is not empty
    while search_list.size() != 0:
        # Iterating 'depth' times from root node
        for x in range(depth):
            current_node = search_list.pop()
            # Check if node is at goalState
            if problem.goal_test(current_node):
                # Print moves
                return current_node.solution()
            # expand children
            children = current_node.expand()
            # Add all outputs to the Stack
            for child in children:
                search_list.push(child)
    return None
    # Return (depth will increase)

# root (0)
# While stack is not empty
    # Look at all valid children ('good' move, not duplicate) (1)
    # Add child to stack
    # Visit stack
    # Depth tag?
    # How?


def iddfs(coordinates):
    init_coordinates = coordinates
    depth = 1
    # Initiate stored coordinates linked list
    stored_coordinates = []
    while depth < 100:  #Using 100 as arbitrary upper limit for now
        if dls(coordinates, depth):
            return 1  # Print solution here
        else:
            coordinates = init_coordinates
            depth += 1
    print('Failed to find soltution after depth of 100, please refine algorithm')


def massacre(coordinates):
    iddfs(coordinates)
    '''
    depth = 0
    IDDFS(coordinates)

    (Probably store positions of white pieces)

    function DLS(node, depth)
        if depth = 0 and node is a goal
            return node
        if depth > 0
            foreach child of node
             found ← DLS(child, depth−1)
                if found ≠ null
                 return found
        return null

    function IDDFS(root)
        for depth from 0 to ∞
            found ← DLS(root, depth)
            if found ≠ null
                return found
'''