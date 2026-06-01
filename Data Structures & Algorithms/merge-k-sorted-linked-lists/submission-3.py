# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Search through all lists to find the list whose current node has the smallest value.
        # If no list has remaining nodes (all are empty), stop.
        res = ListNode(0)
        cur = res

        while True:
            minNode = -1

            # finding the min (iterates through all values)
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if minNode == -1 or lists[minNode].val > lists[i].val:
                    minNode = i

            if minNode == -1: # means traversal is over
                break
            
            # after min is found
            cur.next = lists[minNode]
            # since it is singly linked, only need to care about .next (not .prev)
            lists[minNode] = lists[minNode].next
            cur = cur.next

        # we created res as dummy, so res.next부터가 values
        return res.next
