class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        p, a = [], []
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    p.append((r, c))
                if r == rows - 1 or c == cols - 1:
                    a.append((r, c))
        
        def bfs(q):
            visited = set()
            while q:
                r, c = q.pop()
                visited.add((r, c))
                for nr, nc in (r+1,c), (r-1,c), (r,c+1), (r,c-1):
                    if not (0 <= nr < rows):
                        continue
                    if not (0 <= nc < cols):
                        continue
                    if (nr, nc) in visited:
                        continue
                    if heights[r][c] > heights[nr][nc]:
                        continue
                    q.append((nr, nc))
            return visited

        p_visited = bfs(p)
        a_visited = bfs(a)
        ans = p_visited.intersection(a_visited)
        return [list(rc) for rc in ans]

