###
# Module containing data structures and appropriate support functions that are
# used by the Project to implement an AI that can play the
# "Watch your back!" board game.
# Structures implemented by Edmond Pan (841389)
###


class NoBoardReadError(Exception):
    """
    Basic exception class to create an error whenever a board state is
    created without being read from input or copying from an existing state
    """
    pass


class BoardState:

    # Class variables to store the current number of rows and cols this
    # board state has
    NUM_COLS = 8
    NUM_ROWS = 8

    def __init__(self, ins_type = 'E', other_state = None):
        """
        Constructor to initialise and fill in the current board state
        :param ins_type: Character determining which method to use to insert the
                         position of pieces into the board structure. If the
                         character is 'I' then insert from stdin otherwise
                         insertion is done by reading from an existing
                         BoardState object and then doing the appropriate
                         movement of the piece. Default insertion is specified
                         by 'E'
        :param other_state: Another BoardState object to copy the board from
        """

        # Coordinate access is of the format self.board[col][row]. Initialise
        # all values to empty spaces denoted by "-"
        self.board = [['-' for j in range(self.NUM_ROWS)]
                      for i in range(self.NUM_COLS)]

        # If ins_type is 'I' then read from input
        if ins_type == 'I':
            self.__read_input__()
        elif isinstance(other_state, BoardState):
            # Takes an board_state object and copies its contents into the
            # board structure
            for i in range(len(other_state.board)):
                for j in range(len(other_state.board[i])):
                    self.board[j][i] = other_state.output_piece(j, i)
        else:
            raise NoBoardReadError('Data is not in correct format. Please'
                                   ' check the inputs')
        # Make sure any pieces that should be eliminated are eliminated
        self.eliminate_piece()

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

    def output_piece(self, j, i):
        """
        This function outputs the character given the coordinates
        :param j: Coordinates
        :param i: Coordinates
        :return: A char representing the piece of the board
            at the coordinates
        """
        return self.board[j][i]

    def move_piece(self, move):
        """
        This function acts out the move on the board state
        :param move: Move object describing moving a piece
        :return: None
        """

        # Read the characters from move
        curr_char = self.board[move.curr_col][move.curr_row]
        new_char = self.board[move.new_col][move.new_row]

        # Swap these characters
        self.board[move.curr_col][move.curr_row] = new_char
        self.board[move.new_col][move.new_row] = curr_char

        return

    def __check_horiz_elim__(self, enemy, col, row):
        """
        Function that checks for horizontal eliminations.
        :param enemy: A character corresponding to the enemy's piece on
                       the board. i.e. 'O' for white and '@' for black
        :param col: Column number of piece to check
        :param row: Row number of piece to check
        :return: None
        """
        # Only check left and right if the piece is not at the very edge
        # of the board
        if col != 0 and col != self.NUM_COLS - 1:
            # Check if both right and left sides are blocked by a corner or
            # a black piece
            if self.board[col + 1][row] == enemy and \
                            self.board[col - 1][row] == enemy:
                # Then the white piece gets destroyed
                self.board[col][row] = '-'
            elif self.board[col + 1][row] == enemy and \
                    self.board[col - 1][row] == 'X':
                self.board[col][row] = '-'
            elif self.board[col + 1][row] == 'X' and \
                    self.board[col - 1][row] == enemy:
                self.board[col][row] = '-'

    def __check_vert_elim__(self, enemy, col, row):
        """
        Function that checks for vertical eliminations.
        :param enemy: A character corresponding to the enemy's piece on
                       the board. i.e. 'O' for white and '@' for black
        :param col: Column number of piece to check
        :param row: Row number of piece to check
        :return: None
        """
        # Only check up and down if the piece is not at the very edge
        # of the board
        if row != 0 and row != self.NUM_ROWS - 1:
            # Check if both up and down sides are blocked by a corner or a
            # black piece
            if self.board[col][row + 1] == enemy and \
               self.board[col][row - 1] == enemy:
                # Then the white piece gets destroyed
                self.board[col][row] = '-'
            elif self.board[col][row + 1] == enemy and \
                    self.board[col][row - 1] == 'X':
                self.board[col][row] = '-'
            elif self.board[col][row + 1] == 'X' and \
                    self.board[col][row - 1] == enemy:
                self.board[col][row] = '-'

    def eliminate_piece(self):
        """
        This function checks if a board state eliminates any pieces and
        removes eliminated pieces appropriately
        :return: None
        """
        # For all white pieces, then black pieces
        whites = self.search_board('W')
        blacks = self.search_board('B')

        # For white pieces
        while len(whites) != 0:
            white_coord = whites.pop()
            col = white_coord[0]
            row  = white_coord[1]

            # Remove whites pieces that can be eliminated
            self.__check_horiz_elim__('@', col, row)
            self.__check_vert_elim__('@', col, row)

        # For black pieces
        while len(blacks) != 0:
            black_coord = blacks.pop()
            col = black_coord[0]
            row = black_coord[1]

            # Remove whites pieces that can be eliminated
            self.__check_horiz_elim__('O', col, row)
            self.__check_vert_elim__('O', col, row)

        return
