# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head.next == None:
            return head
        nextNode = head.next
        head.next = None
        prevNode = head
        head = nextNode
        while head:
            nextNode = head.next
            head.next = prevNode
            prevNode = head
            if nextNode == None:
                break
            head = nextNode
        return head
