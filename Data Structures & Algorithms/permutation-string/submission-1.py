class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # char freq count of (substring of s2 with same length as s1) == char freq count of (s1) ??
        # if the two arrays (one for s1 and one for s2 match => return True)
        
        # FIXED WINDOW APPROACH
        # increment window forward by 1 & update count by removing left and adding right
        # "char freq count" is KEY! (A는 몇번, B는 몇번, etc.)

        # edge case
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0]*26, [0]*26

        # initalize first window
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # how many letters currently match in frequency b/w s1 and s2.
        matches = 0
        for i in range(26): # bc 26 alphabets
            if s1Count[i] == s2Count[i]:
                matches += 1

        l = 0
        # sliding window starts
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
                
            # add char to right
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
