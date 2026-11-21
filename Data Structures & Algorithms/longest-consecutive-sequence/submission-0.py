class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        ans = 0
        for num in hs:
            tmp = 0
            if num - 1 in hs:
                continue
            while num in hs:
                tmp += 1
                num += 1
            ans = max(ans, tmp)
        return ans
