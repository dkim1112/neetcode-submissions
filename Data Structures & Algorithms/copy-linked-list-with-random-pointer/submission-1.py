"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # want to create a copy linked list, where each node has pointer "next" and "random"

        # a dictionary that maps original node to copied node
        # key: actual Node objects, not values
        oldToCopy = {None: None}

        # 1st round: create copy of node (of just the values).
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy # this creates a map of oldNode -> newNode
            cur = cur.next # move onto next one
        
        # 2nd round: connect next and random pointers for each copied node
        cur = head
        while cur:
            copy = oldToCopy[cur] # at first iteration, this is head of newNode
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next # move onto next one
        
        return oldToCopy[head]