"""Problem No.: 49
Problem: 49. Group Anagrams
DS:  Hash map
Approach:
Date: 18/07/2023

Detailed Problem:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 """
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        magic_dict = {}
        for i in range(len(strs)):
            
            key = tuple(sorted(strs[i]))
            if key not in magic_dict:
                magic_dict[key] = [strs[i]]
            else:
                magic_dict[key].append(strs[i])

        return magic_dict.values()



"""
Time Complexity: O(NKlogK), where N is the length of strs, and K is the maximum length of a string in strs. The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(Klog⁡K) time.
Space Complexity: O(NK), the total information content stored in magic_dict

"""
