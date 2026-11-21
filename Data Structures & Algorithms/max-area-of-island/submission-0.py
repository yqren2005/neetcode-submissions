class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = 0

        def bfs(r, c):
            area = 0
            q = [(r, c)]
            grid[r][c] = 0
            while q:
                # print('q', q)
                r, c = q.pop(0)
                area += 1
                # print(r, c, area)
                for nr, nc in (r+1,c), (r-1,c), (r,c+1), (r,c-1):
                    if nr < 0 or nr >= rows:
                        continue
                    if nc < 0 or nc >= cols:
                        continue
                    if grid[nr][nc] == 0:
                        continue
                    grid[nr][nc] = 0
                    q.append((nr, nc))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                ans = max(ans, bfs(r, c))
        return ans

                    
