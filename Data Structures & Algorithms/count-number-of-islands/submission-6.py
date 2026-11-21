class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        # def bfs(x, y):
        #     if grid[x][y] == "0":
        #         return 0
        #     grid[x][y] = "0" #important
        #     q = [(x, y)]
        #     while q:
        #         r, c = q.pop(0)
        #         for rn, cn in (r+1,c), (r-1,c), (r,c+1), (r,c-1):
        #             if not (0 <= rn < rows) or not (0 <= cn < cols):
        #                 continue
        #             if grid[rn][cn] == "0":
        #                 continue
        #             grid[rn][cn] = "0" #important
        #             q.append((rn, cn))
        #     return 1

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j]=="0":
                return
            grid[i][j] = "0" #visited
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for r in range(rows):
            for c in range(cols):
                # count += bfs(r, c)
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count

