class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        k = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            hours = sum([-(-p // mid) for p in piles])
            if hours > h:
                lo = mid + 1
            else:
                k = mid
                hi = mid - 1
        return k