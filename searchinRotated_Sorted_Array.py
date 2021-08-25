'''
# Search in rotated sorted array 


There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104


LINK:-  https://leetcode.com/problems/search-in-rotated-sorted-array/


'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        low=0
        end=len(nums)-1
        while low<=end:
            mid=(low+end)//2
            if nums[mid]==target:
                return mid
            if nums[low]==target:
                return low
            if nums[end]==target:
                return end
            if low==end:
                if nums[mid]==target:
                    return mid
                return -1
            if nums[mid]>nums[end]:
                if target>nums[mid]:
                    low=mid+1
                elif target>nums[end]:
                    end=mid-1
                else:
                    low=mid+1
            elif nums[mid]<=nums[end]:
                if nums[end]<target:
                    end=mid-1
                elif target>nums[mid]:
                    low=mid+1
                else:
                    end=mid-1                                 


        return -1      