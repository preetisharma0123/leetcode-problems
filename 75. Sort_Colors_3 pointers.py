"""Problem No.: 75
Problem:  Sort Colors
Approach: 3 pointers
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
        p0,curr,p2 = 0,0,len(nums)-1
        while curr<=p2:
            if nums[curr]==0:
                nums[curr],nums[p0]= nums[p0],nums[curr]
                curr +=1
                p0 +=1
            elif nums[curr]== 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -=1
                
            elif nums[curr]==1:
                curr+=1
        return nums            
        
        
"""
Time Complexity:O(n)
Space Complexity: O(1)
"""
