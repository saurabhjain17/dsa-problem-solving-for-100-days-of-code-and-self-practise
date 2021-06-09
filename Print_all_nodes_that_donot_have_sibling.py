''' Print all nodes that don't have sibling
Given a Binary Tree of size N, find all the nodes which don't have any sibling. Root node can not have a sibling.
 question link:- https://practice.geeksforgeeks.org/problems/print-all-nodes-that-dont-have-sibling/1/?category[]=Tree&category[]=Binary%20Search%20Tree&category[]=Tree&category[]=Binary%20Search%20Tree&problemStatus=unsolved&difficulty[]=0&page=1&sortBy=submissions&query=category[]Treecategory[]Binary%20Search%20TreeproblemStatusunsolveddifficulty[]0page1sortBysubmissionscategory[]Treecategory[]Binary%20Search%20Tree#
 '''
 #SOLUTION
 #User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
def preorder(root):
    global test
    if root is None:
        return
    else:
       
        if root.right is None and root.left is not None:
            test.append(root.left.data)
        if root.right is not None and root.left is  None:
            test.append(root.right.data)
          
        preorder(root.left)
        preorder(root.right)  
        
def noSibling(root):
    global test
    test=[]
    preorder(root)
    if len(test)>0:
        return sorted(test)
    else:
        return [-1]

#{ 
#  Driver Code Starts
from collections import deque
# Tree Node
class Node:
   def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree  
def buildTree(s):
   #Corner Case
   if(len(s)==0 or s[0]=="N"):          
       return None
       
   # Creating list of strings from input
   # string after spliting by space
   ip=list(map(str,s.split()))
   
   # Create the root of the tree
#   print(ip)
   root=Node(int(ip[0]))                    
   size=0
   q=deque()
   
   # Push the root to the queue
   q.append(root)                            
   size=size+1
   
   # Starting from the second element
   i=1                                      
   while(size>0 and i<len(ip)):
       # Get and remove the front of the queue
       currNode=q[0]
       q.popleft()
       size=size-1
       
       # Get the current node's value from the string
       currVal=ip[i]
       
       # If the left child is not null
       if(currVal!="N"):
           
           # Create the left child for the current node
           currNode.left=Node(int(currVal))
           
           # Push it to the queue
           q.append(currNode.left)
           size=size+1
       # For the right child
       i=i+1
       if(i>=len(ip)):
           break
       currVal=ip[i]
       
       # If the right child is not null
       if(currVal!="N"):
           
           # Create the right child for the current node
           currNode.right=Node(int(currVal))
           
           # Push it to the queue
           q.append(currNode.right)
           size=size+1
       i=i+1
   return root

   
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ans = noSibling(root)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends