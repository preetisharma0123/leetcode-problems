"""Problem No.: 599
Problem:  Minimum Index Sum of Two Lists
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
Time Complexity:O(l1+l2)
l1: length of string1
L2: length of string2
Space Complexity: O(l1*x), hashmap size grows upto l1∗x, where x refers to average string length. string comparison takes x time.
"""
