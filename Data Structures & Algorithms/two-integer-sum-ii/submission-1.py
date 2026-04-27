class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPtr, rightPtr = 0, len(numbers) - 1

        while leftPtr < rightPtr:
            curSum = numbers[leftPtr] + numbers[rightPtr]
            if curSum > target:
                rightPtr -= 1
            elif curSum < target:
                leftPtr += 1
            else:
                # 
                return [leftPtr + 1, rightPtr + 1]
        
        return []