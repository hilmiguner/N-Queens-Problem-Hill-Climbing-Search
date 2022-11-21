from state import Board
from algorithm import algorithm

# queensPositions = [(3, 0), (2, 1), (1, 2), (4, 3), (3, 4), (2, 5), (1, 6), (2, 7)]
queensPositions = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]
obj = Board(8, queensPositions)

algorithm(obj)
