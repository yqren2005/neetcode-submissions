class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi-sources BFS
        rows, cols = len(grid), len(grid[0])
        freshs = 0
        q = [] # rottens
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    freshs += 1
        # print(freshs, q)
        minutes = 0
        while q and freshs > 0:
            for i in range(len(q)):
            # for _ in range(len(q)):
                r, c = q[i]
                for nr, nc in (r+1,c), (r-1,c), (r,c+1), (r,c-1):
                    if not (0 <= nr < rows):
                        continue
                    if not (0 <= nc < cols):
                        continue
                    if grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    freshs -= 1
                    q.append((nr, nc))
            minutes += 1
            # print(q, minutes, freshs, i, q[i:])
            q = q[i+1:]
        return minutes if freshs == 0 else -1

