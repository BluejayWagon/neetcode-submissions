class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 or len(s) == 0:
            return False
        openStack = []
        closedStack = []
        parenHash = {'(':')','[':']','{':'}'}
        for paren in s:
            #if it's an opening paraen
            if paren in parenHash:
                openStack.append(paren)
                closedStack.append(parenHash[paren])
            #if it's not a key in paren hash it's a closed paren
            #check if it's latest in queue
            else:
                if len(closedStack) == 0:
                    return False
                val = closedStack.pop()
                if paren != val:
                    print(paren)
                    print(val)
                    return False
        if len(closedStack) != 0:
            return False
        return True

