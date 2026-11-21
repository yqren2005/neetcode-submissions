class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def bt(nums, curr):
            if len(nums) == 0:
                ans.append(curr)
                return
            for i in range(len(nums)):
                bt(nums[:i]+nums[i+1:], curr+[nums[i]])
        bt(nums, [])
        return ans