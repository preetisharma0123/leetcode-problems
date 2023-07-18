"""Problem No.: 219
Problem:   Contains Duplicate II
DS:  Hash map
Date: 18/07/2023

Problem elaborated: Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict1 = {}

        for i in range(len(nums)):
            if nums[i] in dict1:
                return True
            else:
                dict1[nums[i]]=i
            if (len(dict1))>k:
                dict1.pop(nums[i-k])
        
        
        return False
"""
Time Complexity:O(n)
Space Complexity: O(1)
"""
