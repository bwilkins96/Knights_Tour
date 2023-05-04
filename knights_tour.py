# Final Project for SWDV 610: Data Structures and Algorithms
# Maryville University
# Benjamin Wilkins

# Knight's tour class and solution
# --------------------------------
# A knight's tour consists of a knight making moves on a board so that
# every space on the board is visited one time

from graph import Graph

class KnightsTour:
    """Knight's tour class designed for Maryville University"""

    def __init__(self, dimensions=(8,8)):
        """
        Sets up a tour instance with a board graph based on dimensions.
        i.e. KnightsTour((5,5)) sets up an instance for tours on a 5x5 board.
        Defaults to an 8x8 board.
        """
        self._dimensions = dimensions
        self._num_spaces = dimensions[0] * dimensions[1]
        self._board = self._setup_board()

    def get_position(self, tup):
        """Returns board vertex with element tup"""
        return self._board.get_vertex(tup)

    def get_change(self, start, end):
        """Returns absolute change in position between start and end"""
        row_change = abs(start[0] - end[0])
        col_change = abs(start[1] - end[1])
        return (row_change, col_change)

    def valid_move(self, start, end):
        """Returns whether move from start to end is legal"""
        change = self.get_change(start, end)
        return change == (1, 2) or change == (2, 1)

    def _setup_board(self):
        """Sets up and returns a graph representing a board and the legal moves between spaces"""
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
        """Returns whether a tour is complete"""
        return len(path) == self._num_spaces
    
    def _less_moves_heur(self, vert, visited):
        """
        Returns the neighbors of a vert, sorted by the number of moves possible from them.
        This heuristic is an application of Warnsdorff's algorithm.
        """  
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
        """Helper function for _less_moves_heur"""
        return tup[1]

    def _tour(self, current, path, visited):
        """Recursive tour implementation using a depth-first search with backtracking"""
        visited.add(current)
        path.append(current)

        if not self._tour_done(path):
            # Get sorted neighbor vertices
            neighbors = self._less_moves_heur(current, visited)
            i = 0

            while i < len(neighbors) and not self._tour_done(path):
                vert = neighbors[i]
                if vert not in visited:
                    # Continue depth-first search with vert
                    self._tour(vert, path, visited)
                
                i += 1

            if not self._tour_done(path):
                # Start backtracking
                path.pop()
                visited.remove(current) 
        
        return path
    
    def tour(self, start):
        """Starts and returns a knight's tour, if possible"""
        return self._tour(start, [], set())
    
    def test_tour(self, path):
        """Returns whether path is a valid tour"""
        if len(path) != self._num_spaces:
            return False
        
        for i in range(len(path)-1):
            if not self.valid_move(path[i].element(), path[i+1].element()):
                return False
    
        for vert in path:
            if path.count(vert) > 1:
                return False
        
        return True
    
    def _print_row(self, row, max_len):
        """Prints a row of the board for print_tour"""
        print('|', end='')
        for num in row:
            print(f'{num: {max_len+1}}', '|', end='')
        print()

    def print_tour(self, path):
        """Prints a board with numbers representing the moves of path"""
        result_board = []
        for i in range(self._dimensions[0]):
            row = [None for j in range(self._dimensions[1])]
            result_board.append(row)

        count = 1
        for vert in path:
            ele = vert.element()
            result_board[ele[0]-1][ele[1]-1] = count
            count += 1

        header_str = "Knight's tour on {}x{} board starting from {}"
        print(header_str.format(self._dimensions[0], self._dimensions[1], path[0].element()))

        max_num_len = len(str(self._num_spaces))
        divider = '-' * ((max_num_len + 3) * self._dimensions[1] + 1)

        print(divider)  
        for i in range(len(result_board)-1, -1, -1):
           self._print_row(result_board[i], max_num_len)
           print(divider)
        
    def execute(self, coords):
        """Executes, tests, prints, and returns a tour with starting coords, if possible"""
        start = self.get_position(coords)
        tour_path = self.tour(start)

        print()
        if self.test_tour(tour_path):
            self.print_tour(tour_path)
        else:
            print(f'Tour not possible on {self._dimensions[0]}x{self._dimensions[1]} board from {coords}')
        print()

        return tour_path
    
if __name__ == '__main__':
    test = KnightsTour((5,5))
    path = test.execute((1,1))

    test2 = KnightsTour()
    path2 = test2.execute((1,1))
    path2b = test2.execute((4,5))
    
    test3 = KnightsTour((16,16))
    path3 = test3.execute((1,12))

    test4 = KnightsTour((4,4))
    path4 = test4.execute((1,1))        # Should not be possible