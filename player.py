###
# This is the Player class that serves to decide and return which moves to do
# to perform to the referee program. This file will be the one that is marked
# for Part B of the project.
###

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
        else:
            self.enemy = 'O'
