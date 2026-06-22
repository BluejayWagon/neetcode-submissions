# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        cur = head
        nextNode = head.next
        prevNode = None
        while cur:
            cur.next = prevNode
            prevNode = cur
            cur = nextNode
            if not nextNode.next:
                break
            nextNode = nextNode.next
        cur.next = prevNode
        return cur