###
# File that is used to test different aspects of the Part B implementation of
# the AI project
###

from move import *
from board_state import *

board = BoardState()
board.place_piece(Move(board, action=(6, 5), enemy='@'), 'O')
print(board)
action = (6, 5), (6, 6)
a = Move(board_state=board, action=action, enemy='@')
board.move_piece(a)
print(board)