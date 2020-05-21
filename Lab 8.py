# Jaime O. Salas
# Data Structures & Algorithms
# TA:  Anindita Nath and Maliheh Zargaran

# Instructor: Olac Fuentes
# Last modification: 5/10/19
# Purpose of Program: The purpose of this program is to discover the trigonometric identities,
# in which this program will test all the combinations of the tri expressions.



import mpmath
import numpy as np
from mpmath import *
import random
import time



F = ["sin(x)", "cos(x)", "tan(x)", "1/cos(x)", "-sin(x)",
     "-cos(x)", "-tan(x)", "sin(-x)", "cos(-x)", "tan(-x)",
     "sin(x)/cos(x)", "2 * sin(x/2)*cos(x/2)", "sin(x)*sin(x)",
     "1-(cos(x)*cos(x))", "(1-cos(2*x))/2", "sec(x)"]
S = [2, 4, 5, 9, 12]
S2 = []
# Used some of the code Dr. Fuentes provided in his website
# Randomization, with tries set to 1000
def equal(F1, F2, tries = 1000, tolerance=0.0001):
     for i in range(tries):
          x = random.random()
          y1 = eval(F1)
          y2 = eval(F2)
          if np.abs(y1-y2) > tolerance:
               return False
     return True


def Verify_EQ(F):
     for i in range(len(F)):
          for j in range(i + 1, len(F), 1):
               if equal(F[i],F[j]): print(F[i], F[j], "There are the same.")




def SubSum(S,S2, l, goal):
     if goal == 0: return True, []
     if goal < 0 or l < 0: return False, []
     res, subset = SubSum(S, S2, l - 1, goal-S[l])
     if res:
          subset.append(S[l])
          S2.remove(S[l])
          return True, subset
     else:
          return SubSum(S, S2,  l-1, goal)



def Partition(S):
     s = sum(S)
     if s % 2 != 0:
          return False
     elif s % 2 == 0:
          S2 = [i for i in S]
          found, s = SubSum(S, S2, len(S)-1, sum(S)//2)
     if found:
          print("Sets", S)
          print("Solution:", s, " & ", S2)
     else:
          print("No Solution:")




if __name__ == '__main__':
     Start_Running = time.time()
     print('Welcome to Lab 8 Please hold\n')
     print("Here are the verifications for the trigonometric expressions")

     print(Verify_EQ(F))
     print()


     print(Partition(S))
     End_running = time.time()
     total_running = End_running - Start_Running
     print()
     print("The running time of the program is: ", total_running)





















































