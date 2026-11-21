class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        targets = 0
        steps = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    targets += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        while q and targets > 0:
            n = len(q)
            for _ in range(n):
                r, c = q.pop(0)
                for x, y in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                        grid[x][y] = 2
                        targets -= 1
                        q.append((x, y))
            steps += 1
        return steps if targets == 0 else -1
