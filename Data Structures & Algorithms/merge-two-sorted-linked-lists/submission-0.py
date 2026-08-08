# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        ans = ListNode()
        a1 = ans
        while l1 and l2:
            if l1.val<l2.val:
                a1.next = l1
                l1 = l1.next
            else:
                a1.next = l2
                l2 = l2.next
            a1 = a1.next
        while l1:
            a1.next = l1
            l1 = l1.next
            a1 = a1.next
        while l2:
            a1.next = l2
            l2 = l2.next
            a1 = a1.next
        ans = ans.next
        return ans
      