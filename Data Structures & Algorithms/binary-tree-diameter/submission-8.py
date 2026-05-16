
class Solution:
    res = [0]
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        return 1+max(self.height(root.left), self.height(root.right))
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        curr = 2+left+right
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)
        return max(curr, left_diameter, right_diameter)
