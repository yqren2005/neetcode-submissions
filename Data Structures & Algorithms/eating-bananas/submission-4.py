class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)

        while lo < hi: #rule for lo <= hi: hi = k - 1
            k = (lo + hi) // 2
            hours = sum(-(-p // k) for p in piles)

            if hours > h:
                lo = k + 1 #k too slow, must be excluded
            else:
                hi = k #k works, but a smaller speed might too
        
        return hi #hi == lo

'''
loop condition	hi update	meaning of hi
while lo <= hi	hi = k - 1	k has been ruled out, so exclude it
while lo < hi	hi = k	    k might still be the answer, so keep it
'''
