class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        ans = 0
        for num in hashSet:
            length = 1
            if num - 1 in hashSet:
                continue
            while num + length in hashSet:
                length += 1
            ans = max(ans, length)
        return ans
