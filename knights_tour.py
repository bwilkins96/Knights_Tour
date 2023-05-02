# Final Project for SWDV 610: Data Structures and Algorithms
# Maryville University
# Benjamin Wilkins

# Knight's tour

from graph import Graph
from stack import Stack
from time import time

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
        visited = {}
        path = []
        
        stack = Stack()
        stack.push((start, None))

        new = 0
        while (stack.size() > 0) and (len(path) < self._num_spaces):
            current, current_edge = stack.pop()
            if current in visited: print('hello :)')
            visited[current] = current_edge
            path.append(current)

            for edge in self._board.incident_edges(current):
                other = edge.opposite(current)

                if other not in visited:
                    stack.push((other, edge))
                    new += 1

            if new == 0:
                if len(path) < self._num_spaces:
                    path = self._backtrack(visited, path, stack)
            else:
                new = 0       

        return path
    
    def _backtrack(self, visited, path, stack):
        #print('\nbacktracking!\n')

        next, next_edge = stack.top()
        parent = next_edge.opposite(next)
        parent_idx = path.index(parent)

        undo_path = path[parent_idx+1:]
        for vert in undo_path:
            del visited[vert]

        new_path = path[:parent_idx+1]
        return new_path
    
    def _tour_done(self, path):
        return len(path) == self._num_spaces
    
    def _heuristic(self, vert, visited):
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

    def tour_alt(self, current, path=[], visited=set()):
        visited.add(current)
        path.append(current)

        if len(path) < self._num_spaces:
            neighbors = self._heuristic(current, visited)
            i = 0

            while i < len(neighbors) and not self._tour_done(path):
                vert = neighbors[i]
                if vert not in visited:
                    done = self.tour_alt(vert, path, visited)
                
                i += 1

            if not self._tour_done(path):
                path.pop()
                visited.remove(current) 
        
        return path
    
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

        for row in result_board:
            print(row)
    
if __name__ == '__main__':
    test = KnightsTour()
    start = test.get_position((1,1))
    #tour = tour.tour(start)
    #print(tour)
    #print(len(tour))

    # s = time()
    tour = test.tour_alt(start)
    test.print_tour(tour)
    # e = time()

    # print('Finished in', e-s, 'seconds')
    # print('\n', tour)
    # print(len(tour), '\n')

    # for vert in tour:
    #     if tour.count(vert) > 1:
    #         print('Count greater than 1!')

    # for i in range(len(tour)-1):
    #     if not test.valid_move(tour[i].element(), tour[i+1].element()):
    #         print('invalid move!')
