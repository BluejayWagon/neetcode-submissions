# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = None
        current = head
        nextNode = head.next
        while current:
            current.next = prev
            prev = current
            current = nextNode
            if nextNode:
                nextNode = nextNode.next
        return prev
        