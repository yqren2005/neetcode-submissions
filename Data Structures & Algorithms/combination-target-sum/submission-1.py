class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []
        def bt(i, left):
            if left == 0:
                ans.append(curr[:])
                return
            if left < 0 or i == len(nums):
                return
            curr.append(nums[i])
            bt(i, left - nums[i])
            curr.pop()
            bt(i + 1, left)
        bt(0, target)
        return ans