'''
Kadane's Algorithm 
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

link:-https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1

'''

#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        res=a[0]
        max_sum=a[0]
        for i in range(1,size):
            res=max(res+a[i],a[i])
            max_sum=max(res,max_sum)
        return max_sum    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends