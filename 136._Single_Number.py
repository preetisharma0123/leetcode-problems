"""Problem No.:136
Problem: Single Number
DS:  
Approach: Best approach to this is bit manipulation. a  XOR 0 = a, a XOR a = 0.
This can als be solved with hash maps with O(n) time and space complexity.
Date: 14/06/2023
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a    

"""
Time Complexity:O(n)
Space Complexity: O(1)
"""
