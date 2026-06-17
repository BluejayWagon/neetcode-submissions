class Solution:
    def isValid(self, s: str) -> bool:
        opStack = []
        parenHash = {')':'(','}':'{',']':'['}

        for i in s:
            if i in parenHash:
                if not opStack:
                    return False
                op = opStack.pop()
                if parenHash[i] != op:
                    return False
            else:
                opStack.append(i)
        return not opStack