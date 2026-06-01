# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        nextNode = head.next
        head.next = None
        previousNode = head
        while nextNode:
            head = nextNode
            nextNode = head.next
            head.next = previousNode
            previousNode = head
        return head