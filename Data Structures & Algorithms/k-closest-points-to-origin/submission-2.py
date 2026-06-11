class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(point: List[int]) -> int:
            return point[0]**2 + point[1]**2
        
        def partition(l, r):
            pivotDist = dist(points[r])
            i = l
            for j in range(l,r):
                if dist(points[j]) <= pivotDist:
                    points[j], points[i] = points[i], points[j]
                    i += 1
            points[i], points[r] = points[r], points[i]
            return i
        
        l, r = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partition(l, r)
            if pivot < k:
                l = pivot + 1
            if pivot > k:
                r = pivot - 1
        return points[0:k]