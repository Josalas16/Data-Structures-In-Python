# Jaime O. Salas
# Data Structures & Algorithms
# TA:  Anindita Nath and Maliheh Zargaran
# Instructor: Olac Fuentes
# Last modification: 4/1/19
# Purpose of Program: The purpose of this program is to compare both data structures Binary Search Trees
# As well as Hashing with strings to see which would be better between the two data structures

# Disclaimer
# For this lab I used Pycharm, which i then stored the text file
# into a directory, not sure if it will cause problems but just wanted to let you know
# The glove file should be in the directory but its too big to upload on github



from BST import *
from HashChaining import *
import numpy as np
import math
import time

######### Lab Code Below ################

lab_start = time.time()

print("Welcome to Lab 5")
print("Listed below are some of the options for this lab")
print("1. Binary Search Tree\n2. Hashing via Chaining")
User_Choice = int(input())

# Lab File will contain the file glove
Lab_File = open("Lab_FIle/glove.6B.50d.txt", encoding= "utf-8", errors='ignore')
My_File = open("Lab_File/MyFile.txt")

if User_Choice == 1:
    BST_Choice(Lab_File, My_File)
elif User_Choice == 2:
    Hash_Option(Lab_File, My_File)
else:
    print("That is a wrong input")
    print("Please choose from Options 1 or 2")



