# Final Project for SWDV 610: Data Structures and Algorithms
# Maryville University
# Benjamin Wilkins

# Knight's tour

from graph import Graph
from stack import Stack

class KnightsTour:
    def __init__(self, dimensions=(8,8)):
        self._board = self._setup_board(dimensions)
        self._num_spaces = dimensions[0] * dimensions[1]

    def get_position(self, tup):
        return self._board.get_vertex(tup)

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

        # Setup edges for valid knight moves
        vertices = list(board.vertices())
        for i in range(len(vertices)):
            for j in range(i+1, len(vertices)):
                position, other = vertices[i], vertices[j]

                if self.valid_move(position.element(), other.element()):
                    board.insert_edge(position, other)

        return board
    
    def tour(self, start):
        visited = set()
        visited.add(start)
        path = []
        
        stack = Stack()
        stack.push(start)
    
        while stack.size() > 0:
            current = stack.pop()
            path.append(current)

            for edge in self._board.incident_edges(current):
                other = edge.opposite(current)

                if other not in visited:
                    visited.add(other)
                    stack.push(other)

        return path
    
if __name__ == '__main__':
    tour = KnightsTour()
    start = tour.get_position((1,1))
    tour = tour.tour(start)
    print(tour)
    print(len(tour))
