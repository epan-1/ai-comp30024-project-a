###
# Python module that contains classes and functions that represent the moves
# in the board game "Watch your back!".
###


class Move:
    """
    This class represents a valid move in the game "Watch your Back!"
    """
    def __init__(self, col, row, new_col, new_row):
        """
        A move object contains the coordinates of the piece to be moved as well
        as the coordinates of the new location that the piece will be moved to
        :param col: The column number this move refers to
        :param row: The row number this move refers to
        """
        self.curr_col = col
        self.curr_row = row
        self.new_col = new_col
        self.new_row = new_row

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
