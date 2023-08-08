"""Problem No.: 164
Problem:   Maximum Gap
Approach: Radix sort 
Date:  08/08/2023
Detailed Problem: Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

 

Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
"""
class Solution:
    def maximumGap(self, nums: List[int]) -> int:

        if len(nums)<=1:
            return 0

              
        # radix sort
        max_element = max(nums)
        place_val = 1

        while place_val<= max_element:
            
            #counting sort
            
            counts = [0]*10
            for elem in nums:
                digit = (elem//place_val)%10
                counts[digit] += 1
            
            starting_index = 0
            for i, count in enumerate(counts):
                counts[i] = starting_index
                starting_index += count

            sorted_lst = [0] * len(nums)
            for elem in nums:
                digit = (elem // place_val) % 10
                sorted_lst[counts[digit]] = elem
                counts[digit] += 1

            for i in range(len(nums)):
                nums[i] = sorted_lst[i]

            place_val *=10

        max_gap =0
        for i in range(1,len(nums)):
            curr_gap =nums[i]-nums[i-1]
            max_gap = max(curr_gap,max_gap)
                
        return max_gap

        
"""
Time Complexity: O(d⋅(n+k))≈O(n)
Since a linear iteration over the array (once it is sorted) is of linear (i.e. O(n) complexity, the performance of this approach is limited by the performance of Radix sort.
Space Complexity: O(n+k)≈O(n) extra space.
Counting sort requires O(k) extra space. Radix sort requires an auxiliary array of the same size as input array. However given that kkk is a small fixed constant, the space required by Counting sort can be ignored for reasonably large input.


"""
