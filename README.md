# Overview
This is a solution to the classic Knight's tour problem that I made as my final project for SWDV 610: Data Structures and Algorithms at Maryville University.

My general strategy was to produce a graph with vertices that hold the position of the board and edges representing legal knight moves between those vertices. I then use a depth-first search algorithm with backtracking to produce a tour.

# Runinng
Running knights_tour.py will produce and print information about knight's tours on boards of different dimensions.

A tour can be produced, with printed output, by producing a KnightsTour object and then calling execute on that object.

i.e. KnightsTour((n,n)).execute((c,c))

(n,n) represents a tuple with the dimensions of a board.
(c,c) represents a tuple with the coordinates of the starting position for the tour.

Coordinates represent the spaces on a board and have the format: (row, column).
Coordinates start at (1,1).

For example, board spaces can be represented in this way for an 8x8 board:

[(8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]
[(7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8)]
[(6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8)]
[(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)]
[(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)]
[(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)]
[(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8)]
[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)]