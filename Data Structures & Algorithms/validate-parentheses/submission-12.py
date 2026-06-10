class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 or len(s) == 0:
            return False
        parenHash = {')':'(',']':'[','}':'{'}
        stack = []

        for val in s:
            if val not in parenHash:
                stack.append(val)
            else:
                if not stack or parenHash[val] != stack[-1]:
                    return False
                else:
                    stack.pop()
        
        if len(stack) != 0:
            return False
        else:
            return True
        