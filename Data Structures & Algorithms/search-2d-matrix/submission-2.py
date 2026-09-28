class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r:
            mid = (l + r) // 2

            val = matrix[mid // n][mid % n]
            if val == target:
                return True

            if val < target:
                l += 1
            else:
                r -= 1
        
        return False