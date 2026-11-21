class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        runningProd = 1
        n = len(nums)
        ans = [1] * n
        for i in range(n - 1):
            runningProd *= nums[i]
            ans[i+1] *= runningProd

        runningProd = 1
        for i in range(n-1, 0, -1):
            runningProd *= nums[i]
            ans[i-1] *= runningProd
        return ans
