"""
1474. Delete N Nodes After M Nodes of a Linked List
You are given the head of a linked list and two integers m and n.

Traverse the linked list and remove some nodes in the following way:

Start with the head as the current node.
Keep the first m nodes starting with the current node.
Remove the next n nodes
Keep repeating steps 2 and 3 until you reach the end of the list.
Return the head of the modified list after removing the mentioned nodes.

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        prev,curr = head,head
        
        while curr:
            slow, fast = m,n

            # traverse m nodes
            while slow>1 and curr:
                prev = curr.next
                curr = curr.next
                slow -=1

            # traverse n nodes
            while fast>-1 and curr:
                curr = curr.next
                fast -=1

            # delete n nodes
            if prev:
                prev.next = curr
                prev = curr
               
        return head
