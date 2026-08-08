# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            temp = []
            while queue:
                n = queue.popleft()
                temp.append(n)
            for n in temp:
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            for i in range(len(temp)):
                temp[i] = temp[i].val
            ans.append(temp)
        return ans
        