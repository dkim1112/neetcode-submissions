class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        a = sorted(nums)

        for i in range(len(a) - 2):
            # duplicate check (연속으로 same i => same currTarget)
            if i > 0 and a[i] == a[i-1]:
                continue # move to next i

            currTarget = 0 - a[i]
            l = i + 1
            r = len(a) - 1

            while l < r:
                currSum = a[l] + a[r]
                if currSum > currTarget:
                    r -= 1
                elif currSum < currTarget:
                    l += 1
                else:
                    ans.append([a[l], a[r], a[i]])
                    # this is to prevent from infinite loop
                    l += 1
                    r -= 1

                    # check duplicates (within sortArr) b/c 있으면 하나더 옮겨야 no duplicate sol.
                    while l < r and a[l] == a[l - 1]:
                        l += 1
                    while l < l and a[r] == a[r + 1]:
                        r -= 1
        return ans