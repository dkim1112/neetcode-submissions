# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # every node must swap its left/right children
        # via BFS - we traverse tree by level, starting from the root

        if not root:
            return None
        
        queue = deque([root])
        while queue:
            # get one node
            node = queue.popleft()
            
            # swap its children (left/right)
            node.left, node.right = node.right, node.left # swapping

            # push (new) left/right children to queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root