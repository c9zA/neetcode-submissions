# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.sol = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.sol

    def dfs(self, root):
        if not root: return -1
        lh = self.dfs(root.left)
        rh = self.dfs(root.right)
        self.sol = max(self.sol, lh + rh +2)
        return max(lh, rh)+1
        