class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sortArr = sorted(nums)

        for i in range(len(sortArr) - 2):
            if i > 0 and sortArr[i] == sortArr[i-1]:
                continue # move to next i

            currTarget = 0 - sortArr[i]
            leftPtr = i + 1
            rightPtr = len(sortArr) - 1

            while leftPtr < rightPtr:
                currSum = sortArr[leftPtr] + sortArr[rightPtr]
                if currSum > currTarget:
                    rightPtr -= 1
                elif currSum < currTarget:
                    leftPtr += 1
                else:
                    ans.append([sortArr[leftPtr], sortArr[rightPtr], sortArr[i]])
                    # this is to prevent from infinite loop
                    leftPtr += 1
                    rightPtr -= 1

                    # check duplicates (within sortArr) b/c 있으면 하나더 옮겨야 no duplicate sol.
                    while leftPtr < rightPtr and sortArr[leftPtr] == sortArr[leftPtr - 1]:
                        leftPtr += 1
                    while leftPtr < rightPtr and sortArr[rightPtr] == sortArr[rightPtr + 1]:
                        rightPtr -= 1
        return ans