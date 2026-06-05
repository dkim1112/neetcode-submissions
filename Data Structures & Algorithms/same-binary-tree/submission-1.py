# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # via DFS, check if "identical"
        # identical condition: same structure, same node value
        
        # always check for non-existing case
        if not p and not q:
            return True
        
        # same structure (p and q are 2 separate trees) and node values
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False