'''
Given a Binary Tree, your task is to find its level order traversal.
For the below tree the output will be 1 $ 2 3 $ 4 5 6 7 $ 8 $.

          1
       /     \
     2        3
   /    \     /   \
  4     5   6    7
    \
     8

     question link:-https://practice.geeksforgeeks.org/problems/level-order-traversal-line-by-line/1/?category[]=Tree&category[]=Binary%20Search%20Tree&category[]=Tree&category[]=Binary%20Search%20Tree&problemStatus=unsolved&difficulty[]=0&page=1&sortBy=submissions&query=category[]Treecategory[]Binary%20Search%20TreeproblemStatusunsolveddifficulty[]0page1sortBysubmissionscategory[]Treecategory[]Binary%20Search%20Tree
'''
#SOLUTION
#User function Template for python3

'''
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return the level order traversal line by line of a tree.
def levelOrder(root):
    
    if root ==None:
        return ["$"]
    else:
        x=[]
        
        q=[root]
        while len(q):
            count=len(q)
            m=[]
            for i in range(1,count+1):
                temp=q.pop(0)
                m.append(temp.data)
                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right) 
            x.append(m)  
        return x    
                    

#{ 
#  Driver Code Starts
#Contributed by Sudarshan Sharma
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
        result = levelOrder(root)
        for values in result:
            for value in values:
                print(value,end = " ")
            print("$",end = " ")
        print()


# } Driver Code Ends