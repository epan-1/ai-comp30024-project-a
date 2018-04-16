###
# This is the Player class that serves to decide and return which moves to do
# to perform to the referee program. This file will be the one that is marked
# for Part B of the project.
###

from board_state import *
from move import *


class Player:
    """
    Player class that is capable of playing a complete game of 'Watch your back'
    when used in the referee.py program
    """
    def __init__(self, colour):
        # Assign the character representing enemy pieces depending on the player
        # colour
        if colour == 'white':
            self.enemy = '@'
            self.piece = 'O'
        else:
            self.enemy = 'O'
            self.piece = '@'
        # Create an empty board state to fill later
        self.board = BoardState()
        # Counter to store the current turn number
        self.turns = 0

    def action(self, turns):
        """
        Method called by referee program to request an action from the player.
        :param turns:
        :return:
        """
        return None

    def update(self, action):
        """
        Method is called by referee to update the player's internal board
        representation with the most recent move done by the opponent
        :param action:
        :return:
        """
        # Placeholder to update the board from enemy perspective
        self.board.modify(Move(self.board, action, enemy=self.piece), self.piece)
        return None
