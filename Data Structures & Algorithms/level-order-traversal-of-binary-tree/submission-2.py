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
            for i in range(len(temp)):
                if temp[i].left:
                    queue.append(temp[i].left)
                if temp[i].right:
                    queue.append(temp[i].right)
                temp[i] = temp[i].val
            ans.append(temp)
        return ans
        