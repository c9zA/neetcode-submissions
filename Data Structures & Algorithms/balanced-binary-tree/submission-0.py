# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[1]
    
    def dfs(self, root):
        if not root: return -1, True
        lh, lb = self.dfs(root.left)
        rh, rb = self.dfs(root.right)
        return max(lh, rh)+1, abs(lh - rh) <= 1 and lb and rb