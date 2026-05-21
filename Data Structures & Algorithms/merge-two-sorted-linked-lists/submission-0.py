# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # after comparing two values, whichever is smaller should appear first in merged list
        # 1. choose smaller node
        # 2. recursively merge rest of list
        # 3. attach result to chosen node

        if list1.val <= list2.val:
            # we know list1 value comes first, since its smaller.
            # now, determine what comes after THAT.
            list1.next = self.mergeTwoLists(list1.next, list2)
            # returns the head
            return list1
        else: # list2.val < list1.val
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2