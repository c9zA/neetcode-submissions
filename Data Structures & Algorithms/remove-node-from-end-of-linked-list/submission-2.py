# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def recurse(self, root, n)->int:
        if not root.next:
            return 0
        count = self.recurse(root.next, n)
        count+=1
        if count==n:
            root.next = root.next.next
        return count
        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        h = ListNode()
        h.next = head
        self.recurse(h, n)
        return h.next

        