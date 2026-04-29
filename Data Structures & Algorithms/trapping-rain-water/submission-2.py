class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)

        if length == 0:
            return 0

        leftMax = [0] * length
        rightMax = [0] * length

        leftMax[0] = height[0] # start from very left
        rightMax[length - 1] = height[length - 1] # start from very right

        for i in range (1, length):
            leftMax[i] = max(leftMax[i-1], height[i])
        for i in range (length - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        
        result = 0
        for i in range(length):
            result += min(leftMax[i], rightMax[i]) - height[i]

        return result