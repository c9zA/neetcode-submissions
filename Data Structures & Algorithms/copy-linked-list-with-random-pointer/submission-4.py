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
        hmap = collections.defaultdict(lambda: Node(0))
        cur = head
        while cur:
            hmap[cur].val = cur.val
            if cur.next:
                hmap[cur].next = hmap[cur.next]
            if cur.random:
                hmap[cur].random = hmap[cur.random]
            cur = cur.next
        return hmap[head] if head else None

        
