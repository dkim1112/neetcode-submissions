# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # hashset: when need to store unique elements and require fast lookups
        
        # To see if it has a cycle, need to know if we ever reach a node we've already seen.
        # => Thus, let's store every node we visit.

        seen = set()
        curr = head

        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next # move onto next value
        
        # if while failed to return smth
        return False