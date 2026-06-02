import numpy as np

# 3x3 matrix of zeros to represent a tic tac toe board
board = np.zeros((3, 3), dtype=str)
board[0,2] = "X"

print(board)