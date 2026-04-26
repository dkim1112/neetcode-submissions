class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        length = 0

        for num in hashset:
            # to assure that it is the MAX of potential sequence
            if num + 1 not in hashset: # 얘보다 딱 하나만 더 큰 숫자는 없는지 확인
                count = 1
                curr = num - 1

                while curr in hashset:
                    count += 1
                    curr -= 1
            
                length = max(count, length)

        return length