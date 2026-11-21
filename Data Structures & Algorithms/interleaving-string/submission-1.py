class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        rows, cols = len(s1), len(s2)
        if rows + cols != len(s3): return False
        dp = [[False for _ in range(cols+1)] for _ in range(rows+1)]
        dp[rows][cols] = True
        for r in range(rows, -1, -1):
            for c in range(cols, -1, -1):
                if r < rows and s1[r] == s3[r+c]:
                    dp[r][c] = dp[r][c] or dp[r+1][c]
                if c < cols and s2[c] == s3[r+c]:
                    dp[r][c] = dp[r][c] or dp[r][c+1]
        return dp[0][0]
