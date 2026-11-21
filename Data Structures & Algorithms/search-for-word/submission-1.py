class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def dfs(r, c, i):
            ch = board[r][c]
            if ch != word[i]:
                return False
            if i == len(word)-1:
                return True
            board[r][c] = ''
            for nr, nc in (r+1,c), (r-1,c), (r,c+1), (r,c-1):
                if not (0<=nr<rows) or not (0<=nc<cols):
                    continue
                if dfs(nr, nc, i+1):
                    return True
            board[r][c] = ch
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False

