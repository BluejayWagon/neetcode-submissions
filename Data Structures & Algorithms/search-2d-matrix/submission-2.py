class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrixStack = []
        for m in matrix:
            if m[0] <= target:
                matrixStack.append(m)
            else:
                break
        if not matrixStack:
            return False
        matrixToUse = matrixStack.pop()
        print(matrixToUse)
        l = 0
        r = len(matrixToUse) - 1
        mid = (l + r) // 2
        while l <= r:
            if target < matrixToUse[mid]:
                r = mid - 1
                mid = (l + r) // 2
            elif target > matrixToUse[mid]:
                l = mid + 1
                mid = (l + r) // 2
            else:
                return True
        return False
