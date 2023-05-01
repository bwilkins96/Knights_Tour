# Final Project for SWDV 610: Data Structures and Algorithms
# Maryville University
# Benjamin Wilkins

# Knight's tour

from graph import Graph
from stack import Stack

class KnightsTour:
    def __init__(self, dimensions=(8,8)):
        self._dimensions = dimensions
        self._num_spaces = dimensions[0] * dimensions[1]
        self._board = self._setup_board()

    def get_position(self, tup):
        return self._board.get_vertex(tup)

    def get_change(self, start, end):
        row_change = abs(start[0] - end[0])
        col_change = abs(start[1] - end[1])
        return (row_change, col_change)

    def valid_move(self, start, end):
        change = self.get_change(start, end)
        return change == (1, 2) or change == (2, 1)

    def _setup_board(self):
        board = Graph()

        # Setup vertices for chess board in the form of (row, column) 
        for i in range(1, self._dimensions[0]+1):
            for j in range(1, self._dimensions[1]+1):
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
        visited = {start: None}
        path = []
        
        stack = Stack()
        stack.push(start)

        new = 0
        while stack.size() > 0:
            current = stack.pop()
            path.append(current)
            print(len(path))
            #print()

            for edge in self._board.incident_edges(current):
                other = edge.opposite(current)

                if other not in visited:
                    visited[other] = edge
                    stack.push(other)
                    new += 1

            if new == 0:
                if len(path) < self._num_spaces:
                    path = self._backtrack(visited, path, stack)
            else:
                new = 0

        return path
    
    def _backtrack(self, visited, path, stack):
        print('\nbacktracking!\n')

        next = stack.top()
        parent = visited[next].opposite(next)
        parent_idx = path.index(parent)

        undo_path = path[parent_idx+1:]
        for vert in undo_path:
            del visited[vert]

        new_path = path[:parent_idx+1]
        return new_path

    
if __name__ == '__main__':
    tour = KnightsTour()
    start = tour.get_position((1,1))
    tour = tour.tour(start)
    print(tour)
    print(len(tour))
