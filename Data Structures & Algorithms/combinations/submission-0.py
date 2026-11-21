class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def bt(start, curr):
            if len(curr) == k:
                ans.append(curr[:])
                return
            for i in range(start, n+1):
                # curr.append(i)
                bt(i+1, curr+[i])
                # curr.pop()
        bt(1, [])
        return ans