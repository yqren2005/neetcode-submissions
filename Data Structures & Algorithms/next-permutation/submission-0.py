class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Scan from the second-to-last element leftward to find the first index i where nums[i] < nums[i+1].
        
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1

        # If such an index exists
        if i >= 0:

            # Scan from the right to find the first index j where nums[j] > nums[i].
            j = len(nums) - 1
            while j >= 0:
                if nums[j] > nums[i]:
                    break
                j -= 1

            # Swap nums[i] and nums[j].
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the subarray from i+1 to the end.
        l, r = i + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        