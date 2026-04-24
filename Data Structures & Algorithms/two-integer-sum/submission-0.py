class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key-value
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                # return i, j pair, as long as i != j
                return [hashmap[complement], i]
            else:
                hashmap[nums[i]] = i # 이 value는 이 idx를 갖고 있어~ 전해줌.