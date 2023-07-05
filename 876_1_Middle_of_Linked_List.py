""""
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node."""

#Brute-force approach-1


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 1

        while curr.next:
            curr = curr.next
            count+=1

        curr = head
        if count%2 == 0:
            for count in range(count,(count//2),-1):
                curr = curr.next
                
            
        else:
            for count in range(count,(count//2)+1,-1):
                curr = curr.next
                
        
        head = curr
        return head









 
