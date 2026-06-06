class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.list = [None] * self.capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.list[i]

    def set(self, i: int, n: int) -> None:
        if not self.list[i]:
            self.length += 1
        self.list[i] = n  


    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.length += 1
        self.list[self.length - 1] = n


    def popback(self) -> int:
        returnVal = self.list[self.length -1]
        self.length -= 1
        return returnVal

    def resize(self) -> None:
        self.list = self.list + ([None] * self.capacity)
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
