# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def h(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max(self.h(root.left), self.h(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.h(root.left)
        right = self.h(root.right)
        return ((abs(left-right) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)) 