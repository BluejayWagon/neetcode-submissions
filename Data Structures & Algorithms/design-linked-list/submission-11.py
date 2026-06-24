class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.headPointer = ListNode(0)
        self.tailPointer = ListNode(0)
        self.headPointer.next = self.tailPointer
        self.tailPointer.prev = self.headPointer
        self.length = 0
        
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        pointer = self.headPointer.next
        for i in range(index):
            pointer = pointer.next
        return pointer.val

    def addAtHead(self, val: int) -> None:
        oldHead = self.headPointer.next
        newHead = ListNode(val)
        newHead.next = oldHead
        newHead.prev = self.headPointer
        self.headPointer.next = newHead
        oldHead.prev = newHead
        self.length += 1

    def addAtTail(self, val: int) -> None:
        oldTail = self.tailPointer.prev
        newTail = ListNode(val)
        newTail.next = self.tailPointer
        newTail.prev = oldTail
        self.tailPointer.prev = newTail
        oldTail.next = newTail
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.length:
            self.addAtTail(val)
            return
        if index < self.length:
            pointer = self.headPointer.next
            for i in range(index):
                pointer = pointer.next
            prevPointer = pointer.prev
            newNode = ListNode(val)
            prevPointer.next = newNode
            newNode.prev = prevPointer
            newNode.next = pointer
            pointer.prev = newNode
            self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < self.length:
            pointer = self.headPointer.next
            for i in range(index):
                pointer = pointer.next
            nextNode = pointer.next
            prevNode = pointer.prev
            nextNode.prev = prevNode
            prevNode.next = nextNode
            self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)