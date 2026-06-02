# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newlist = ListNode()
        current = newlist
        if not list1:
            return list2
        if not list2:
            return list1
        if not list1 and not list2:
            return None
        while list1 or list2:
            if list1.val <= list2.val:
                current.val = list1.val
                if list1.next != None:
                    list1= list1.next
                else:
                    current.next = list2
                    break
            else:
                current.val = list2.val
                if list2.next != None:
                    list2 = list2.next
                else:
                    current.next = list1
                    break
            current.next = ListNode()
            current = current.next
        return newlist
