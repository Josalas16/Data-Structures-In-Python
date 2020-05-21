# Author: Jaime O Salas
# Data Structures & Algorithms
# TA: Anithdita Nath
# Instructor: Olac Fuentes
# Last Modification: 2/8/19
# Purpose of program: The purpose of this lab is to be
# able to draw figures/fractals recursively


import matplotlib.pyplot as plt
import numpy as np
import math
import time


 # method for the circle
def circle(center, rad):
    n = int(4 * rad * math.pi)
    t = np.linspace(0, 6.3, n)
    x = center[0] + rad * np.sin(t)
    y = center[1] + rad * np.cos(t)
    return x, y


# method to draw the multiple circles
def draw_circles(ax, n, center, radius, w):
    if n == 0:
        return
    if n > 0:
       x, y = circle(center, radius)
       ax.plot(x, y, color='k')
       draw_circles ( ax, n - 1, center, radius * w, w)

#plt.close("all")
fig, ax = plt.subplots ()
draw_circles(ax, 50, [100, 0], 100, .9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig ('circles.png')


# Example of the recursive squares
# n = level of recursive calls
# p = coordinates of corner squares
def draw_squares(ax, n, p, w):
    if n == 0:
        return
    if n > 0:
        index_1 = [1, 2, 3, 0, 1]
        q = p * w + p[index_1] * (1 - w)

        #plots the square
        ax.plot ( p[:, 0], p[:, 1], color='k' )
        draw_squares ( ax, n - 1, q, w )


#plt.close ( 'all' )
orig_size = 800
p = np.array ( [[0, 0], [0, orig_size], [orig_size, orig_size], [orig_size, 0], [0, 0]] )
fig, ax = plt.subplots ()
draw_squares ( ax, 15, p, .8 )
ax.set_aspect ( 1 )
ax.axis ( 'off' )
plt.show ()
fig.savefig('squares.png')

#1. Drawing the recursive squares
def draw_squares(ax, n, p, w):
    if n == 0:
        return
    if n > 0:
        q = p * w
        ax.plot ( p[:, 0], p[:, 1], color='k' )
        draw_squares ( ax, n - 1, q / w, w )



#plt.close ( 'all' )
orig_size = 800
# This is the array of the square
p = np.array ( [[0, 0], [0, orig_size], [orig_size, orig_size], [orig_size, 0], [0, 0]])
fig, ax = plt.subplots()
draw_squares ( ax, 15, p, .8 )  # These 3 lines from above draw one single square
ax.set_aspect ( 1 )
ax.axis ( 'off' )
plt.show () # shows the plotted graph
fig.savefig('squares.png') # Saves the file into a png



# 2. Shell Circle
def multi_circles(ax, n, center, radius, w):
    if n == 0:
        return

    elif n > 0:
       x, y = circle(center, radius)
       ax.plot ( x + radius, y, color='k') # Adds a different radius each time the graph is being plotted
       multi_circles( ax, n - 1, center, radius * w, w )


#plt.close("all")
fig, ax = plt.subplots ()
multi_circles(ax, 50, [100, 0], 100, .9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig ( 'multi_circles.png' )


# 3. Write a recursive method to draw a tree
def binary_tree(ax, n, x_axis, y_axis, nodes):
    if nodes == 0:
        return

    if nodes > 0:
        ax.plot([n[0], n[0]- y_axis], [n[0], n[0] - x_axis], color='k')
        binary_tree(ax, [n[0] - x_axis, n[1] - y_axis], nodes - 1, x_axis/2, x_axis* .9)

#plt.close("all")
fig, ax = plt.subplots()
n = np.array([0,0])
binary_tree(ax, n, 5, 50, 10) # Method call
ax.set_aspect(1.0)
ax.axis('on') # an.axis shows the graphs "
plt.show() # shows the plot of the graph
fig.savefig('binary_tree.png')


# 4. Write recursive method to draw  the circle with multiple circle
#def multi_circle(ax, n,)