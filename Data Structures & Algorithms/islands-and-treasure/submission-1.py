class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = []
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        while q:
            r, c = q.pop(0)
            for nr, nc in (r+1,c), (r-1,c), (r,c+1), (r,c-1):
                if not (0 <= nr < rows):
                    continue
                if not (0 <= nc < cols):
                    continue
                if (nr, nc) in visited:
                    continue
                if grid[nr][nc] in (-1, 0):
                    continue
                visited.add((nr, nc))
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))
        


