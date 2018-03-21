# Massacre

# This is a linked list (for storing board states for DFS
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
    if j != 0 and coordinates[i][j + 1] == 'O' or 'X':
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


# This does not store data
# ------------------------


def swap(coordinates, iO, jO, i_, j_):
    coordinates[iO][jO] = '-'
    coordinates[i_][j_] = 'O'
    return


def move_up(coordinates, i, j):
    if i != 0 and coordinates[i - 1][j] == '-':
        swap(coordinates, i, j, i - 1, j)
    elif i != 0 and (coordinates[i - 1][j] == 'O' or coordinates[i - 1][j] == '@'):
        if i != 1 and coordinates[i - 2][j] == '-':
            swap(coordinates, i, j, i - 2, j)
    return


def move_down(coordinates, i, j):
    if i != 7 and coordinates[i + 1][j] == '-':
        swap(coordinates, i, j, i + 1, j)
    elif i != 7 and (coordinates[i + 1][j] == 'O' or coordinates[i + 1][j] == '@'):
        if i != 6 and coordinates[i + 2][j] == '-':
            swap(coordinates, i, j, i + 2, j)
    return


def move_left(coordinates, i, j):
    if j != 0 and coordinates[i][j - 1] == '-':
        swap(coordinates, i, j, i, j - 1)
    elif j != 0 and (coordinates[i][j - 1] == 'O' or coordinates[i][j - 1] == '@'):
        if j != 1 and coordinates[i][j - 2] == '-':
            swap(coordinates, i, j, i, j - 2)
    return


def move_right(coordinates, i, j):
    if j != 7 and coordinates[i][j + 1] == '-':
        swap(coordinates, i, j, i, j + 1)
    elif j != 7 and (coordinates[i][j + 1] == 'O' or coordinates[i][j + 1] == '@'):
        if j != 6 and coordinates[i][j + 2] == '-':
            swap(coordinates, i, j, i, j + 2)
    return


# ------------------------


def number_of_blacks(coordinates):
    no_of_blacks = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if coordinates[i][j] == '@':
                no_of_blacks += 1
    return no_of_blacks


def find_position_of_whites(coordinates):
    white_pos = [[0 for x in range(12)] for y in range(2)]
    white_number = 0;
    for i in range(0, 8):
        for j in range(0, 8):
            if coordinates[i][j] == 'O':
                white_pos[white_number][0] = i
                white_pos[white_number][1] = j
                white_number += 1
    return white_pos


def find_position_of_blacks(coordinates):
    black_pos = [[0 for x in range(12)] for y in range(2)]
    black_number = 0;
    for i in range(0, 8):
        for j in range(0, 8):
            if coordinates[i][j] == 'O':
                black_pos[black_number][0] = i
                black_pos[black_number][1] = j
                black_number += 1
    return black_pos



# To do
# It is easy to implement an iterative deepening search
# IDS: Start with depth = 1
# for each white piece, move through each possible move, store board structure for each?
# for each board state, "for each white piece, move through each possible move, store board structure for each?"
# Could be a queue
# Tag visited states, delete visited states if a black is killed
def massacre(coordinates):
    temp_coordinates = coordinates
    no_of_blacks = number_of_blacks(coordinates)
    temp = Node(coordinates)
    white_positions = find_position_of_whites(coordinates)
    depth = 0
    IDDFS(coordinates, white_positions)
    # I don't if this is right:
    # Check 1 white piece move
    # Loop (depth)
    #   Loop (white pieces)
    #       Loop (check direction)
    #           Loop (0 to depth)
    #               Move it
    #               Store as temp.setNext
    #   Depth++
    #   Delete all stored items

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

    -------      
    function DLS(temp_coordinates, depth, white_positions)
        if depth = 0 and node is a goal
            return node
        if depth > 0
            foreach child of node
             found ← DLS(child, depth−1)
                if found ≠ null
                 return found
        return null

    function IDDFS(temp_coordinates, white_positions)
        while(1)
            if DLS(temp_coordinates, depth, white_positions)
                return true
        return false
    -------


    '''

    # if check_killed(coordinates, i, j):
    # kill(coordinates, i, j)
    # no_of_blacks -= 1
    # if (no_of_blacks == 0): break
    # Loop something
    # For each move, check adjacent blacks, check_killed
    return