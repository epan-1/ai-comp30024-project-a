# Massacre

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
    new = [0 for x in range(2)]
    if i != 0 and coordinates[i - 1][j] == '-':
        swap(coordinates, i, j, i - 1, j)
        new[0] = i - 1
        new[1] = j
    elif i != 0 and (coordinates[i - 1][j] == 'O' or coordinates[i - 1][j] == '@'):
        if i != 1 and coordinates[i - 2][j] == '-':
            swap(coordinates, i, j, i - 2, j)
            new[0] = i - 2
            new[1] = j
    return new


def move_down(coordinates, i, j):
    new = [0 for x in range(2)]
    if i != 7 and coordinates[i + 1][j] == '-':
        swap(coordinates, i, j, i + 1, j)
        new[0] = i + 1
        new[1] = j
    elif i != 7 and (coordinates[i + 1][j] == 'O' or coordinates[i + 1][j] == '@'):
        if i != 6 and coordinates[i + 2][j] == '-':
            swap(coordinates, i, j, i + 2, j)
            new[0] = i + 2
            new[1] = j
    return new


def move_left(coordinates, i, j):
    new = [0 for x in range(2)]
    if j != 0 and coordinates[i][j - 1] == '-':
        swap(coordinates, i, j, i, j - 1)
        new[0] = i
        new[1] = j - 1
    elif j != 0 and (coordinates[i][j - 1] == 'O' or coordinates[i][j - 1] == '@'):
        if j != 1 and coordinates[i][j - 2] == '-':
            swap(coordinates, i, j, i, j - 2)
            new[0] = i
            new[1] = j - 2
    return new


def move_right(coordinates, i, j):
    new = [0 for x in range(2)]
    if j != 7 and coordinates[i][j + 1] == '-':
        swap(coordinates, i, j, i, j + 1)
        new[0] = i
        new[1] = j
    elif j != 7 and (coordinates[i][j + 1] == 'O' or coordinates[i][j + 1] == '@'):
        if j != 6 and coordinates[i][j + 2] == '-':
            swap(coordinates, i, j, i, j + 2)
            new[0] = i
            new[1] = j
    return new


# ------------------------


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
            if coordinates[i][j] == '@':
                no_of_whites += 1
    return no_of_whites

# Whites and blacks are going to decrease


def find_position_of_whites(coordinates):
    white_pos = [[0 for x in range(12)] for y in range(2)]
    white_number = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if coordinates[i][j] == 'O':
                white_pos[white_number][0] = i
                white_pos[white_number][1] = j
                white_number += 1
    return white_pos


def find_position_of_blacks(coordinates):
    black_pos = [[0 for x in range(12)] for y in range(2)]
    black_number = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if coordinates[i][j] == 'O':
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
    whites = find_position_of_whites(coordinates)
    blacks = find_position_of_blacks(coordinates)
    lowest_distance = 100
    for x in range(number_of_whites(coordinates)):
        # Do not move pieces that are adjacent to a black piece
        if distance_to_black(coordinates, whites[x][0], whites[x][1], blacks) > 1:
            if distance_to_black(coordinates, whites[x][0], whites[x][1], blacks) < lowest_distance:
                lowest_distance = distance_to_black(coordinates, whites[x][0], whites[x][1])
                lowest_distance_white = whites[x]
    return lowest_distance_white


'''
function DLS(temp_coordinates, depth, white_positions)
        if depth = 0 and node is a goal
            return node
        if depth > 0
            foreach child of node
             found ← DLS(child, depth−1)
                if found ≠ null
                 return found
        return null

    def IDDFS(temp_coordinates, white_positions)
        while(1)
            if DLS(temp_coordinates, depth, white_positions)
                return true
        return false
'''
'''
def DLS(temp_coordinates, depth, white_positions):
    if depth = 0 and node is a goal:
        return node
    if depth > 0:
        foreach child of node
            found ← DLS(child, depth−1)
                if found ≠ null
                    return found
    return None
'''

# Can add check history here
# Iterate over all stored coordinates, check if current temp_coordinates == storedcoordinates[x]
def check_closer(temp_coordinates, i, j, blacks):
    current_coordinates = temp_coordinates
    checker = distance_to_black(temp_coordinates, i, j, blacks)
    new_coords = move_up(temp_coordinates, i, j)
    if distance_to_black(temp_coordinates, new_coords[0], new_coords[1], blacks) < checker:
        return temp_coordinates
    temp_coordinates = current_coordinates
    new_coords = move_down(temp_coordinates, i, j)
    if distance_to_black(temp_coordinates, new_coords[0], new_coords[1], blacks) < checker:
        return temp_coordinates
    temp_coordinates = current_coordinates
    new_coords = move_left(temp_coordinates, i, j)
    if distance_to_black(temp_coordinates, new_coords[0], new_coords[1], blacks) < checker:
        return temp_coordinates
    temp_coordinates = current_coordinates
    new_coords = move_right(temp_coordinates, i, j)
    if distance_to_black(temp_coordinates, new_coords[0], new_coords[1], blacks) < checker:
        return temp_coordinates

# Depth limited search 


def dls(temp_coordinates, depth, white_positions):
    node_coordinates = temp_coordinates
    current_mrw = find_most_relevant_white(temp_coordinates)
    blacks = find_position_of_blacks(temp_coordinates)
    # Initialise stored coordinates as 0
    # Start with stack of all possible current moves
    # Check if moves decrease distance to blacks

    for d in range(depth):
        # Check each direction, if movement decreases distance from a black, move it
        # Remember to store the temp coordinates
        temp_coordinates = check_closer(temp_coordinates, current_mrw[0], current_mrw[1], blacks)
        # Store temp_coordinates as visited
        # Add all possible movements to stack


    # for x in range(number_of_blacks(temp_coordinates)):

# Let's try recursive


def dlf_rec(temp_coordinates, depth, white_positions):
    if number_of_blacks(temp_coordinates) == 0:
        return  # Something
    if depth > 0:
        return  # I'm done till here

# root (0)
# While stack is not empty
    # Look at all valid children ('good' move, not duplicate) (1)
    # Add child to stack
    # Visit stack
    # Depth tag?
    # How?


def iddfs(coordinates, white_positions):
    depth = 1
    while 1:
        if dls(coordinates, depth, white_positions):
            return 1  # Print solution here
        else:
            depth += 1


# To do
# It is easy to implement an iterative deepening search
# IDS: Start with depth = 1
# for each white piece, move through each possible move, store board structure for each?
# for each board state, "for each white piece, move through each possible move, store board structure for each?"
# Could be a queue
# Tag visited states, delete visited states if a black is killed
def massacre(coordinates):
    initial_state = coordinates
    temp_coordinates = coordinates
    no_of_blacks = number_of_blacks(coordinates)
    temp = Node(coordinates)
    white_positions = find_position_of_whites(coordinates)
    iddfs(coordinates, white_positions)
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
