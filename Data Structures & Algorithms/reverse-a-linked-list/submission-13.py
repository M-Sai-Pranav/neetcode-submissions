

class Solution:
    def reverseList(self, head: Optional[ListNode], prev = None) -> Optional[ListNode]:
        curr = head 
        if curr is None:
            return prev
        next = curr.next
        curr.next = prev 
        return self.reverseList(next, head)