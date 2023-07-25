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
        self.array = {}
        

    def add(self, number: int) -> None:
        #Given a desired sum value S, for each number a, we just need to verify if there exists a complement number (S-a) in the table. 
        #we build a frequency hashtable with the number as key and the frequency of the number as the value in the table.
        if number in self.array.keys():
            self.array[number] +=1
        else:
            self.array[number] = 1

    def find(self, value: int) -> bool:
                             
        for key in self.array.keys(): # in order to iterate over keys
            comp = value - key
            if  key != comp:
                if comp in self.array :
                    return True
            else:
                if self.array[comp]>1:
                    return True

        return False


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
