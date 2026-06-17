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
        if index > self.length - 1:
            return -1
        pointer = self.headPointer.next
        if index == 0:
            return pointer
        for i in range(index):
            pointer = pointer.next
        return pointer.val

    def addAtHead(self, val: int) -> None:
        pointer = self.headPointer
        nextNode = pointer.next
        newNode = ListNode(val)
        newNode.next = nextNode
        newNode.prev = pointer
        pointer.next = newNode
        nextNode.prev = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        pointer = self.tailPointer
        prevNode = pointer.prev
        newNode = ListNode(val)
        newNode.next = pointer
        newNode.prev = prevNode
        pointer.prev = newNode
        prevNode.next = newNode
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        if index == self.length:
            self.addAtTail(val)
            return
        pointer = self.headPointer.next
        if index == 0:
            addAtHead(val)
        else:
            for i in range(index):
                pointer = pointer.next
            prevNode = pointer.prev
            newNode = ListNode(val)
            newNode.next = pointer
            newNode.prev = prevNode
            pointer.prev = newNode
            prevNode.next = newNode
            self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        if index > self.length - 1:
            return
        pointer = self.headPointer.next
        for i in range(index):
            pointer = pointer.next
        prevPointer = pointer.prev
        nextPointer = pointer.next
        prevPointer.next = nextPointer
        nextPointer.prev = prevPointer
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)