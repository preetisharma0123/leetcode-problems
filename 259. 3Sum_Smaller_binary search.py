"""Problem No.: 259
Problem:   3Sum Smaller
Approach: binary search
Date:  31/07/2023
Detailed Problem:Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

 

Example 1:

Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]
Example 2:

Input: nums = [], target = 0
Output: 0
Example 3:

Input: nums = [0], target = 0
Output: 0
"""
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        result =0
        nums.sort()

        if len(nums) <3:
            return 0
        for i in range(len(nums)-2):
            result +=self.twoSum(nums,i+1,target-nums[i])
        return result
    
    def twoSum(self,nums, startindex,target):
        result = 0
        for i in range(startindex,len(nums)-1):
           j = self.binarySearch(nums,i,target-nums[i])
           result += j-i
        return result


    def binarySearch(self,nums, startindex,target):
        left = startindex
        right = len(nums)-1
        while left<right:
            mid =(right+left+1)//2
            if nums[mid]<target:
                left = mid
            else:
                right = mid-1
        return left
       

                
               
"""
Time Complexity:O(n2 logn) The binarySearch function takes O(log⁡n) time, therefore the twoSumSmaller takes O(nlog⁡n) time. The threeSumSmaller wraps with another for-loop, and therefore is O(n2log⁡n) time.
Space Complexity: O(1) because no additional data structures are used.
"""
