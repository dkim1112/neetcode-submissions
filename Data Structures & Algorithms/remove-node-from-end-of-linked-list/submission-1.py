# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # linked list - nodes connected via .next
        # to skip a node, do .next.next

        dummy = ListNode(0, head) 

        # we make a copy of dummy as left
        # b/c we need the "dummy" to be used to 
        # traverse from start of head after deleting is done (last line)
        left = dummy # one BEFORE head (= start of Linked List)
        right = head

        for _ in range(n):
            right = right.next
        
        while right: # until right reaches end of list (that is, one AFTER the last node (= None))
            left = left.next
            right = right.next

        # when right reached end
        left.next = left.next.next # skip that one node

        return dummy.next
