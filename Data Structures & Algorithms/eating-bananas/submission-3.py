class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        while lo < hi:
            k = (lo + hi) // 2
            hours = 0
            for p in piles:
                hours += -(-p // k)
            if hours > h:
                lo = k + 1
            else:
                hi = k
        return lo
