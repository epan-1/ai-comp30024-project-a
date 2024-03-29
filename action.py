###
# Python module that contains a class that represents the different
# actions in the board game "Watch your back!".
###

from move import *


class Action:
    """
    This class contains the information regarding the type of action that is to
    be played or for a player to update
    """
    def __init__(self, board_state, action, enemy):
        """
        Initialises and validates a passed in action which is simply a tuple or
        tuple of tuples.
        :param board_state: BoardState object containing information about the
                            current state of the game
        :param action: Value representing a placing action which is a single
                       tuple, a movement action which is a tuple of tuples and
                       a forfeited action which is simple the None value
        :param enemy: A character that represents the enemy piece
        """
        # Assign the values read from action
        coords = self.__convert_action__(action)
        curr_col = coords[0][0]
        curr_row = coords[0][1]
        new_col = coords[1][0]
        new_row = coords[1][1]
        self.move_type = coords[2]
        self.move = Move(board_state, enemy, curr_col, curr_row, new_col, new_row)

    def __str__(self):
        """
        Function that returns the string representation of the action
        :return:
        """
        return str(self.return_action())

    @classmethod
    def __convert_action__(cls, action):
        """
        This method converts the action into an appropriate placement or
        movement type move.
        :param action: The following are valid representations of an action
                        - A single tuple (x,y) representing a placement move
                        - A tuple of tuples ((a,b), (c,d) representing a
                            movement move
                        - The value None for forfeited turns where no move
                            can be done
        :return: A tuple of tuples with the format
                        ((col, row), (new_col, new_row), move_type)
        """
        # Check if it's a forfeited move
        if action is None:
            return (None, None), (None, None), 'forfeit'
        else:
            # Unpack the action to check whether it contains tuples or ints
            val1, val2 = action
            if isinstance(val1, tuple) and isinstance(val2, tuple):
                # This is movement move
                return val1, val2, 'move'
            elif isinstance(val1, int) and isinstance(val2, int):
                # This is a placement move
                return (val1, val2), (None, None), 'place'

            return None

    def return_action(self):
        """
        This function returns the move in the format required by the referee.py
        program
        :return: Tuples depending on whether the move was placement one or
                 movement one
        """
        # If no new column or row was specified, then it was a placement move
        if self.move_type == 'place':
            return self.move.curr_col, self.move.curr_row
        # If new column or row was specified then it must be a movement move
        elif self.move_type == 'move':
            return (self.move.curr_row, self.move.curr_row), \
                   (self.move.new_col, self.move.new_row)
        # Otherwise this is a forfeited move
        else:
            return
