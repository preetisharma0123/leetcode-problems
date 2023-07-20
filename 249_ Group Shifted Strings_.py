"""Problem No.: 249
Problem:  Group Shifted Strings
DS:  Hash map
Date: 19/07/2023

Detailed Problem: We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

 

Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
Example 2:

Input: strings = ["a"]
Output: [["a"]]
"""
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        magic_dict = {}
        for s in strings:
            count =""*len(s)
            for char in range(len(s)-1):
                count += str((ord(s[char])-ord(s[char+1]))%26)+"#"

            if count not in magic_dict:
                magic_dict[count] = [s]
            else:
                magic_dict[count].append(s)
            
        return magic_dict.values()





"""
Time Complexity: O(NKlogK), where N is the length of strs, and K is the maximum length of a string in strs. The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(Klog⁡K) time.
Space Complexity: O(NK), the total information content stored in magic_dict

"""
