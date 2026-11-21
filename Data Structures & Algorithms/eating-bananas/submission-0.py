class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        while lo <= hi:
            k = (lo + hi) // 2
            hours = sum([-(-p // k) for p in piles])
            if hours > h:
                lo = k + 1
            else:
                hi = k - 1
        return lo