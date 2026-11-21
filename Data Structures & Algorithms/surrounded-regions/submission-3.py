class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # multi-source BFS
        rows, cols = len(board), len(board[0])
        q = []

        for r in range(rows):
            for c in range(cols):
                if 0 < r < rows - 1 and 0 < c < cols - 1:
                    continue
                if board[r][c] == 'O':
                    q. append((r, c))
                    
        while q:
            r, c = q.pop(0)
            board[r][c] = 'T'
            for dr, dc in (r+1,c), (r-1,c), (r,c+1), (r,c-1):
                if not (0 <= dr < rows):
                    continue
                if not (0 <= dc < cols):
                    continue
                if board[dr][dc] == 'O':
                    q.append((dr, dc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        

