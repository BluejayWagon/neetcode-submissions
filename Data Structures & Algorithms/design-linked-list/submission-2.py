class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.length = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if self.length == 0:
            return -1
        pointer = self.head.next
        while pointer and index > 0:
            print(pointer.val)
            pointer = pointer.next
            index -= 1
        if pointer and pointer != self.tail and index == 0:
            return pointer.val
        return -1



    def addAtHead(self, val: int) -> None:
        head = self.head
        nextPointer = head.next
        newNode = ListNode(val)
        newNode.prev = head
        newNode.next = nextPointer
        nextPointer.prev = newNode
        head.next = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        tail = self.tail
        prevPointer = tail.prev
        newNode = ListNode(val)
        newNode.prev = prevPointer
        newNode.next = tail
        prevPointer.next = newNode
        tail.prev = newNode
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        pointer = self.head
        while index >= 0:
            if pointer.next == None:
                return -1
            pointer = pointer.next
            index -= 1
        prevPointer = pointer.prev
        newNode = ListNode(val)
        pointer.prev = newNode
        prevPointer.next = newNode
        newNode.next = pointer
        newNode.prev = prevPointer
        self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index > self.length - 1:
            return
        pointer = self.head
        while index >= 0:
            if pointer.next == None:
                return -1
            pointer = pointer.next
            index -= 1
        pointer.next.prev = pointer.prev
        pointer.prev.next = pointer.next
        self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)