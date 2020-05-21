# Author: Jaime O Salas
# Data Structures & Algorithms
# TA: Anithdita Nath
# IA: Eduardo Lara
# Instructor: Olac Fuentes
# Last Modification: 2/15/19
# Purpose Of Program: The Purpose of this program is to know and understand
# the implementations of B-Trees by doing several "requirements" in the lab.
# and how they can be different than BST (Binary Search Trees)

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i) 
        
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
    
##################### Lab Code Below ##################################



# 1. Compute the height of the tree
def height(T):
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])


# B-Tree to sorted array method should be below
# 2. Extract the items in the B-Tree into a sorted list
def Tree_To_List(T):
    Tree_List = []
    if T.isLeaf: return T.item
    for i in range(len(T.child)):
        Tree_List += Tree_To_List(T.child[i])
        Tree_List.append(T.child[i])
    return Tree_List
    


# 3. Return the minimum element in the tree at a given depth d.
def min_Element(T, d):
    if T.isLeaf: return None
    if d == 0: return T.item[0]
    return min_Element(T.child[0], d - 1)


# 4. Return the maximum element in the tree at a given depth d.
def Max_Element(T, d):
    if T.isLeaf: return None
    if d == 0:  return T.item[len(T.item) -1]
    return Max_Element(T.child[len(T.item)], d - 1)

# 5. Return the number of nodes in the tree a  given depth d.
def Nodes_At_Depth(T, d):
    sum = 0
    if d == 0: return 1
    if T.isLeaf: None
    for i in range(len(T.child)):
        sum += Nodes_At_Depth(T.child[i], d - 1)
    return sum




# 6. Print all the items in the tree at a given depth d
def Print_Items_At_Depth(T,d):
    if T is None: return
    if d == 0: print(T.item, end=' ')
    for i in range(len(T.child)):
        Print_Items_At_Depth(T.child[i], d - 1)



# 7. Return the number if nodes in the tree that are full
def Full_Nodes(T):
    sum = 0
    if T.isLeaf: return 0
    #if len(T.item) equal T.max_items: return 1
    for i in range(len(T.child)):
        sum += Full_Nodes(T.child[i])
    return sum


# 8. Return the number of leaves in the tree that are full
def Full_Leaves(T):
    sum = 0
    if T.isLeaf:

        if len(T.item) == T.max_items:
            return 1
        else:
            return 0
    for i in range(len(T.child)):
        sum += Full_Leaves(T.child[i])
    return sum



# 9. Given a key, return the depth at which it is found in the tree, of
# -1 if k is not in the tree
def Depth_Return_Key(T,k):
    if T.isLeaf: return None
    if k == T.item[0]:
        return
    return 1

L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6]
T = BTree()    
for i in L:
    Insert(T,i)

PrintD(T,'')
print()
print("#########################################################")

###### Testing of the methods above with the list #######

# 1. Computing the height of the tree
print("The  height of the B-Tree is",height(T))
print()

# 2. Extracting the items in the B-tree into a sorted list
print("Here is the tree converted into a sorted list", Tree_To_List(T), ' ')
print()

# 3.  Returning thr minimum element in the tree at a given depth d
print("The Minimum  Number in the given depth is", min_Element(T,1))
print()

# 4. Returning the maximum element in the tree at the given depth d
print("The Largest Number in the given depth is", Max_Element(T,1))
print()


# 5. Returning the number of nodes in the tree at a given depth d
print("These are the number of nodes at the given depth", Nodes_At_Depth(T,0))
print()


# 6. Printing all the items in the tree at a given depth d
print("These are items/lists at the given depth:")
Print_Items_At_Depth(T, 2)
print()
print()


# Double check this
# 7. Return the number of nodes in the tree that are full
print("Here are the Nodes that are full", Full_Nodes(T))
print()

# Double check this 
# 8. Return the number of leaves in the tree that are full
print("The Number of leaves that are in the tree full are", Full_Leaves(T))
print()


# 9. Given a key k, return the depth at which it is found in the tree,
# -1 if k is not in the tree.
print("This is the depth of the given key", Depth_Return_Key(T,30))
print()




