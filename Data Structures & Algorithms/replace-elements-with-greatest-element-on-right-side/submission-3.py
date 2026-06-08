class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        returnarr = [0] * len(arr)
        maxVal = -1
        for i in range(len(arr) - 1, -1, -1):
            returnarr[i] = maxVal
            maxVal = max(maxVal, arr[i])
        return returnarr