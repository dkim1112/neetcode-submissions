from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # answer list (list of sublists)
        ans = []

        # iterates through each string in entirety of strs
        for word in strs:
            placed = False
            
            # group represents each "sublist"
            # ans represents "list of sublist"
            for group in ans:
                # group[0] is the representative of each sublist
                if Counter(group[0]) == Counter(word):
                    group.append(word)
                    placed = True
                    break

            # reaching here means that none worked
            if not placed:
                # adding a new set of list into the lists
                ans.append([word])

        return ans

