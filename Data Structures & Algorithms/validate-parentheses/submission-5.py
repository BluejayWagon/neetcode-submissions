class Solution:
    def isValid(self, s: str) -> bool:
        openStack = []
        closeStack = []
        parenHash = {'(':')','{':'}','[':']'}
        returnVal = True
        for i in s:
            if i in [')','}',']']:
                if len(closeStack) == 0:
                    return False
                closeCheck = closeStack.pop()
                if i != closeCheck:
                    return False
                else:
                    openStack.pop()
            else:
                openStack.append(i)
                closeStack.append(parenHash[i]) 
        if len(closeStack) != 0 or len(openStack) != 0:
            return False 
        return returnVal