

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            return (bst(node.left, left, node.val) and 
            bst(node.right, node.val, right))
        return bst(root, float("-inf"), float("+inf"))