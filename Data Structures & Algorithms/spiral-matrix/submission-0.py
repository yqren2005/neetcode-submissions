class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        i, j = 0, 0
        ans = []

        while i < rows and j < cols:
            for k in range(j, cols):
                ans.append(matrix[i][k])
            i += 1

            for k in range(i, rows):
                ans.append(matrix[k][cols-1])
            cols -= 1

            if not (i < rows and j < cols):
                break

            for k in range(cols-1, j-1, -1):
                ans.append(matrix[rows-1][k])
            rows -= 1

            for k in range(rows-1, i-1, -1):
                ans.append(matrix[k][j])
            j += 1
        
        return ans

