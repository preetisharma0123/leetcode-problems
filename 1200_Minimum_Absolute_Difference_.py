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
        # Sort the original array
        arr.sort()

        # Initialize minimum difference `min_pair_diff` as a huge integer in order not 
        # to miss the absolute difference of the first pair. 
        min_pair_diff = float('inf')
        answer = []

        # Traverse the sorted array
        for i in range(len(arr) - 1):
            # For the absolute value `curr_pair_diff` of the current pair:
            curr_pair_diff = arr[i + 1] - arr[i]

            # If `curr_pair_diff` equals `min_pair_diff`, add this pair to the answer list.
            # If `curr_pair_diff` is smaller than `min_pair_diff`, discard all pairs in the answer list, 
            # add this pair to the answer list and update `min_pair_diff`.
            # If `curr_pair_diff` is larger than `min_pair_diff`, we just go ahead.
            if curr_pair_diff == min_pair_diff:
                answer.append([arr[i], arr[i + 1]])
            elif curr_pair_diff < min_pair_diff:
                answer = [[arr[i], arr[i + 1]]]
                min_pair_diff = curr_pair_diff

        return answer
        
        
"""
Time Complexity: O(n⋅log(n))
Space Complexity: O(n)
"""
