'''
Given an unsorted array arr[] of n positive integers.
 Find the number of triangles that can be formed with three different array elements as lengths of three sides of triangles. 
n = 3
arr[] = {3, 5, 4}
Output: 
1
Explanation: 
A triangle is possible 
with all the elements 5, 3 and 4.


Tagged company: AMAZON
level: Medium

link:https://practice.geeksforgeeks.org/problems/count-possible-triangles-1587115620/1/?track=DSA-Foundation-Sorting&batchId=197#
'''
#SOLUTION

#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def findNumberOfTriangles(self, arr, n):
        arr.sort()
        count=0
        for i in range(n-2):
            k=i+2
            for j in range(i+1,n):
                while(k<n and arr[i]+arr[j]>arr[k]):
                    k+=1
                count+=k-j-1
        return count            
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findNumberOfTriangles(arr,n))

# } Driver Code Ends
