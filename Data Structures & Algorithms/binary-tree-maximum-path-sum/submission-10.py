# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        if not root:
            return 0
        def path(root):
            if not root:
                return 0
            left = max(path(root.left),0)
            right = max(path(root.right),0)
            res[0] = max(res[0], root.val+left+right)
            return root.val+max(left, right)
        path(root)
        return res[0]