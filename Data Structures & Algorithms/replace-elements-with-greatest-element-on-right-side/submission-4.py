class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        returnArr = [None] * len(arr)
        maxNum = -1
        for i in range(len(arr) -1, -1, -1):
            returnArr[i] = maxNum
            maxNum = max(maxNum, arr[i])
        return returnArr 