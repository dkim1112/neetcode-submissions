# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # by definition, the root node은 항상 goodNode

        # 현재까지 그 branch의 maxVal과 새로 비교하게 된 node와 비교해본다.
        def dfs(node, maxVal):
            if not node:
                return 0
            
            if node.val >= maxVal:
                res = 1
            else:
                res = 0

            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res

        return dfs(root, root.val) # at start, root.val would be the max
            
