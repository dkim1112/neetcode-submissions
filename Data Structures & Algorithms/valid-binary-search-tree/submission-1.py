# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # level마다 check해야함 --> BFS --> use queue
        # = "checking if its valid B"
    
        if not root:
            return True
        
        # push (root, -inf, inf) into queue
        queue = deque([(root, float("-inf"), float("inf"))])

        while queue:
            # pop (node, leftbound, rightbound)
            node, left, right = queue.popleft()
            if not (left < node.val < right):
                return False
            
            # when moving left -> current node's value = max allowed value
            if node.left:
                queue.append((node.left, left, node.val))
            # when moving right -> current node's value = min allowed value 
            if node.right:
                queue.append((node.right, node.val, right))
            
        # if while has passed
        return True