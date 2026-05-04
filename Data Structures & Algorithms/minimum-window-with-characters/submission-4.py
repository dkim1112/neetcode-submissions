class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # we want smallest window in "s", containing all char of "t"
        # 1. expand window w/ right pointer - adding char to window
        # 2. once we covered all required char, w/ left pointer - remove char from window
        # 3. we try to minimize it while it's still valid.

        # build freqency map for t
        countT, window = {}, {}
        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1
        # if t = "AABC" --> countT = {A:2, B:1, C:1}
        

        have, need = 0, len(countT)
        res = [-1, -1]
        resLen = float('inf')
        
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                have += 1
            
            # have == need means we got all char needed somehow
            while have == need:
                if r - l + 1 < resLen: # if shorter than current min
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        if resLen != float('inf'):
            # means it has new min
            return s[l : r + 1]
        else:
            return ""