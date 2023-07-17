"""Problem No.:349
Problem: 349. Intersection of Two Arrays. Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 
DS: Array/set
Approach: To solve the problem in linear time, let's use the structure set,
which provides in/contains operation in O(1)\mathcal{O}(1)O(1) time in
average case.

The idea is to convert both arrays into sets, and then iterate over
the smallest set checking the presence of each element in the larger set.
Date: 15/06/2023
"""

class Solution:
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]
        
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """  
        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)
"""
Time Complexity: O(n+m), where n and m are
arrays lengths. O(n) time is used to convert nums1
into set, O(m) time is used to convert nums2, and
contains/in operations are O(1) in the average case.\


Space Complexity: O(n+m) in the worst case when
all elements in the arrays are different.


"""
