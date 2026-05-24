# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return False
        
        # notice the pattern:
        # 1. after splitting middle,
        # 2. reverse second half,
        # 3. and take each node from first/second one by one = MERGE
        
        # Find mid node
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half
        second = slow.next
        slow.next = None # first element of second half's next = None --> becomes tail

        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        second = prev

        # Merge two
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        