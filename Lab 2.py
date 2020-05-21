# Author: Jaime O Salas
# Data Structures & Algorithm
# TA: Anithdita Nath
# Instructor: Olac Fuentes
# Last Modification: 2/22/19
# Purpose Of Program: The Purpose of the program is to familiarize ourselves
# with different sorting algorithms and to see their differences between them.



import random

# Nodes
class Node(object):#Constructor
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

def PrintNodes(N):
    if N is not None:
        print(N.item, end=' ')
        PrintNodes(N.next)

def PrintNodesReverse(N):
    if N is not None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')

# Lists
class List(object):  # Constructor
    def __init__(self):
        self.head = None
        self.tail = None

def IsEmpty(L):
    return L.head == None

def Append(L,x):  # Inserts x at the end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next

def Preppend(L,x): # Inserts x at beginning of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.head = Node(x, L.head)

def InsertAfter(L,x, item):
    s = Search(L,x)
    if s is None:
        Append(L,item)
    else:
        s.next = Node(item, s.next)

def Search(L, x): # Search the list for the node
    temp = L.head
    while temp is not None:
        if temp.item == x:
            temp = temp.next
            return None

def GetLength(L):
    count = 0
    temp = L.head
    while L is not None:
        count += 1
        temp = temp.next
        return count

def IsSorted(L):
    if L.head is None or L.head.next is None:
        return True
    temp = L.head
    while temp.next is not None:
        if temp.item > temp.next.item:
            return False
        return True

def ElementAt(L,x):
    if L.head is None:
        return None
    node = L.head
    count = 0
    while count < x:
        node = node.next
        count+= 1
        return node

def Copy(L):
    cloned_List = List()
    node = L.head
    while node is not None:
        Append(cloned_List, node.item)
        node = node.next
        return cloned_List

# Method for finding the median using Bubble Sort
def Bubble_Median(L):
    C = Copy(L)
    Bubble_Sort(C)
    return ElementAt(C,GetLength(C)//2)

#Method for finding the median using Merge Sort
def Merge_Median(L):
    C = Copy(L)
    Merge_Sort(C)
    return ElementAt(C, GetLength(C)//2)

def Quick_Median(L):
    C = Copy(L)
    QuickSort(C)
    return ElementAt(C, GetLength(C)//2)



#def Bubble_Median(L):
   # C = Copy(L)
   # Bubble_Sort(C)
    #temp = C.head
    #for i in range(C.Len//2):
      #  temp = temp.next
       # return temp.item


def Print(L):  # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New Line

def PrintRec(L): # Prints list L's items in order using a for loop
    PrintNodes(L.head)
    print()

def PrintReverse(L): # Prints list L's items in reverse order
    PrintNodesReverse(L.head)
    print()

# Removes x from list L
# It does nothing if x is not in L
def Remove(L,x):
    if L.head == None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:  # Find x
        temp = L.head
        while temp.next != None and temp.next.item != x:
            if temp.next == L.tail: # x is the last node
                L.tail = temp
                L.tail.next = None
            else:
                temp.next = temp.next.next

# Sorting Methods For The Lab
# Bubble sort
# O(n^2) running time
def Bubble_Sort(L):
    if IsEmpty(L):
        return
    else:
        change = True
    while change:
        t = L.head
        change = False
        while t.next is not None:
            if t.item > t.next.item:
                temp = t.item
                t.item = t.next.item
                t.next.item = temp
                change = True
            t = t.next

# Merge Sort usually is O(nlogn)
def Merge_Sort(L):
    mergeSort = L
    if L is None:
        return L
    length = GetLength(L)
    for i in range(int(length/2) - 1): # Half length of the total linked list
        mergeSort = mergeSort.next
        rightside = mergeSort.next
        #mergeSort.next = None
        leftside = L

        side1 = Merge_Sort(leftside) # left side
        side2 = Merge_Sort(rightside) # Right side

        sort_finished = None
        if side1.item > side2.item:
            sort_finished = side1
            side1 = side1.next
        else:
            sort_finished = side2
            side2 = side2.next
            head = sort_finished
            while side1 is not None and side2 is not None:
                if side1.item > side2.item:
                    sort_finished.next = side1
                    side1 = side1.next
                else:
                    sort_finished = side2
                    side2 = side2.next
                    sort_finished = sort_finished.next

                    while side1 is not None:
                        sort_finished.next = side1
                        side1 = side1.next
                        sort_finished = sort_finished.next

                    while side2 is not None:
                        sort_finished.next = side2
                        side2 = side2.next
                        sort_finished = sort_finished.next
                        return sort_finished.next




# 3. Sort list using quick sort, then return the element in the middle
# Worst case is O(n^2)
# Average case is O(n log n)
"""
def Quick_Sort(L):
    if IsEmpty(L):
        print('The list is empty')
        return
    else:
        pivot = L.head

def Quick_Sort(L):
    Quick_Sort2(L, 0, len(L)-1)

def Quick_Sort2(L, low, high):
    if low < high:
        p = partition(L,low, high)
        Quick_Sort2(L, low, p-1)
        Quick_Sort2(L, p + 1, high)

def pivoting(L,low,high):
    mid = (high + low) //2
    switch = high
    if L[low] < L[mid]:
        if L[mid] < L[high]:
            switch = mid
        elif L[low] < L[high]:
            switch = low
            return switch
# lists is split
    def partition(L, low, high):
        switchIndex = pivoting(L,low, high)
        switchValue = L[switchIndex]
        L[switchIndex], L[low] = L[low], L[switchIndex]
        border = low
# iterating through the list
        for i in range(low, high + 1):
            if L[i] < switchValue:
                border += 1
                L[i], L[border] = L[border], L[i]
                # swaps the border position
                L[low], L[border] = L[border], L[low]
                return  border
"""





# List is created below
# from 1 - 100 possible numbers
L = List()
for i in range(6):
    x = random.randrange(0,101)
    Append(L,x)


# Original list is below
print("This is the original list: ")
Print(L)
print()

#Bubble Sort Method
print("This is the Bubble Sort List: ")
Bubble_Sort(L)
med = Bubble_Median(L)

# Merge Sort list is printed below
print("This is Merge Sort: ")
Merge_Sort(L)
Print(L)
print()

print("This is Quick Sort: ")

Print(L)
print()

