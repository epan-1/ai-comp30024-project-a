###
# File that is used to test different aspects of the Part B implementation of
# the AI project
###

from action import *
from board_state import *

board = BoardState()
board.modify(Action(board, action=(6, 5), enemy='@'), '@')
print(board)
action = (6, 5), (6, 6)
a = Action(board_state=board, action=action, enemy='@')
board.modify(a, '@')
print(board)
print(count_pos_moves(board))
