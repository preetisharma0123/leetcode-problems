"""Problem No.:705
Problem: Design a HashSet without using any built-in hash table libraries.
DS: LinkedList
Approach: LinkedList as Bucket
Explained: In the Python implementation, we employed a sort of pseudo head to keep a reference to the actual head of the LinkedList, which could simplify a bit the logic by reducing the number of branchings.
Date: 14/06/2023
"""

class Node:
    def __init__(self, val= None):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.array = [Node(0) for i in range(10001)]

    def add(self, key: int) -> None:
        i = self.hashfunction(key)
        curr = self.array[i]
        while curr.next:
            if curr.next.val == key:
                return 
            curr = curr.next
        curr.next = Node(key)

    def remove(self, key: int) -> None:
        i = self.hashfunction(key)
        curr = self.array[i]
        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        return
            

    def contains(self, key: int) -> bool:
        i = self.hashfunction(key)
        curr = self.array[i]
        while curr.next:
            if curr.next.val == key:
                return True
            curr = curr.next
        return False 

    def hashfunction(self,key):
        index = key%(len(self.array))
        return index 

# Time Complexity: O(N/K) where N is the number of all possible values and K is the number of predefined buckets, which is 769.
# Space Complexity: O(K+M) where K is the number of predefined buckets, and M is the number of unique values that have been inserted into the HashSet.



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
