# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def recurseReorder(self, arr)->None:
        if len(arr)>1:
            arr[0].next = arr[-1]
            if len(arr)>2:
                arr[-1].next = arr[1]
            else:
                arr[-1].next = None
            self.recurseReorder(arr[1:-1])
        elif len(arr)==1:
            arr[0].next = None
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        self.recurseReorder(arr)

        
        