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
        if self.__is_valid__(board_state, col, row, new_col, new_row):
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
        line = "({}, {}) -> ({}, {})".format(self.curr_col, self.curr_row,
                                               self.new_col, self.new_row)
        return line

    @classmethod
    def __is_valid__(cls, board_state, col, row, new_col, new_row):
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
            validity = False
            out = cls.check_up(board_state, col, row)
            if out:
                if out[0] == new_col and out[1] == new_row:
                    validity = True
            out = cls.check_down(board_state, col, row)
            if out:
                if out[0] == new_col and out[1] == new_row:
                    validity = True
            out = cls.check_left(board_state, col, row)
            if out:
                if out[0] == new_col and out[1] == new_row:
                    validity = True
            out = cls.check_right(board_state, col, row)
            if out:
                if out[0] == new_col and out[1] == new_row:
                    validity = True
            # Now return the answer
        return validity

    @classmethod
    def check_up(cls, board_state, col, row):
        """
        Function checks if the current move is allowed to move up one space
        or can legally jump
        :param board_state:
        :return:
        """
        # Ensure that it's not at the very top of the board, and there is at
        # least 1 space to allow it to move upwards
        if row != 0 and board_state.board[col][row - 1] == '-':
            return col, row-1
        # Check that if there is a space and it is occupied by a black or white
        # piece that there is space to allow the current piece to jump
        elif row != 0 and (
                    board_state.board[col][row - 1] == 'O' or
                    board_state.board[col][row - 1] == '@'):
            # Make sure its not on the second row of the board otherwise
            # there would be no more board left after you jumped over the piece
            if row != 1 and board_state.board[col][row - 2] == '-':
                return col, row-2
            else:
                return False
        else:
            # Otherwise the piece is not allowed to move upwards
            return False

    @classmethod
    def check_down(cls, board_state, col, row):
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
            return col, row+1
        # Check that if there is a space and it is occupied by a black or white
        # piece that there is space to allow the current piece to jump
        elif row != board_state.NUM_ROWS-1 and (
                        board_state.board[col][row + 1] == 'O' or
                        board_state.board[col][row + 1] == '@'):
            # Make sure its not on the second last row of the board otherwise
            # there would be no more board left after you jumped over the piece
            if row != board_state.NUM_ROWS-2 and \
                      board_state.board[col][row + 2] == '-':
                return col, row+2
            else:
                return False
        else:
            # Otherwise the piece is not allowed to move downwards
            return False

    @classmethod
    def check_left(cls, board_state, col, row):
        """
        Function checks if the current move is allowed to move left one space
        or can legally jump
        :param board_state:
        :return:
        """
        # Ensure that it's not at the very left of the board, and there is at
        # least 1 space to allow it to move left
        if col != 0 and board_state.board[col - 1][row] == '-':
            return col-1, row
        # Check that if there is a space and it is occupied by a black or white
        # piece that there is space to allow the current piece to jump
        elif col != 0 and (
                        board_state.board[col - 1][row] == 'O' or
                        board_state.board[col - 1][row] == '@'):
            # Make sure its not on the second col of the board otherwise
            # there would be no more board left after you jumped left
            if col != 1 and board_state.board[col - 2][row] == '-':
                return col-2, row
            else:
                return False
        else:
            # Otherwise the piece is not allowed to move leftwards
            return False

    @classmethod
    def check_right(cls, board_state, col, row):
        """
        Function checks if the current move is allowed to move right one space
        or can legally jump
        :param board_state:
        :return:
        """
        # Ensure that it's not at the very right of the board, and there is at
        # least 1 space to allow it to move right
        if col != board_state.NUM_COLS-1 and \
                board_state.board[col + 1][row] == '-':
            return col+1, row
        # Check that if there is a space and it is occupied by a black or white
        # piece that there is space to allow the current piece to jump
        elif col != board_state.NUM_COLS-1 and (
                        board_state.board[col + 1][row] == 'O' or
                        board_state.board[col + 1][row] == '@'):
            # Make sure its not on the second last col of the board otherwise
            # there would be no more board left after you jumped right
            if col != board_state.NUM_COLS-2 and \
                      board_state.board[col + 2][row] == '-':
                return col+2, row
            else:
                return False
        else:
            # Otherwise the piece is not allowed to move rightwards
            return False


def generate_moves(board_state, player='W'):
    """
    This function generates a list of all possible Moves that the player
    can make given the current board state
    :param board_state: 
    :param player: A character to identify which player to create moves for.
                   Defaults to the white player
    :return: A list of Move objects representing all valid, possible moves
    """
    poss_moves = []
    piece_locs = board_state.search_board(player)
    # For each piece, create the valid moves.
    for coord in piece_locs:
        # Checking possible up movement
        new_loc = Move.check_up(board_state, coord[0], coord[1])
        if new_loc:
            poss_moves.append(Move(board_state, coord[0], coord[1],
                                   new_loc[0], new_loc[1]))
        # Checking possible down movement
        new_loc = Move.check_down(board_state, coord[0], coord[1])
        if new_loc:
            poss_moves.append(Move(board_state, coord[0], coord[1],
                                   new_loc[0], new_loc[1]))
        # Checking possible left movement
        new_loc = Move.check_left(board_state, coord[0], coord[1])
        if new_loc:
            poss_moves.append(Move(board_state, coord[0], coord[1],
                                   new_loc[0], new_loc[1]))
        # Checking possible right movement
        new_loc = Move.check_right(board_state, coord[0], coord[1])
        if new_loc:
            poss_moves.append(Move(board_state, coord[0], coord[1],
                                   new_loc[0], new_loc[1]))

    return poss_moves


def count_pos_moves(board_state, player='W'):
    """
    This function counts the total number of legal moves available for player
    given the current board_state. This is in the movement phase of the game
    and assumes all regular moves and jumps available including ones which
    may eliminate the player's pieces
    :param board_state: A BoardState object containing the current state of
                        the game.
    :param player: A character indicating which player's legal moves to count.
                   Defaults to the White player
    :return: Integer corresponding to the number of moves currently
    """
    piece_locs = board_state.search_board(player)
    valid_count = 0

    # For each piece, count the number of valid moves
    for coord in piece_locs:
        if Move.check_up(board_state, coord[0], coord[1]):
            valid_count += 1
        if Move.check_down(board_state, coord[0], coord[1]):
            valid_count += 1
        if Move.check_left(board_state, coord[0], coord[1]):
            valid_count += 1
        if Move.check_right(board_state, coord[0], coord[1]):
            valid_count += 1
    # Return the count
    return valid_count
