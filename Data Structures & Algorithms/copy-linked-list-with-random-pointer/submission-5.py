"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def recurse(self, head, hmap):
        if not head:
            return None
        hmap[head] = Node(head.val)
        hmap[head].next = self.recurse(head.next, hmap)
        if head.random:
            hmap[head].random = hmap[head.random]
        return hmap[head]
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ans = Node(0)
        hmap = {}
        ans.next = self.recurse(head, hmap)
        return ans.next
