# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        arr[-n] = 0
        if arr[0]==0:
            return arr[1] if len(arr)>1 else None
        arr[-n-1].next = arr[-n+1] if 1-n<0 else None
        return arr[0]