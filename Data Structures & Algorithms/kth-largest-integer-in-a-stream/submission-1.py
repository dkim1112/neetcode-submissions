class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # to maintain k-th largest, only need to keep track of k largest elements seen so far
        # no need to save ALL
        # = Utilize "minheap" - always keeps smallest value at top = (kth largest)
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

        # when heap size is greater than k, remove smallest one to contain k
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # minHeap에다가 val 추가
        # when heap size is greater than k, remove smallest one to contain k
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
