# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        originalHead = head
        nextNode = head.next
        prev = None
        while head:
            head.next = prev
            prev = head
            head = nextNode
            head = nextNode
            if nextNode:
                nextNode = nextNode.next
        return prev
            