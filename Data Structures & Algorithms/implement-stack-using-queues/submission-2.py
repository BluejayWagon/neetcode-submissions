class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        if self.q1:
            self.q2.append(x)
            while self.q1:
                self.q2.append(self.q1.popleft())
            print('added ' + str(x) + ' to q2')
        else:
            self.q1.append(x)
            while self.q2:
                self.q1.append(self.q2.popleft())
            print('added ' + str(x) + ' to q1')


    def pop(self) -> int:
        if self.q1:
            print(list(self.q1))
            returnVal = self.q1.popleft()
            if len(self.q1) == 0:
                return returnVal
            while self.q1:
                finalVal = self.q1.popleft()
                self.q2.append(finalVal)
            while self.q2:
                self.q1.append(self.q2.popleft())
        else:
            returnVal = self.q2.popleft()
            if len(self.q2) == 0:
                return returnVal
            while self.q2:
                finalVal = self.q2.popleft()
                self.q1.append(finalVal)
            while self.q1:
                self.q2.append(self.q1.popleft())
        return returnVal
        

    def top(self) -> int:
        if self.q1:
            return self.q1[0]
        else:
            return self.q2[0]

    def empty(self) -> bool:
        if self.q1 or self.q2:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()