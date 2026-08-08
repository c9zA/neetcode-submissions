# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def recurse(self, root, arr)->ListNode:
        if not root:
            return None
        
        root.next = self.recurse(root.next, arr)
        arr[0]-=1
        if arr[0]==0:
            return root.next
        return root
        
        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return self.recurse(head, [n])
        