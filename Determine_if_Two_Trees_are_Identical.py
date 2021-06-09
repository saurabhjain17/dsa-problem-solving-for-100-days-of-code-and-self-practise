''' Determine if Two Trees are Identical

Given two binary trees, the task is to find if both of them are identical or not. 
link:- https://practice.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1/?category[]=Tree&category[]=Binary%20Search%20Tree&category[]=Tree&category[]=Binary%20Search%20Tree&problemStatus=unsolved&difficulty[]=0&page=1&sortBy=submissions&query=category[]Treecategory[]Binary%20Search%20TreeproblemStatusunsolveddifficulty[]0page1sortBysubmissionscategory[]Treecategory[]Binary%20Search%20Tree#

'''

#SOLUTION
#User function Template for python3

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    #Function to check if two trees are identical.
    def inorder(self,root1,root2):
        global test
        if root1 is None and root2 is None:
            return 
        if root1 is None and root2 is not None:
            test[0]=0
            return 
        if root1 is not None and root2 is None:
            
            test[0]=0
            return     
        else:   
           if root1.data!=root2.data:
               test[0]=0
               return    
           self.inorder(root1.left,root2.left)  
           
           self.inorder(root1.right,root2.right)
        
    def isIdentical(self,root1, root2):
        global test
        test=[1]
        self.inorder(root1,root2)
        if test[0]==1:
            return True
        return False    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3



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
        s1=input()
        s2=input()
        head1=buildTree(s1)
        head2=buildTree(s2)
        if Solution().isIdentical(head1, head2):
            print("Yes")
        else:
            print("No")
        
        

# } Driver Code Ends