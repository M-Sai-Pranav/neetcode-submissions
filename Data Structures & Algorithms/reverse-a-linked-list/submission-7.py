# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head, prev=None):
        if head is None:
            return prev 
        next = head.next
        head.next = prev 
        return self.reverseList(next, head)
        