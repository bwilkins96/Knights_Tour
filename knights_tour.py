# Final Project for SWDV 610: Data Structures and Algorithms
# Maryville University
# Benjamin Wilkins

# Knight's tour

from graph import Graph

class KnightsTour:
    def __init__(self):
        self._board = self._setup_board()
        self._visited = set()

    def _setup_board(self):
        board = Graph()

        # Setup vertices for 8x8 chess board in the form of (row, column) 
        for i in range(1, 9):
            for j in range(1, 9):
                board.insert_vertex((i, j))

        return board
    
if __name__ == '__main__':
    print(KnightsTour()._board.vertices())