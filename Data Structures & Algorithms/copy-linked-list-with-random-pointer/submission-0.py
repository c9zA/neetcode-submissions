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
        cur = head
        newHead = Node(0)
        newCur = newHead
        idx = 0
        oldMap = {}
        newMap = {}
        while cur:
            newCur.next = Node(cur.val)
            newCur = newCur.next
            oldMap[cur] = idx
            newMap[idx] = newCur
            idx+=1            
            cur = cur.next
        cur = head
        newCur = newHead.next
        while cur:
            if cur.random:
                randIdx = oldMap[cur.random]
                newCur.random = newMap[randIdx]
            cur = cur.next
            newCur = newCur.next
        return newHead.next

        
