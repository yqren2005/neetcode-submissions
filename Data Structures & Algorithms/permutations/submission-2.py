class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def bt(curr, left):
            if left == []:
                ans.append(curr)
                return
            for i in range(len(left)):
                bt(curr+[left[i]], left[:i]+left[i+1:])
        bt([], nums)
        return ans