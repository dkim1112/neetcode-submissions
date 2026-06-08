# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        visited = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            length = len(queue)
            for n in range(length):
                node = queue.popleft()

                # last node of this level
                if n == length - 1:
                    visited.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return visited

        