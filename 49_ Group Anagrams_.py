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
        
        #let's create a dictionary
        magic_dict = {}

        # we iterate through each string in strs
        for i in range(len(strs)):
            # for each string we create a list called as count
            count = [0]*26
            # for each character in the string we find the ASCII value and assign it to an index and increment it by one for each count
            for char in strs[i]:
                count[ord(char)-ord("a")] += 1
            # once we finalize the count list, we change it to string by adding a delimiter after each number. this is required to eliminate any chance of error.
            key = "#".join(map(str,count)) 

            # we are using the map function here, as the count list has numbers and not strings
        
            # finally we see if the key we got from each string is there in the dictionary or not. If it is there, we add the value to the value list. If not we add the key, value pair to the dictionary
            if key not in magic_dict:
                magic_dict[key] = [strs[i]]
            else:
                magic_dict[key].append(strs[i])

        return magic_dict.values()





"""
Time Complexity: O(NKlogK), where N is the length of strs, and K is the maximum length of a string in strs. The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(Klog⁡K) time.
Space Complexity: O(NK), the total information content stored in magic_dict

"""
