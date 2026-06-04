class ListNode:
    def __init__(self, val: str):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode('head')
        self.tail = ListNode('tail')
        self.cur = ListNode(homepage)
        self.head.next = self.cur
        self.tail.prev = self.cur
        self.cur.next = self.tail
        self.cur.prev = self.head

    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        newNode.prev = self.cur
        newNode.next = self.tail
        self.cur.next = newNode
        self.tail.prev = newNode
        self.cur = newNode
        

    def back(self, steps: int) -> str:
        current = self.cur
        while current and steps > 0:
            current = current.prev
            steps -= 1
        if current == None or current.val == 'head':
            self.cur = self.head.next
            return self.cur.val
        else:
            self.cur = current
            return self.cur.val


    def forward(self, steps: int) -> str:
        current = self.cur
        while current and steps > 0:
            current = current.next
            steps -= 1
        if current == None or current.val == 'tail':
            self.cur = self.tail.prev
            return self.cur.val
        else:
            self.cur = current
            return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)