class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxVal = -1
        for i in range(len(arr) - 1, -1, -1):
            print(arr[i])
            valToCompare = arr[i]
            arr[i] = maxVal
            maxVal = max(maxVal, valToCompare)
        return arr
