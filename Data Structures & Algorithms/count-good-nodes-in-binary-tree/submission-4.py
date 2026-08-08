# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)
    
    def dfs(self, root, mx)->int:
        mx = max(root.val, mx)
        ctl = self.dfs(root.left, mx) if root.left else 0
        ctr = self.dfs(root.right, mx) if root.right else 0
        return ctl+ctr+1 if root.val>=mx else ctl+ctr