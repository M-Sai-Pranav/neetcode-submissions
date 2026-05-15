

class Solution:  
    def same(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: 
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return (self.same(p.left, q.left) and self.same(p.right, q.right))
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        return (self.same(root, subRoot) or self.isSubtree(root.left, subRoot)
        or self.isSubtree(root.right, subRoot))
        