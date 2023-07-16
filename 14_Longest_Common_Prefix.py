"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings

 """

 class Solution(object):
    def longestCommonPrefix(self,strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        if len(strs)<=1:
            return strs[0]
        if 1<len(strs)<=200:
            small_len = len(strs[0])

            small_len = len(strs[0])
        
            for idx in range(1,len(strs)):
                if len(strs[idx])< small_len:
                    small_len = len(strs[idx])
            chr = 0     
            while (chr<small_len):
                counter = 0
                for i in range(0,len(strs)-1):           
                    if strs[i][chr]== strs[i+1][chr]:
                        counter +=1
                    
                if counter == len(strs)-1:
                    result += strs[i][chr]
                else:
                    break
                chr +=1                

            return result
