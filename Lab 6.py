# Jaime O. Salas
# Data Structures & Algorithms
# TA:  Anindita Nath and Maliheh Zargaran
# Instructor: Olac Fuentes
# Last modification: 4/12/19
# Purpose of Program: Is to build a maze using the Disjoint Set forests in order to compare the running times
# of both union by size and regular unions

import matplotlib.pyplot as plt
import numpy as np
import random
import time


def DisjointSetForest(size):
    return np.zeros ( size, dtype=np.int ) - 1


# Returns a list containing the sets encoded in S
def dsfToSetList(S):
    sets = [[] for i in range ( len ( S ) )]
    for i in range ( len ( S ) ):
        sets[find ( S, i )].append ( i )
    sets = [x for x in sets if x != []]
    return sets

# Gets the total number of sets
def Total_Sets(S):
    Set_Num = 0
    for i in range(len(S)):
        if S[i] < 0: Set_Num += 1
    return Set_Num


# Returns root of tree that i belongs to
def find(S, i):
    if S[i] < 0:
        return i
    return find ( S, S[i] )


# Find with path compression
def find_c(S, i):
    if S[i] < 0:
        return i
    r = find_c ( S, S[i] )
    S[i] = r
    return r


# Joins i's tree and j's tree, if they are different
def union(S, i, j):
    ri = find ( S, i )
    rj = find ( S, j )
    if ri != rj:
        S[rj] = ri


# Joins i's tree and j's tree, if they are different
# Uses path compression
def union_c(S, i, j):
    ri = find_c ( S, i )
    rj = find_c ( S, j )
    if ri != rj:
        S[rj] = ri


# if i is a root, S[i] = -number of elements in tree (set)
# Makes root of smaller tree point to root of larger tree
# Uses path compression
def union_by_size(S, i, j):
    ri = find_c ( S, i )
    rj = find_c ( S, j )
    if ri != rj:
        if S[ri] > S[rj]:  # j's tree is larger
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri


################################################
def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w = []
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c != maze_cols-1:
                w.append([cell, cell+1])
            if r != maze_rows-1:
                w.append([cell, cell+maze_cols])
    return w

# draw_maze(walls, maze_rows, maze_cols, cell_nums=False)
'''
for i in range(len(walls)//2):  # Remove 1/2 of the walls
    d = random.randint(0, len(walls)-1)
    print('removing wall ', walls[d])
    walls.pop(d)'''


def draw_maze(walls, maze_rows, maze_cols, cell_nums=False):
    fig, ax = plt.subplots()  # Plots the maze
    for w in walls:
        if w[1]-w[0] == 1:  # vertical wall
            x0 = (w[1] % maze_cols)
            x1 = x0
            y0 = (w[1] // maze_cols)
            y1 = y0 + 1

        else:  # horizontal wall
            x0 = (w[0] % maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0
        ax.plot([x0, x1], [y0, y1], linewidth=1, color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0, 0, sx, sx, 0], [0, sy, sy, 0, 0], linewidth=2, color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols
                ax.text((c+.5), (r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off')
    ax.set_aspect(1.0)


# The total number of rows and cols will
# Be determined by the number below
maze_rows = 10
maze_cols = 15

S = DisjointSetForest(maze_rows * maze_cols)
Num_Of_Sets = Total_Sets(S)
walls = wall_list(maze_rows,maze_cols)



def union_maze():
    draw_maze(walls,maze_rows,maze_cols,cell_nums=True)
    while Total_Sets(S) > 1:
        remove_w = random.randint(0,len(walls)-1)
        if find(S,(walls[remove_w])[0]) != find(S, (walls[remove_w])[1]):
            union(S,(walls[remove_w])[0], (walls[remove_w])[1])
            walls.pop(remove_w)

def compression_maze():
    draw_maze(walls,maze_rows,maze_cols,cell_nums=True)
    while Total_Sets(S) > 1:
        remove_w = random.randint(0,len(walls)-1)
        if find_c(S,(walls[remove_w])[0]) != find_c(S, (walls[remove_w])[1]):
            union_by_size(S, (walls[remove_w])[0], (walls[remove_w])[1])
            walls.pop(remove_w)






print("Your choices are displayed below")
print("Option 1. Maze with standard union")
print("Option 2. Maze with compression")
print()

User_input = int(input("Please choose an option from above: "))
sets = dsfToSetList(S)

if User_input == 1:
    union_time = time.time()
    union_maze()
    draw_maze(walls, maze_rows, maze_cols)
    union_time_stop = time.time()
    print("The time for the maze using standard union is: ", union_time_stop - union_time)


if User_input == 2:
    compression_time = time.time()
    compression_maze()
    draw_maze(walls, maze_rows, maze_cols)
    compression_stop = time.time()
    print("The time for the maze using compression is: ", compression_stop - compression_time)



