"""Problem No.: 75
Problem:  Sort Colors
Approach:Counting sort 
Date:  07/08/2023
Detailed Problem: Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
                
        # O(N)
        zeros = 0
        onces = 0
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                onces += 1
        
        for i in range(len(nums)):
            if zeros > 0:
                nums[i] = 0
                zeros -= 1
            elif onces > 0 :
                nums[i] = 1
                onces -= 1
            else:
                nums[i] = 2
        
        
"""
Time Complexity:O(n)
Space Complexity: O(1)
"""
