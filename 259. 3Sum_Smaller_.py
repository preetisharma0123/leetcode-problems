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
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i ==0 or nums[i-1] != nums[i]:
                self.twoSum(nums,i,result)
        return result

    
    def twoSum(self,nums, i,result):
        low = i+1
        high = len(nums)-1
        while (low <high):
            sum = nums[i]+nums[low]+nums[high]
            if sum>0:
                high -=1               
            elif sum<0:
                low +=1
            else: 
                result.append([nums[i],nums[low],nums[high]])
                low +=1
                high -=1
                while (low<high )and nums[low]== nums[low-1]:
                    low +=1
                
               
"""
Time Complexity:O(n*2).
Space Complexity: O(1) because no additional data structures are used.
"""
