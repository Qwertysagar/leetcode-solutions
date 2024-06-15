from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        rotations = k % length
        if rotations == 0:
            return head
        for i in range(rotations):
            temp = head
            while temp.next.next != None:
                temp = temp.next
            end = temp.next
            temp.next = None
            end.next = head
            head = end
        return head
