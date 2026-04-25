class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        # sort by frequency
        # dictionary doesn't used sort(), instead used sorted()
        # dictionary's value can be accessed via dot operator
        # backward traversal to get highest to lowest
        arr = sorted(freq.items(), key=lambda x: x[1], reverse = True)
        
        result = []

        for i in range(k):
            # just want the number, not freq.
            result.append(arr[i][0])

        return result