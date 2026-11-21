class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        n, m = len(grid), len(grid[0])
        def bfs(i, j):
            q = [(i, j)]
            grid[i][j] = '0'
            while q:
                x, y = q.pop(0)
                for dx, dy in (x+1,y), (x-1,y), (x,y+1), (x,y-1):
                    if not (0 <= dx < n) or not (0 <= dy < m):
                        continue
                    if grid[dx][dy] == '0':
                        continue
                    grid[dx][dy] = '0'
                    q.append((dx, dy))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    bfs(i, j)
                    ans += 1
        return ans