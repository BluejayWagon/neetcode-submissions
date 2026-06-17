class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class MinStack:

    def __init__(self):
        self.headPointer = ListNode(0)
        self.tailPointer = ListNode(0)
        self.headPointer.next = self.tailPointer
        self.tailPointer.prev = self.headPointer
        self.Length = 0
        self.Min = [2 ** 31]

    def push(self, val: int) -> None:
        head = self.headPointer
        nextPointer = head.next
        newNode = ListNode(val)
        head.next = newNode
        newNode.next = nextPointer
        newNode.prev = head
        nextPointer.prev = newNode
        if val <= self.Min[-1]:
            self.Min.append(val)
        

    def pop(self) -> None:
        val = self.headPointer.next.val
        if val == self.Min[-1]:
            self.Min.pop()
        head = self.headPointer
        newNext = head.next.next
        newNext.prev = head
        head.next = newNext

    def top(self) -> int:
        node = self.headPointer.next
        return node.val

    def getMin(self) -> int:
        return self.Min[-1]

        
