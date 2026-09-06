"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hmap = {}
        if not node:
            return
        root = Node(node.val)
        hmap[1] = root
        def dfs(par, cppar):
            for n in par.neighbors:
                if n.val not in hmap:
                    hmap[n.val] = Node(n.val)
                    dfs(n, hmap[n.val])
                cppar.neighbors.append(hmap[n.val])
        dfs(node, root)
        return root