class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m * n
        left = 0
        right = t - 1

        while left <= right:
            middle = (left + right) // 2
            i = middle // n
            j = middle % n

            mid_num = matrix[i][j]

            if target == mid_num:
                return True

            elif target < mid_num:
                right = middle - 1

            else:
                left = middle + 1

        return False