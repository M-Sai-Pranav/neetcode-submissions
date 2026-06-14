class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        if not curr1:
            return curr2
        if not curr2:
            return curr1 
        if curr1.val < curr2.val:
            tail = curr1
            curr1 = curr1.next 
        else:
            tail = curr2
            curr2 = curr2.next 
        head = tail
        while curr1 is not None and curr2 is not None:
            if curr1.val < curr2.val:
                tail.next = curr1
                curr1 = curr1.next 
            else:
                tail.next = curr2
                curr2 = curr2.next 
            tail = tail.next 
        if not curr1:
            tail.next = curr2
        if not curr2:
            tail.next = curr1
        return head