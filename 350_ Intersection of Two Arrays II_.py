"""Problem No.: 350
Problem:   Intersection of Two Arrays II
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
DS:  Hash set
Approach:Using HashMap
Date: 18/07/2023
"""
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = {}
        result = []
        min_sum = len(list1)+len(list2)-2
        
        for i in range(len(list1)):
            dict1[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in dict1:
                total = i +dict1[list2[i]]
                if total<min_sum:
                    min_sum = total
                    result.clear()
                    result.append( list2[i])
                elif min_sum == total:
                    result.append( list2[i])
        return result
        

"""
Time Complexity: O(n+m), where n and m are
arrays lengths. 
Space Complexity: 
"""        
