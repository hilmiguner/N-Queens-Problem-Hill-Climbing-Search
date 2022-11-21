from state import Board

def algorithm(boardObject: Board):
    current = boardObject
    while True:
        neighbour = current.neighbour()
        print("current", current.totalConflict)
        print("neighbour", neighbour.totalConflict)
        if neighbour.totalConflict >= current.totalConflict:
            return current
        current = neighbour