# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        length = len(arr)
        if length<3:
            return
        cur = arr[0]
        for i in range(1, ((length-1)>>1)+1):
            cur.next = arr[length-i]
            cur = cur.next
            cur.next = arr[i] 
            cur = cur.next
        if length%2==0:
            cur.next = arr[length>>1]
            cur = cur.next
        cur.next = None
   