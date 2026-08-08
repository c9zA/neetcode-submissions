# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, prev, cur):
        if not cur:
            return prev
        temp = cur.next
        cur.next = prev
        return self.reverse(cur, temp)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        temp = head.next
        head.next = None
        return self.reverse(head, temp)
    