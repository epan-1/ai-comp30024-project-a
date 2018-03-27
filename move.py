###
# Python module that contains classes and functions that represent the moves
# in the board game "Watch your back!".
###


# A simple little custom exception to raise whenever an invalid move is passed
class InvalidMoveError(Exception):
    pass


class Move:
    """
    This class represents a valid move in the game "Watch your Back!"
    """
    def __init__(self, board_state, col, row, new_col, new_row):
        """
        A move object contains the coordinates of the piece to be moved as well
        as the coordinates of the new location that the piece will be moved to
        :param col: The column number this move refers to
        :param row: The row number this move refers to
        """
        # Check if the move is valid before creating the object
        if self.is_valid(board_state, col, row, new_col, new_row):
            self.curr_col = col
            self.curr_row = row
            self.new_col = new_col
            self.new_row = new_row
        else:
            raise InvalidMoveError("Invalid Move detected...")

    def __eq__(self, other):
        """
        Function to test if the current move is equal to another one
        :param other: The other object to check against
        :return: True if they are the same and False otherwise
        """
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            # Compare if all values are the same
            if self.curr_col == other.col and \
               self.curr_row == other.row and \
               self.new_col == other.new_col and \
               self.new_row == other.new_row:
                return True
            else:
                # Otherwise they must be a different move
                return False

    def __str__(self):
        """
        To string function that prints out what the move is
        :return: None
        """
        line = "({}, {}) -> ({}, {})\n".format(self.curr_col, self.curr_row,
                                               self.new_col, self.new_row)
        return line

    @classmethod
    def is_valid(cls, board_state, col, row, new_col, new_row):
        """
        This function checks if the current move being created is valid
        :param board_state:
        :return:
        """
        # Check if the current coords refer to an actual piece
        if board_state.board[col][row] != 'O' and \
           board_state.board[col][row] != '@':
            return False
        else:
            # Check if the new coords are valid
            if cls.__check_up__(board_state, col, row, new_col, new_row):
                return True
            elif cls.__check_down__(board_state, col, row, new_col, new_row):
                return True
            elif cls.__check_left__(board_state, col, row, new_col, new_row):
                return True
            elif cls.__check_right__(board_state, col, row, new_col, new_row):
                return True
            else:
                return False

    @classmethod
    def __check_up__(cls, board_state, col, row, new_col, new_row):
        """
        Function checks if the current move is allowed to move up one space
        or can legally jump
        :param board_state:
        :return:
        """
        # Ensure that it's not at the very top of the board, and there is at
        # least 1 space to allow it to move upwards
        if row != 0 and board_state.board[col][row - 1] == '-':
            # If the jump coords match the new specified move coords, then
            # it is valid
            if col == new_col and row-1 == new_row:
                return True
            else:
                return False
        # Check that if there is a space and it is occupied by a black or white
        # piece that there is space to allow the current piece to jump
        elif row != 0 and (
                    board_state.board[col][row - 1] == 'O' or
                    board_state.board[col][row - 1] == '@'):
            if row != 1 and board_state.board[col][row - 2] == '-':
                # If the jump coords match the new specified move coords, then
                # it is valid
                if col == new_col and row-2 == new_row:
                    return True
                else:
                    return False
        else:
            # Otherwise the piece is not allowed to move upwards
            return False

    @classmethod
    def __check_down__(cls, board_state, col, row, new_col, new_row):
        """
        Function checks if the current move is allowed to move down one space
        or can legally jump
        :param board_state:
        :return:
        """
        # Ensure that it's not at the very bottom of the board, and there is at
        # least 1 space to allow it to move downwards
        if row != board_state.NUM_ROWS-1 and \
                board_state.board[col][row + 1] == '-':
            # If the jump coords match the new specified move coords, then
            # it is valid
            if col == new_col and row+1 == new_row:
                return True
            else:
                return False
        # Check that if there is a space and it is occupied by a black or white
        # piece that there is space to allow the current piece to jump
        elif row != board_state.NUM_ROWS and (
                        board_state.board[col][row + 1] == 'O' or
                        board_state.board[col][row + 1] == '@'):
            if row != 1 and board_state.board[col][row + 2] == '-':
                # If the jump coords match the new specified move coords, then
                # it is valid
                if col == new_col and row+2 == new_row:
                    return True
                else:
                    return False
        else:
            # Otherwise the piece is not allowed to move downwards
            return False

    @classmethod
    def __check_left__(cls, board_state, col, row, new_col, new_row):
        """
        Function checks if the current move is allowed to move left one space
        or can legally jump
        :param board_state:
        :return:
        """
        # Ensure that it's not at the very left of the board, and there is at
        # least 1 space to allow it to move left
        if col != 0 and board_state.board[col - 1][row] == '-':
            if col-1 == new_col and row == new_row:
                return True
            else:
                return False
        # Check that if there is a space and it is occupied by a black or white
        # piece that there is space to allow the current piece to jump
        elif row != board_state.NUM_ROWS and (
                        board_state.board[col - 1][row] == 'O' or
                        board_state.board[col - 1][row] == '@'):
            if row != 1 and board_state.board[col - 2][row] == '-':
                if col-2 == new_col and row == new_row:
                    return True
                else:
                    return False
        else:
            # Otherwise the piece is not allowed to move leftwards
            return False

    @classmethod
    def __check_right__(cls, board_state, col, row, new_col, new_row):
        """
        Function checks if the current move is allowed to move right one space
        or can legally jump
        :param board_state:
        :return:
        """
        # Ensure that it's not at the very right of the board, and there is at
        # least 1 space to allow it to move right
        if col != board_state.NUM_COLS and \
                board_state.board[col - 1][row] == '-':
            if col + 1 == new_col and row == new_row:
                return True
            else:
                return False
        # Check that if there is a space and it is occupied by a black or white
        # piece that there is space to allow the current piece to jump
        elif row != board_state.NUM_ROWS and (
                        board_state.board[col + 1][row] == 'O' or
                        board_state.board[col + 1][row] == '@'):
            if row != 1 and board_state.board[col + 2][row] == '-':
                if col + 2 == new_col and row == new_row:
                    return True
                else:
                    return False
        else:
            # Otherwise the piece is not allowed to move rightwards
            return False
