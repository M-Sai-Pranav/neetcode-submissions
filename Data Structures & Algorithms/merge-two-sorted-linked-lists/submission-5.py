

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2 

        if curr1 is None:
            return curr2
        if curr2 is None:
            return curr1
        if curr1 is None and curr2 is None:
            return []
        
        if curr1.val < curr2.val:
            tail = curr1
            curr1 = curr1.next 
        else:
            tail = curr2
            curr2 = curr2.next 
        head = tail 
        while curr1 and curr2:
            if curr1.val < curr2.val:
                tail.next = curr1
                curr1 = curr1.next 
            else:
                tail.next = curr2 
                curr2 = curr2.next 
            tail = tail.next 
        if curr1 is not None:
            tail.next = curr1
        if curr2 is not None:
            tail.next = curr2
        return head 
