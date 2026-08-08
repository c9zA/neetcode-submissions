# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def notEnough(self, root, k):
        for _ in range(k):
            if not root:
                return None, True
            root = root.next
        return root, False
    
    def recurse(self, n, k, ct):
        if ct==k:
            return n
        nh = self.recurse(n.next, k, ct+1)
        n.next.next = n
        n.next = None
        return nh

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1:
            return head
        dum = ListNode(0)
        curdum = dum
        cur = head
        while cur:
            tail, notEnough = self.notEnough(cur, k)
            if notEnough:
                break
            nh = self.recurse(cur, k, 1)
            curdum.next = nh
            curdum = cur
            cur = tail
        curdum.next = cur
        return dum.next

        