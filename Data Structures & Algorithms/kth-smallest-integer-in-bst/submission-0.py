# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # utilizing the traits of BST (left < current < right)
        # run through DFS and save nodes in this order into array (= automatically sorted)
        # = we call this "inorder traversal"
        
        res = []
            
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root) # start from root
        return res[k-1]

