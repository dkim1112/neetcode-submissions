class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # use max-heap to store [nodes: (value, index)], for all elements we get
        # push - heapq.heappush(heap, (-value, index))
        # pop (automatically the smallest or largest)- heapq.heappop(heap)

        heap = []
        res = []

        for i in range(len(nums)):
            # expand window by inserting element into heap
            heapq.heappush(heap, (-nums[i], i))

            # when window size = k is reached,
            if i >= k - 1:
                # when idx < current window left boundary
                while heap[0][1] < i - k + 1:
                    heapq.heappop(heap) # remove element outside window

                # top of heap is max for that window --> add that to result list
                res.append(-heap[0][0])
        return res