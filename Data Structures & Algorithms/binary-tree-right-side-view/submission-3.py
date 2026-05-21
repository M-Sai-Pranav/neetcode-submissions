

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []
        q = deque([root])
        while q:
            level = len(q)
            for i in range(level):
                node = q.popleft()
                if i == (level-1):
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res