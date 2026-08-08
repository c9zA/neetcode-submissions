# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def carryFunc(self, sm):
        if sm>9:
            return sm%10, 1
        else:
            return sm%10, 0
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        cur = ans
        carry = 0
        while l1 or l2:
            if l1 and l2:
                sm, carry =self.carryFunc(l1.val+l2.val+carry)
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sm, carry = self.carryFunc(l1.val+carry)
                l1 = l1.next
            else:
                sm, carry = self.carryFunc(l2.val+carry)
                l2 = l2.next
            cur.next = ListNode(sm)
            cur = cur.next
        if carry==1:
            cur.next = ListNode(1)
        return ans.next
        