# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans, _ = self.dfs(root)
        return ans
    
    def dfs(self, root):
        if not root:
            return True, -1
        if not root.left and not root.right:
            return True, 0
        lb, lh = self.dfs(root.left)
        if not lb:
            return False, 0
        rb, rh = self.dfs(root.right)
        if not rb:
            return False, 0
        return abs(lh-rh)<=1, max(lh,rh)+1