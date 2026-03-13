# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head

        move = head
        temp1 = None
        temp = None

        while move:
            temp1 = move.next
            move.next = temp
            temp = move
            move = temp1

        head = temp
        return head
