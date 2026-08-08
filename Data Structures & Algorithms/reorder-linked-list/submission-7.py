# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def recurseReorder(self, root, cur)->ListNode:
        if not cur:
            return root
        root = self.recurseReorder(root, cur.next)
        if not root:
            return
        if root==cur or root.next==cur:
            cur.next = None
        else:
            temp = root.next
            root.next = cur
            cur.next = temp
        return cur.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        self.recurseReorder(head, head.next)
