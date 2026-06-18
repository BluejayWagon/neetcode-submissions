class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)

        top, bot = 0, rows -1
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break
        
        if not (top <= bot):
            return False

        rowIndex = (top + bot) // 2
        matrixToUse = matrix[rowIndex]

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
