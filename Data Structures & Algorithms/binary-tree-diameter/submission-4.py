# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 # to be globally accessed

        # for each node during DFS...
        def dfs(node):

            if not node:
                return 0
            
            # recursively get left / right height
            left = dfs(node.left)
            right = dfs(node.right)

            # get diameter
            diameter = left + right

            # update answer with max diameter
            self.res = max(self.res, diameter)

            # return height
            return 1 + max(left, right)

        dfs(root)
        return self.res