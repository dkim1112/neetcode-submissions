# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # use dummy node that points to head (used for traversal at end)
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # for each "section" of k,
            # find kth node for current group.
            kth = self.getKth(groupPrev, k)

            # if kth is null, fewer than k nodes left -> break
            if not kth:
                break
            groupNext = kth.next # next set of groups grouped in size k

            # reverse those nodes
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            # reconnect and move onto next group
            nxt = groupPrev.next
            groupPrev.next = kth
            groupPrev = nxt
    
        return dummy.next # entire list

    # use helper method to get kth node from groupPrev
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr