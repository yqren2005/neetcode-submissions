class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 2nd solution, using lo <= hi
        lo, hi = 1, max(piles)
        k = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            hours = sum(-(-p // mid) for p in piles)
            if hours > h:
                lo = mid + 1
            else:
                hi = mid - 1 #then look for something smaller
                k = mid #mid works, so record it
        return k
    # O(n log m)|O(1) (n = len(piles), m = max(piles))

