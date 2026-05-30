class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        returnArray = [0] * len(arr)
        maxNum = -1
        #traverse array right to left
        for i in range(len(arr) - 1, -1, -1):
            returnArray[i] = maxNum
            maxNum = max(arr[i],maxNum)
        return returnArray
