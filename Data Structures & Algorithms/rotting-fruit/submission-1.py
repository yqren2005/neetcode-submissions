class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        fresh = 0
        n, m = len(grid), len(grid[0])
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        # if fresh == 0: return 0
        ans = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.pop(0)
                for nr, nc in (r+1,c), (r-1,c), (r,c+1), (r,c-1):
                    if not(0 <= nr < n) or not(0 <= nc < m):
                        continue
                    if grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    # if fresh == 0:
                    #     return ans + 1
                    q.append((nr, nc))
            ans += 1
        return ans if fresh == 0 else -1



