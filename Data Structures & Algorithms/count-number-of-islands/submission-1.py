class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        def bfs(x, y):
            if grid[x][y] == "0":
                return 0
            q = [(x, y)]
            while q:
                r, c = q.pop(0)
                grid[r][c] = "0"
                for rn, cn in (r+1,c), (r-1,c), (r,c+1), (r,c-1):
                    if not (0 <= rn < rows) or not (0 <= cn < cols):
                        continue
                    if grid[rn][cn] == "0":
                        continue
                    q.append((rn, cn))
            return 1

        for r in range(rows):
            for c in range(cols):
                count += bfs(r, c)
        return count
