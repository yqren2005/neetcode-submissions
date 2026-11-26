class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # no recursion
        perms = [[]]
        for num in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p[:]
                    p_copy.insert(i, num)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms
        # O(n! * n^2) | O(n! * n)
