"""Problem No.: 202
Problem: Happy Number
DS:  Hash set/Linked list
Approach 1: Detect Cycles with a HashSet
Date: 17/07/2023
"""

class Solution:
          
    def digits_square(self, number):
        result = 0
    
        while (number/10) != 0:
            result += (number%10)**2
            number //=10
        return result

    def isHappy(self, number: int) -> bool:  
        set_resul  = set()
        while number !=1 and number not in set_resul:
            set_resul.add(number)
            number = self.digits_square(number)
        return number ==1




        
"""
Time Complexity:O(logn)
Space Complexity: O(logn)
"""
