# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]

    def dfs(self, root):
        ans = True
        mn, mx = root.val, root.val
        if root.left:
            b, n, m = self.dfs(root.left)
            mx = max(mx, m, root.val)
            mn = min(mn, n, root.val)
            ans = root.val>m and b and root.val>n
        if root.right:
            b, n, m = self.dfs(root.right)
            mn = min(mn, n, root.val)
            mx = max(mx, m, root.val)
            ans = b and root.val<n and ans and root.val<m
        return ans, mn, mx
        