# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def move(self, nodeToMove, k, end):
        c = nodeToMove
        for _ in range(k):
            c = c.next
        temp = c.next
        c.next = nodeToMove
        nodeToMove.next = temp

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        n = 1
        end = head
        while end.next:
            n+=1
            end = end.next
        for _ in range((n-1)>>1):
            end.next = head.next
            head.next = head.next.next
            end.next.next = None
            end = end.next
        cur = head.next
        for i in range(n>>1, 1, -1):
            head.next = head.next.next
            self.move(cur, (i-1)*2, end)
            cur = head.next

        


        