class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        returnArray = [0] * len(arr)
        #traverse array right to left
        for i in range(len(arr) - 1, -1, -1):
            maxNum=-1
            for j in range(i + 1, len(arr)):
                maxNum = max(arr[j],maxNum)
            returnArray[i] = maxNum
        return returnArray
