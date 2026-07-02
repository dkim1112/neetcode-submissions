class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        # hashmap
        digitToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "qprs",
            "8" : "tuv",
            "9" : "wxyz",
        }

        # recursion
        def backtrack(i, curStr): # 보통 idx 함께 써줌
            # condition to append to res & return
            # = one backtrack cycle
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            # recursion
            for c in digitToChar[digits[i]]:
                backtrack(i+1, curStr + c)
        
        if digits:
            backtrack(0, "")

        return res