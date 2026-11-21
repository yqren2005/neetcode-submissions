class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        nums.sort()
        def bt(i):
            if i == len(nums):
                ans.append(cur[:])
                return
            cur.append(nums[i])
            bt(i + 1)
            cur.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            bt(i + 1)
        bt(0)
        return ans