"""Problem No.:1
Problem:  Two Sum
DS:  Hash set
Approach: One-pass Hash Table
Date: 17/06/2023
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            for key,value in nums_dict.items():
                if target-nums[i] == value:
                    return i , key
            nums_dict[i]= nums[i] 

    
"""
Time Complexity:O(n)
Space Complexity: O(n)

"""

"""
Approach-Brute force solution:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

Time Complexity:O(n**2)
Space Complexity: O(n)
"""
