# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, root, mn, mx):
        ans = True
        if root.left:
            ans = ans and self.dfs(root.left, mn, root.val)
        if root.right:
            ans = ans and self.dfs(root.right, root.val, mx)
        return ans and mn<root.val and root.val<mx
        
        