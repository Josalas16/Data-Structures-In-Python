# Jaime O. Salas
# Data Structures & Algorithms
# TA:  Anindita Nath and Maliheh Zargaran
# Instructor: Olac Fuentes
# Last modification: 4/29/19
# Purpose of Program: Draw a maze, that will randomly remove walls, tp create a path
# with 3 different algorithms and get their running times






import matplotlib.pyplot as plt
import numpy as np
import random
import queue
from scipy import interpolate
import dsf
import sys


def DisjointSetForest(size):
    return np.zeros(size, dtype=np.int) - 1




def dsfToSetList(S):
    # Returns aa list containing the sets encoded in S
    sets = [[] for i in range ( len ( S ) )]
    for i in range ( len ( S ) ):
        sets[find ( S, i )].append ( i )
    sets = [x for x in sets if x != []]
    return sets


def find(S, i):
    # Returns root of tree that i belongs to
    if S[i] < 0:
        return i
    return find(S, S[i])


def find_c(S, i):  # Find with path compression
    if S[i] < 0:
        return i
    r = find_c ( S, S[i] )
    S[i] = r
    return r


def union(S, i, j):
    # Joins i's tree and j's tree, if they are different
    ri = find ( S, i )
    rj = find ( S, j )
    if ri != rj:
        S[rj] = ri

def N_Union(S,i,j):
    if find(S,i):
        S[find(S,j)] = find(S,i)
        return True
    return False

def Union_Comp(S,i,j):
    I = find_com(S,i)
    J = find_com(S,j)
    if I != J:
        S[J] = I
        return True
    return False
def union_c(S, i, j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c ( S, i )
    rj = find_c ( S, j )
    if ri != rj:
        S[rj] = ri

def find_com(S,i,j):
    I = find_com(S,i)
    J = find_com(S,j)
    if I != J:
        S[J] = I
        return True
    return False

def union_by_size(S, i, j):
    # if i is a root, S[i] = -number of elements in tree (set)
    # Makes root of smaller tree point to root of larger tree
    # Uses path compression
    ri = find_c ( S, i )
    rj = find_c ( S, j )
    if ri != rj:
        if S[ri] > S[rj]:  # j's tree is larger
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri

def Print_Path(prev,v):
    if prev[v] != 1:
        Print_Path(prev,prev[v])
        print("-", end="")
        print(v, end='')


def ADJ_L(r,c,w):
    G = F_Al(r,c)
    for i in w:
        G[i[0]].remove(i[1])
        G[i[1]].remove(i[0])
    return G



def draw_dsf(S):
    scale = 30
    fig, ax = plt.subplots ()
    for i in range ( len ( S ) ):
        if S[i] < 0:  # i is a root
            ax.plot ( [i * scale, i * scale], [0, scale], linewidth=1, color='k' )
            ax.plot ( [i * scale - 1, i * scale, i * scale + 1], [scale - 2, scale, scale - 2], linewidth=1, color='k' )
        else:
            x = np.linspace ( i * scale, S[i] * scale )
            x0 = np.linspace ( i * scale, S[i] * scale, num=5 )
            diff = np.abs ( S[i] - i )
            if diff == 1:  # i and S[i] are neighbors; draw straight line
                y0 = [0, 0, 0, 0, 0]
            else:  # i and S[i] are not neighbors; draw arc
                y0 = [0, -6 * diff, -8 * diff, -6 * diff, 0]
            f = interpolate.interp1d ( x0, y0, kind='cubic' )
            y = f ( x )
            ax.plot ( x, y, linewidth=1, color='k' )
            ax.plot ( [x0[2] + 2 * np.sign ( i - S[i] ), x0[2], x0[2] + 2 * np.sign ( i - S[i] )],
                      [y0[2] - 1, y0[2], y0[2] + 1], linewidth=1, color='k' )
        ax.text ( i * scale, 0, str ( i ), size=20, ha="center", va="center",
                  bbox=dict ( facecolor='w', boxstyle="circle" ) )
    ax.axis ( 'off' )
    ax.set_aspect ( 1.0 )


def Num_Sets(S):
    c = 0
    for i in S:
        if i == -1: c += 1
    return c

def maze_draw(walls, maze_rows, maze_cols, G, cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1] - w[0] == 1:
            x0 = (w[1] % maze_cols)
            x1 = x0
            y0 = (w[1] // maze_cols)
            y1 = y0 + 1
        else:
            x0 = (w[0] % maze_cols)
            x1 = x0 + 1
            y0 = (w[1] // maze_cols)
            y1 = y0
        ax.plot([x0,x1], [y0,y1], linewidth=2, color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0], linewidth=2, color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r * maze_cols
                ax.text((c+.5),(r+.5),str(cell), size=10, ha='center', va='center')
    ax.axis('off')
    ax.set_aspect(1.0)





def F_Al(r,c):
    G = [[] for a in range(r*c)]
    for i in range(c):
        for j in range(c):
            cur = j + i * c
            if i != 0:
                G[cur].append(cur - c)
            if cur % c != 0:
                G[cur].append(cur - 1)
            if j != (cur - 1):
                G[cur].append(cur + 1)
            if i != r -1:
                G[cur].append(cur + c)
    return G



def condition(r,c):
    if r < c - 1:
        print("A path may not exist")
    elif r > c - 1:
        print("There is at least one path")
    else:
        print("A Unique path exists")


def BFS(G,v):
    vis, prev = [False for a in range(len(G))], [-1 for b in (len(G))]
    q = queue.Queue(1)
    vis[v] = True
    while not q.empty():
        u = q.get()
        for i in G[u]:
            if not vis[i]:
                vis[i] = True
                prev[i] = u
                q.put(i)
    Print_Path(prev,len(G)-1)

def DFS_Recursion(G,s):
    global vis
    global pre
    vis[s] = True
    for i in G[s]:
        if not vis[i]:
            vis[i] = True
            pre[i] = s
            DFS_Recursion(G,i)





def DFS_Stack(G, v):
    vis, prev = [False for a in range(len(G))], [-1 for b in range(len(G))]
    s = []
    s.append(v)
    vis[v] = True
    while s != []:
        q = s.pop()
        for i in G[q]:
            if not vis[i]:
                vis[i] = True
                prev[i] = q
                s.append(i)
    Print_Path(prev, len(G)- 1)





def wall_List(maze_rows, maze_cols):
    w = []
    for i in range(maze_rows):
        for j in range(maze_cols):
            cur = j + i * maze_cols
            if j != maze_cols - 1:
                w.append([cur, cur + 1])
            if i != maze_rows - 1:
                w.append([cur, cur + maze_cols])
    return w

if __name__ == '__main__':
    print("Welcome tp Lab 7")

    maze_rows = 5
    maze_cols = 5

    print("The total number of cells in the maze are: ", maze_rows*maze_cols)
    W_R = int(input("Number of walls to be removed? "))
    print()

    print("Choose from these option below")
    U_C = int(input("Option 1: Standard Union\nOption 2: Union Compression"))
    w = wall_List(maze_rows, maze_cols)
    S = DisjointSetForest(maze_rows * maze_rows)

    condition(W_R,(maze_cols*maze_rows))
    while Num_Sets(S)>1:
        d = random.randint(0, len(w)-1)
        if U_C == 1:
            if union(S, w[d][0],w[d][1]):
                w.pop(d)
        elif U_C == 2:
            if union_c(S,w[d][0], w[d][1]):
                w.pop(d)

    G = ADJ_L(maze_rows,maze_cols,w)
    print("The following is the adjacency list: ", G)



