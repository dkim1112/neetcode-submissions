class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # when m x n
        m, n = len(matrix), len(matrix[0])

        # r은 첫째줄부터 (=0), c는 오른쪽부터 (=n-1)
        r, c = 0, n - 1

        while r < m and c >= 0: # c >= 0 b/c dont want to go more left than 0
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        
        return False
