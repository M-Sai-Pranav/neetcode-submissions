

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            return 1+max(left, right)
        return (abs(dfs(root.left)-dfs(root.right)) <= 1 and 
        self.isBalanced(root.left) 
        and self.isBalanced(root.right))