class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
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
        if not opStack:
            return True
        else:
            return False