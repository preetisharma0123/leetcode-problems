"""Problem No.: 259
Problem:   3Sum Smaller
Approach:2 pointers
Date:  28/07/2023
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
            result +=self.twoSum(nums,i,target-nums[i])
        return result
    
    def twoSum(self,nums, i,target):
        low = i+1
        high = len(nums)-1
        result =0
        while low<high:
            sum1 = nums[low]+nums[high]
            if sum1<target:
                result += (high - low)
                low +=1
            else:
                high -= 1
        return result
       
               
"""
Time Complexity:O(n*2).
Space Complexity: O(1) because no additional data structures are used.
"""
