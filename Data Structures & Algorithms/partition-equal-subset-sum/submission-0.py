class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2 or sum(nums) % 2 > 0:
            return False
        s = {0}
        for i in nums:
            for j in list(s):
                if i + j == sum(nums) // 2:
                    return True
                s.add(i + j)
        return False
