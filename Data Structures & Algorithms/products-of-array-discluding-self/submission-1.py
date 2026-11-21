class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tmp1 = [1] * n
        tmp2 = [1] * n
        for i in range(1, n):
            tmp1[i] = nums[i-1] * tmp1[i-1]
        for i in range(n-2, -1, -1):
            tmp2[i] = nums[i+1] * tmp2[i+1]
        ans = [1] * n
        for i in range(n):
            ans[i] = tmp1[i] * tmp2[i]
        return ans