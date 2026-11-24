class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #backtracking
        ans = []
        curr = [['.'] * n for _ in range(n)]
        columns = set()
        posDiag = set() # r+c = constant
        negDiag = set() # r-c = constant
        def bt(row):
            if row == n:
                ans.append([''.join(line) for line in curr]) 
                return
            for col in range(n):
                if col in columns:
                    continue
                if row + col in posDiag:
                    continue
                if row - col in negDiag:
                    continue
                
                curr[row][col] = 'Q'
                columns.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)

                bt(row + 1)

                curr[row][col] = '.'
                columns.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)

        bt(0)
        return ans
        
