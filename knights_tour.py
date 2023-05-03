# Final Project for SWDV 610: Data Structures and Algorithms
# Maryville University
# Benjamin Wilkins

# Knight's tour

from time import time
from sys import setrecursionlimit
from graph import Graph

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
    
    def _tour_done(self, path):
        return len(path) == self._num_spaces
    
    def _less_moves_heur(self, vert, visited):
        # Warnsdorff’s algorithm

        result = []
        for neighbor in self._board.neighbors(vert):
            if neighbor not in visited:
                
                connects = 0
                for other in self._board.neighbors(neighbor):
                    if other not in visited:
                        connects += 1

                result.append((neighbor, connects))
        
        result.sort(key=self._sort_helper)
        return [ i[0] for i in result ]

    def _sort_helper(self, tup):
        return tup[1]

    def _tour(self, current, path, visited):
        visited.add(current)
        path.append(current)

        if not self._tour_done(path):
            neighbors = self._less_moves_heur(current, visited)
            i = 0

            while i < len(neighbors) and not self._tour_done(path):
                vert = neighbors[i]
                if vert not in visited:
                    self._tour(vert, path, visited)
                
                i += 1

            if not self._tour_done(path):
                path.pop()
                visited.remove(current) 
        
        return path
    
    def tour(self, start):
        return self._tour(start, [], set())
    
    def print_tour(self, path):
        result_board = []
        for i in range(self._dimensions[0]):
            row = [None for j in range(self._dimensions[1])]
            result_board.append(row)

        count = 1
        for vert in path:
            ele = vert.element()
            result_board[ele[0]-1][ele[1]-1] = count
            count += 1

        for i in range(len(result_board)-1, -1, -1):
            print(result_board[i])

    def execute(self, coords):
        start = self.get_position(coords)
        
        s = time()
        tour_path = self.tour(start)
        e = time()

        print()
        self.print_tour(tour_path)
        print('\ncompleted in', e-s, 'seconds')
        return tour_path
    
    def test(self, path):
        for i in range(len(path)-1):
            if not self.valid_move(path[i].element(), path[i+1].element()):
                print('Invalid move!')
    
        for vert in path:
            if path.count(vert) > 1:
                print('More than 1!')

        if len(path) != self._num_spaces:
            print('Invalid length of', f'{len(path)}!', 'Expected:', self._num_spaces)
    
if __name__ == '__main__':
    setrecursionlimit(10000)
   
    test = KnightsTour()
    path = test.execute((1,1))
    test.test(path)

    test2 = KnightsTour((16,16))
    path2 = test2.execute((1,1))
    test2.test(path2)
    
    test3 = KnightsTour((32,32))
    path3 = test3.execute((1,1))
    test3.test(path3)
