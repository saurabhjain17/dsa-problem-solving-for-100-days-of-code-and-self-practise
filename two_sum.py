'''Two sum
LINK:- https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 


'''

class Solution:
    def indexi(self,nums,left,right,x):
        i=0
        count=counti=0
        flag=clag=-1
        while (flag<0 or clag<0 or flag==clag) and i<len(nums):
            if (count==1 and counti==1) and flag>-1 and clag>-1 and flag!=clag:
                return(min(flag,clag),max(flag,clag))
            if nums[i]==x[left] and count==0:
                flag=i
                count=1
            elif nums[i]==x[right] and counti==0:
                clag=i
                counti=1
            i+=1
        if flag<clag:
            return flag,clag
        elif flag>clag:
            return clag,flag
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     if target-nums[i] in nums and nums.index(target-nums[i])!=i :
        #         return [i,nums.index(target-nums[i])]
            left=0
            right=len(nums)-1
            x=sorted(nums)
            while left<=right:
                if x[left]+x[right]==target:
                    flag,clag=self.indexi(nums,left,right,x)
                    return [flag,clag]
                elif x[left]+x[right]>target:
                    right-=1
                else:
                      left+=1  
            return -1            