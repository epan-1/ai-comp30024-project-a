###
# File that is used to test different aspects of the Part B implementation of
# the AI project
###

from move import *
from board_state import *

board = BoardState()
board.modify(Move(board, action=(6, 5), enemy='@'), 'O')
print(board)
action = (6, 5), (6, 6)
a = Move(board_state=board, action=action, enemy='@')
board.modify(a)
print(board)