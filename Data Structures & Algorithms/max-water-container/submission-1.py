class Solution:
    def maxArea(self, heights: List[int]) -> int:
        answer = 0
        l, r = 0, len(heights)-1

        while l < r:
            curr_sum = min(heights[l], heights[r]) * (r - l)

            if heights[l] >= heights[r]:
                r -= 1
            if heights[l] < heights[r]:
                l += 1
            
            if curr_sum > answer:
                answer = curr_sum

        return answer