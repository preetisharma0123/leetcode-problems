"""Problem No.: 771
Problem:  Jewels and Stones
DS:  Hash map
Date:  21/07/2023
Detailed Problem: You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
"""
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        j_set = set(jewels)
        for i in stones:
            if i in j_set:
                count += 1
        return count
""" searching in set is O(1) time complexity, therefore this reduces the time. 
Time complexity reduced from O(len(j)*len(s)) to O(len(j)+len(s)). O(j) part comes from creating set j and O(s) part comes from searching each element in s.
"""
"""
Time Complexity:O(len(j)+len(s))
Space Complexity: O(1)
"""
