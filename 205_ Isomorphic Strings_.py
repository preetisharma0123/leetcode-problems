"""Problem No.: 205
Problem: Isomorphic Strings
DS:  Hash set
Approach: we create 2 different dictionaries to check one to one mapping of the strings in both ways and check if it is same.
Date: 17/07/2023

Problem explained with examples:
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1, dict2 = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]
             
            if (c1 not in dict1) and (c2 not in dict2):
                dict1[c1] = c2
                dict2[c2] = c1
            elif dict1.get(c1) != c2 or dict2.get(c2) != c1:
                return False
        return True


"""
Time Complexity:O(n)
Space Complexity: O(1)
"""
