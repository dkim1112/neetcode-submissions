# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # using pointers, flip them one at a time
        # redirect its next pointer to the one behind it, instead.

        prev = None # node that should come after curr, once reversed
        curr = head # node we currently process

        while curr:
            temp = curr.next # original next node (before reverse)
            curr.next = prev
            prev = curr

            # this bit moves curr -> temp, (which is curr.next) every iteration.
            # once it reaches end, while ends, it exists.
            curr = temp

        return prev
