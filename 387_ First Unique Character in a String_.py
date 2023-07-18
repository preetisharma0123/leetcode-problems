"""Problem No.: 387
Problem:  First Unique Character in a String 
DS:  Hash map
Date: 18/07/2023
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # let's make a dict to store the chrs in string and the number of times they appear
        dumm_dict = {}

        #let's itirrate over the string and place the chrs and the frequesncy in the dict
        for i in range(len(s)):
            if s[i] in dumm_dict:
                dumm_dict[s[i]] +=1
            else:
                dumm_dict[s[i]] = 1
        # let's return the first index with unique chr 
        for i in range(len(s)):        
            if dumm_dict[s[i]] ==1:
                        return i
            
        return -1
"""
Time Complexity:O(n)
Space Complexity: O(n)
"""
