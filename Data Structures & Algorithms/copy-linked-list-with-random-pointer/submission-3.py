"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hmap = {}
        cur = head
        while cur:
            hmap[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                hmap[cur].next = hmap[cur.next]
            if cur.random:
                hmap[cur].random = hmap[cur.random]
            cur = cur.next
        return hmap[head] if head else None

        
