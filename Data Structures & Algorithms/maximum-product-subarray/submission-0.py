class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        curMinProd = 1
        curMaxProd = 1
        for num in nums:
            curMinProd, curMaxProd = min(curMinProd * num, curMaxProd * num, num), max(
                curMinProd * num, curMaxProd * num, num
            )
            maxProd = max(maxProd, curMaxProd)
        return maxProd