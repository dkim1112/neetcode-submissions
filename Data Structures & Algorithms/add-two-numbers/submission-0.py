# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 그냥 result linkedlist의 맨 앞에 있는 놈
        temp = ListNode()
        cur = temp

        # carry is the leftover from previous calculation
        carry = 0

        while l1 or l2 or carry: # 뭐라도 하나 있으면 계속 진행
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry

            # since nodes are reversed anyways, when we add two number
            # saving sum % 10 to that new node, make sense, and
            # carry on the sum // 10
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # 위에 cur.next value에는 val을 넣어줬지만, 막상 cur 자체는 update 안해줬었음
            cur = cur.next 

            # update ptrs (move to right)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # 하나 다음부터가 real answer
        return temp.next