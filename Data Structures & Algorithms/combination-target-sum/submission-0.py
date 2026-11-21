class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def dfs(nums, curr, target):
            if target < 0:
                return
            if target == 0:
                ans.append(curr[:])
                return
            for i in range(len(nums)):
                dfs(nums[i:], curr+[nums[i]], target-nums[i])
        
        dfs(nums, [], target)
        return ans
