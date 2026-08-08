# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def recurse(self, root,n, countArr)->ListNode:
        if not root.next:
            countArr[0] = 0
            return None
        ans = self.recurse(root.next, n, countArr)
        if countArr[0]!=-1:
            countArr[0] += 1
        if countArr[0]==n:
            return root
        return ans
        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        h = ListNode()
        h.next = head
        node = self.recurse(h, n, [-1])
        node.next = node.next.next
        return h.next

        