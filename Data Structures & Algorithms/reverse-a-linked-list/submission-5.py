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
        prevNode = head
        curNode = head.next
        nextNode = curNode.next
        curNode.next = prevNode
        prevNode.next = None
        while nextNode:
            prevNode = curNode
            curNode = nextNode
            nextNode = nextNode.next
            curNode.next = prevNode
        return curNode
