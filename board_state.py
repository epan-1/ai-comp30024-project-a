###
# Module containing data structures and appropriate support functions that are
# used by the Project to implement an AI that can play the
# "Watch your back!" board game.
# Structures implemented by Edmond Pan (841389)
###


class BoardState:

    # Class variables to store the current number of rows and cols this
    # board state has
    NUM_COLS = 8
    NUM_ROWS = 8

    def __init__(self, ins_type = 'E'):
        """
        Constructor to initialise and fill in the current board state
        :param ins_type: Character determining which method to use to insert the
                         position of pieces into the board structure. If the
                         character is 'I' then insert from stdin otherwise
                         insertion is done by reading from an existing
                         BoardState object and then doing the appropriate
                         movement of the piece. Default insertion is specified
                         by 'E'
        """

        # Coordinate access is of the format self.board[col][row]. Initialise
        # all values to empty spaces denoted by "-"
        self.board = [['-' for j in range(self.NUM_ROWS)]
                      for i in range(self.NUM_COLS)]

        # If ins_type is 'I' then read from input
        if ins_type == 'I':
            self.__read_input__()
        else:
            # To fill in with function that takes a 2D list and copies it into
            # the board structure
            None

    def __read_input__(self):
        """
        Function that reads an input file from the standard input into the
        board data structure.
        :return:
        """
        for i in range(self.NUM_ROWS):
            # Read in one line
            line = input()
            # Split it based on whitespace
            line = line.split()
            # For each line add it to the correct row and column in table
            j = 0
            for piece in line:
                self.board[j][i] = piece
                j += 1

    def __str__(self):
        """
        To string function that prints out what the board looks like
        :return: None
        """
        line = ''
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                # Swap coords since access is done by (col, row) not (row, col)
                # then add to the current line
                line += self.board[j][i] + ' '
            # Add newline character to end the current line and start the next
            line += '\n'
        return line

    def __eq__(self, other):
        """
        Function to test if the current board state is equal to another one
        :param other: The other object to check against
        :return: True if they are the same and False otherwise
        """
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            # Compare if the pieces on the board are in the same positions
            for i in range(len(self.board)):
                for j in range(len(self.board)):
                    if self.board[j][i] != other.board[j][i]:
                        return False
            # Otherwise they must be the same state
            return True

    def search_board(self, player='W'):
        """
        This function searches the board for the specified player's pieces.
        :param player: A character indicating which player's pieces to check.
                       Defaults to 'W' i.e. the white player
        :return: A list of tuples containing the coords (col, row) of the
                 player's pieces
        """
        output = []
        if player == 'W':
            # If white player search for 'O' characters on the board
            piece_char = 'O'
        else:
            # Must be searching for black player's pieces which are '@' chars
            piece_char = '@'

        # Looping across entire board and then adding to the output
        for i in range(self.NUM_COLS):
            for j in range(self.NUM_ROWS):
                if self.board[j][i] == piece_char:
                    output.append((j, i))

        return output
