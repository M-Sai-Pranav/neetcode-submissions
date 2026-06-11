

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1 = list1
        curr_2 = list2
        if  curr_1 is None:
            return curr_2
        if curr_2 is None:
            return curr_1
        if curr_2 is None:
            return None 
        if curr_1.val < curr_2.val:
            tail = curr_1
            curr_1 = curr_1.next
        else:
            tail = curr_2
            curr_2 = curr_2.next 
        head = tail
        while curr_1 is not None and curr_2 is not None:
            if curr_1.val < curr_2.val:
                tail.next = curr_1
                curr_1 = curr_1.next 
            else:
                tail.next = curr_2
                curr_2 = curr_2.next 
            tail = tail.next 
        if curr_1 is not None:
            tail.next = curr_1
        if curr_2 is not None:
            tail.next = curr_2 
        return head 