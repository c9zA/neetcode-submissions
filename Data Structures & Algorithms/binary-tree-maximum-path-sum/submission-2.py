# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[1]
    
    def dfs(self, root):
        if not root:
            return float('-inf'), float('-inf')
        reuse = root.val
        ans = root.val
        rel, ansl = self.dfs(root.left)
        rer, ansr = self.dfs(root.right)
        reuse = max(reuse, reuse+rel, reuse+rer)
        ans = max(ans, rel+rer+root.val, ansl, ansr, reuse)
        return reuse, ans