
class Solution:   
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        def dfs(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return (dfs(p.left, q.left) and dfs(p.right, q.right))
        return (dfs(root, subRoot)
        or self.isSubtree(root.left, subRoot)
        or self.isSubtree(root.right, subRoot))

        






