from copy import deepcopy

class Board:
    def __init__(self, n: int, queensPositions):
        self.n = n
        self.queensPositions = queensPositions

        # ------BOARD INITIALIZATION------
        self.conflictBoard = {}
        # --------------------------------

        self.totalConflict = self.calculateTotalConflict()

    def calculateTotalConflict(self):
        for row in range(self.n):
            for column in range(self.n):
                self.conflictBoard[(row, column)] = 0

        for queenPosition in self.queensPositions:
            # ---------VERTICAL CHECK---------
            temp = 1
            while True:
                rowUp = queenPosition[0] + temp
                rowDown = queenPosition[0] - temp
                if rowUp >= self.n and rowDown <= -1:
                    break
                if rowUp < self.n:
                    self.conflictBoard[(rowUp, queenPosition[1])] += 1
                if rowDown > -1:
                    self.conflictBoard[(rowDown, queenPosition[1])] += 1
                temp += 1
            # --------------------------------

            # --------HORIZONTAL CHECK--------
            temp = 1
            while True:
                columnRight = queenPosition[1] + temp
                columnLeft = queenPosition[1] - temp
                if columnRight >= self.n and columnLeft <= -1:
                    break
                if columnRight < self.n:
                    self.conflictBoard[(queenPosition[0], columnRight)] += 1
                if columnLeft > -1:
                    self.conflictBoard[(queenPosition[0], columnLeft)] += 1
                temp += 1
            # --------------------------------

            # ---------DIAGONAL CHECK---------
            temp = 1
            while True:
                rowUp = queenPosition[0] + temp
                rowDown = queenPosition[0] - temp
                columnRight = queenPosition[1] + temp
                columnLeft = queenPosition[1] - temp
                if rowUp >= self.n and columnRight >= self.n and rowDown <= -1 and columnLeft <= -1:
                    break
                if rowUp < self.n and columnRight < self.n:
                    self.conflictBoard[(rowUp, columnRight)] += 1
                if rowDown > -1 and columnLeft > -1:
                    self.conflictBoard[(rowDown, columnLeft)] += 1
                temp += 1
            # --------------------------------

        totalConflict = 0
        for key in self.queensPositions:
            totalConflict += self.conflictBoard[key]

        return totalConflict

    def neighbour(self):
        tempQueensPositions = deepcopy(self.queensPositions)
        tempConflictBoard = deepcopy(self.conflictBoard)

        # ---------ORDERING---------
        tempConflictOrdered = []
        for key in tempConflictBoard:
            if len(tempConflictOrdered) == 0:
                tempConflictOrdered.append((key, tempConflictBoard[key]))
                continue
            ix = 0
            while True:
                if tempConflictBoard[key] < tempConflictOrdered[ix][1]:
                    tempConflictOrdered.insert(ix, (key, tempConflictBoard[key]))
                    break
                ix += 1
                if ix == len(tempConflictOrdered):
                    tempConflictOrdered.append((key, tempConflictBoard[key]))
                    break
        # --------------------------

        while True:
            willContinue = False
            try:
                lowestPosition, lowestConflict = tempConflictOrdered.pop(0)
            except IndexError:
                return self

            for pos in tempQueensPositions:
                if pos[1] == lowestPosition[1] and pos[0] == lowestPosition[0]:
                    willContinue = True
                    break
            if willContinue:
                continue
            break

        tempQueensPositions[lowestPosition[1]] = lowestPosition
        return Board(self.n, tempQueensPositions)
