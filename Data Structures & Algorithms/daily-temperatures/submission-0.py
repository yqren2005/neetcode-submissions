class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #monotonic stack
        s = []
        ans = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while s and s[-1][1] < t:
                pre, _ = s.pop()
                ans[pre] = i - pre
            s.append((i, t))
        return ans