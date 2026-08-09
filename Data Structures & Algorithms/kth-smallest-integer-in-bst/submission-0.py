# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.dfs(root, k, [0])
    
    def dfs(self, root, k, ct):
        ans = -1
        if root.left:
            ans = self.dfs(root.left, k, ct)
        if ans>-1:
            return ans
        ct[0]+=1
        if ct[0]==k:
            return root.val
        if root.right:
            ans = self.dfs(root.right, k, ct)
        return ans
        