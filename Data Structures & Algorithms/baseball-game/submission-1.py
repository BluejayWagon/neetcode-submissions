class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            stackLen = len(stack) - 1
            if i == '+':
                firstNum = stack[-1]
                secondNum = stack[-2]
                stack.append(int(firstNum) + int(secondNum))
            elif i == 'D':
                previousScore = stack[-1]
                stack.append(int(previousScore) * 2)
            elif i == 'C':
                stack.pop()
            else:
                stack.append(int(i))
        return sum(stack)