# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val] # to start with

        # perform DFS
        def dfs(root):
            if not root:
                return 0
            
            # we have 3 path we can consider
            # for either, we need left / right subtree values
            leftDir = max(dfs(root.left), 0)
            rightDir = max(dfs(root.right), 0)
          
            # best path "THROUGH" nodes => left node -> curr node -> right node
            res[0] = max(res[0], root.val + leftDir + rightDir)

            # return "DOWNWARD" path
            return root.val + max(leftDir, rightDir)
            
        
        dfs(root)
        return res[0]
