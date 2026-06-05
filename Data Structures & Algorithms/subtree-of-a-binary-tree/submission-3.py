# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root: # then there can't be a subtree
            return False

        # at each node of tree (root), check if this is starting point of subRoot
        # if so, check if they're identical from there via recursion
        if self.sameTree(root, subRoot):
            return True
        
        # DFS - recursively walk through every node in tree (root)
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    # previous problem
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
        else:
            return False
    