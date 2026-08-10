# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def dfsSerialize(self, arr, root):
        if root:
            arr.append(str(root.val))
            if root.left:
                self.dfsSerialize(arr, root.left)
            else:
                arr.append('n')
            if root.right:
                self.dfsSerialize(arr, root.right)
            else:
                arr.append('n')
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []
        if not root:
            return ""
        self.dfsSerialize(ans, root)
        print(ans)
        return ','.join(ans)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        arr = data.split(",")
        idx = 0
        def dfs(arr):
            nonlocal idx
            if arr[idx]!='n':
                r = TreeNode(int(arr[idx]))
                idx += 1
                if idx<len(arr) and arr[idx]!='n':
                    r.left = dfs(arr)
                idx += 1
                if idx<len(arr) and arr[idx]:
                    r.right = dfs(arr)
                return r
        return dfs(arr)
