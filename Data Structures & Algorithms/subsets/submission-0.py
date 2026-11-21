class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        def bt(i):
            if i == len(nums):
                ans.append(curr[:])
                return
            curr.append(nums[i])
            bt(i+1)
            curr.pop()
            bt(i+1)
        bt(0)
        return ans