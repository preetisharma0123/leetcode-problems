"""Problem No.: 1200
Problem:   Minimum Absolute Difference
Approach: counting sort
Date:  07/08/2023
Detailed Problem: Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]
Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
"""
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        shift = -min(arr)
        k = max(arr)+shift
        count = [0]*(k+1)
        output = []

        for elem in arr:
            count[elem+shift] =1

        min_diff = float(inf)
        prev = 0
        for curr in range(1,len(count)):
            if count[curr]==0:
                continue
                
            curr_diff = curr-prev
            if curr_diff==min_diff:
                output.append([prev-shift,curr-shift])
            elif curr_diff<min_diff:
                output = [[prev-shift,curr-shift]]
                min_diff = curr-prev

            prev = curr
        return output      
        
        
"""
Time Complexity:O(n)
Space Complexity: O(1)
"""
