class Solutions:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Do bfs and count the levels
        queue = deque()
        levels = 0
        if root:
            queue.append((root, 1))

        while queue:
            currNode, level = queue.pop()
            if currNode.right:
                queue.append((currNode.right, level+1))
            if currNode.left:
                queue.append((currNode.left, level+1))
            levels = max(level, levels)
        return levels