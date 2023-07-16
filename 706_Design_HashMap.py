"""
706. Design HashMap
Approach: We organize the storage space as an array where each element is indexed with the output value of the hash function.
In case of collision, where two different keys are mapped to the same address, we use a bucket to hold all the values. The bucket is a container that hold all the values that are assigned by the hash function. We could use either a LinkedList or an Array to implement the bucket data structure.

"""
class Node:
    def __init__(self, key = None, val = None, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.array = [Node(0) for i in range(2069)]

    def hash_func(self,key):
        return key%(len(self.array))        

    def put(self, key: int, value: int) -> None:
        index = self.hash_func(key)
        curr = self.array[index]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = Node(key,value)

    def get(self, key: int) -> int:
        index = self.hash_func(key)
        curr = self.array[index]
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1


    def remove(self, key: int) -> None:
        index = self.hash_func(key)
        curr = self.array[index]
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

"""
Time Complexity: O(N/K) - where N is the number of all possible keys and K is the number of predefined buckets in the hashmap, which is 2069 in our case.
Space Complexity: O(k+M) - where K is the number of predefined buckets in the hashmap and M is the number of unique keys that have been inserted into the hashmap.
        



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
