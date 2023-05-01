# Final Project for SWDV 610: Data Structures and Algorithms
# Maryville University
# Benjamin Wilkins

# Knight's tour

from graph import Graph

class KnightsTour:
    def __init__(self, dimensions=(8,8)):
        self._board = self._setup_board(dimensions)

    def get_change(self, start, end):
        row_change = abs(start[0] - end[0])
        col_change = abs(start[1] - end[1])
        return (row_change, col_change)

    def valid_move(self, start, end):
        change = self.get_change(start, end)
        return change == (1, 2) or change == (2, 1)

    def _setup_board(self, dimensions):
        board = Graph()

        # Setup vertices for chess board in the form of (row, column) 
        for i in range(1, dimensions[0]+1):
            for j in range(1, dimensions[1]+1):
                board.insert_vertex((i, j))

        return board
    
if __name__ == '__main__':
    print(KnightsTour()._board.vertices())