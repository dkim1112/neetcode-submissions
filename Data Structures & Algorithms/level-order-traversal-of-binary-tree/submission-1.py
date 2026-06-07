# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # BFS processes nodes in order they appear using queue
        visited = []

        # make queue
        queue = collections.deque()
        queue.append(root)

        while queue:
            length = len(queue)
            level = []
            
            # remove nodes from queue and add that to visited (at that level)
            # add children of the removed node to queue
            for n in range(length):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left) # we need to add smth - for while to continue next round
                    queue.append(node.right) # we need to add smth - for while to continue next round
            
            # if level exists = has some value -> add that to visited as a list
            if level:
                visited.append(level)

        return visited