"""Problem No.: 170
Problem:  Two Sum III - Data structure design
DS:  Sprting, 2 pointer
Approach:
Date:  24/07/2023
Detailed Problem: Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.
 

Example 1:

Input
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
Output
[null, null, null, null, true, false]

Explanation
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --> [1]
twoSum.add(3);   // [1] --> [1,3]
twoSum.add(5);   // [1,3] --> [1,3,5]
twoSum.find(4);  // 1 + 3 = 4, return true
twoSum.find(7);  // No two integers sum up to 7, return false
"""
class TwoSum:

    def __init__(self):
        self.array = []
        self.is_sorted = False

    def add(self, number: int) -> None:
        self.array.append(number)
        self.is_sorted = False

    def find(self, value: int) -> bool:
        if not self.is_sorted:
            self.array.sort()
            self.is_sorted = True
                     
        length = len(self.array)
        low, high = 0,length-1
    
        while low < high:
            total = self.array[low] + self.array[high] 
            if total == value:
                return True
            elif total<value:
                low+=1
            else:
                high -=1
        return False


"""
Time Complexity: O(N⋅log⁡(N))
Space Complexity: O(n)
"""
