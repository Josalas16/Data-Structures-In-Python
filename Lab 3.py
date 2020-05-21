# Author: Jaime O Salas
# Data Structures & Algorithm
# TA: Anithdita Nath
# IA: Eduardo Lara
# Instructor: Olac Fuentes
# Last Modification: 3/8/19
# Purpose Of Program: The purpose of this lab is to see the implementations of Binary
# Search Trees (BST's) and familiarize ourselves with them as well

import math
import matplotlib.pyplot as plt
import numpy as np

# BST Class
class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

# Method will Insert new items into the tree
def Insert(T ,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left ,newItem)
    else:
        T.right = Insert(T.right ,newItem)
    return T

def Delete(T ,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left ,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right ,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right ,m.item)
    return T

def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item ,end = ' ')
        InOrder(T.right)

def InOrderD(T ,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right ,space +'   ')
        print(space ,T.item)
        InOrderD(T.left ,space +'   ')

def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T

def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)

def Find(T ,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item <k:
        return Find(T.right ,k)
    return Find(T.left ,k)

# Methods for the circles are below
def circle(center ,radius):
    n = int(4 * radius * math.pi)
    t = np.linspace(0 ,6.3, n)
    x = center[1] + radius * np.sin(t)
    y = center[0] + radius * np.cos(t)
    return x ,y

# Method will print the circles for the tree
def draw_circles(ax, center, radius):
    x ,y = circle(center ,radius)
    ax.plot(x ,y, color='k')
    ax.fill(x ,y, color='white', )

''' 
Handout code
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')
'''
# If the item in the BST is found then
# If will be printed
# If its found then it will print "has been found"
# If hasnt been found it will return 'has not been found'
def FindAndPrint(T ,k):
    f = Find(T ,k)
    if f is not None:
        print(f.item ,'has been found')
    else:
        print(k ,'has not been found')

# Prints all the items in the depts of BST
def DepthPrint(T ,k):
    if T is None:
        return None
    if k is 0:
        print(T.item, end = " ")
    else:
        DepthPrint(T.left, k -1)
        DepthPrint(T.right, k - 1)


# 1. Graphing the tree
# Zorder = default for drawing axes,patches,lines and text.
def CircleD(T, center, radius, ax):
    if T != None:
        x, y = circle(center, radius)
        ax.plot(x, y, color='k', zorder=1, linewidth=2.5)
        ax.fill(x, y, color='white', zorder=1, linewidth=2.5)
        ax.text(center[0], center[1], str(T.item), horizontalalignmnet='center', verticalalignment='center',
                fontsize=6.5, zorder=4)


def BST_Draw(ax, c, T, x, y):
    if T == None:
        return None
    if T.left is not None and T.right is not None:
        # Left side will be plotted first followed by the recursive call
        ax.plot([c[0], c[0] - x], [c[1], c[1] - y], color='k')
        BST_Draw(ax, [c[0] - x, c[1] - y], T.left, x * 0.5, y * 0.9)
        # Then the right side next with the recrusive call aswell
        ax.plot([c[0], c[0] + x], [c[1], c[1] - y], color='k')
        BST_Draw(ax, [c[0] + x, c[1] - y], T.right, x * 0.5, y * 0.9)
    plt.plot(c[0], c[1], markersize=12, markeredgecolor='black')


# 2.Seach iterative
def Iterative_Search(T, k):
    if T is None:
        return None
    while T != None and T.item != k:
        # If k is smaller, it will move to the left child
        if k < T.item:
            T = T.left
        # If k is bigger, then it will move to the right child
        elif k > T.item:
            T = T.right
    return T


# 3. Building a balanced tree given a sorted array
# must be build with O(n) time
def Build_Tree(SortedArr):
     if not SortedArr:
         return None
     if len(SortedArr) != 0:
     # Finds the middle, while adding the new elements
        middle = (len(SortedArr)) // 2
     # T is the root
        T = BST(SortedArr[middle])
        T.left = Build_Tree(SortedArr[:middle])
     # Right Subtree will have the values greater than the middle
        T.right = Build_Tree(SortedArr[middle + 1:])
        return T
        
def Tree_Arr(T, SortedArr):
    if T is None:
        return None
    elif T is not None:
        Tree_Arr(T.left, SortedArr)
        SortedArr.append(T.item)
        Tree_Arr(T.right, SortedArr)


# 4. Extracting the elements in a binary search tree
# into a sorted tree


# Code to test the functions
T = None
A = [70, 50, 90, 130, 150, 40, 10]
for a in A:
    T = Insert(T, a)

T2 = None
# Numbers from the handout
Array2 = [10,4,15,2,8,12,18,1,5,3,9,7]
for array2 in Array2:
    Array2 = Insert(T2,array2) 



plt.close('all')
fig, ax = plt.subplots()
BST_Draw(ax, [0, 0], T, 50, 50)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()


# 5. Print the elements in the BST by the depths
# A for loop could also be used
print("Keys at depth 0:", end=' ')
DepthPrint(T, 0)
print()

print("Keys at depth 1:", end=' ')
DepthPrint(T, 1)
print()

print("Keys at depth 2:", end=' ')
DepthPrint(T, 2)
print()

print("Keys at depth 3:", end=' ')
DepthPrint(T, 3)
print()

print("Keys at depth 4:", end=' ')
DepthPrint(T, 4)
print()
