class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort
        def split(arr):
            n = len(arr)
            if n < 2:
                return arr
            mid = n // 2
            return merge(split(arr[:mid]), split(arr[mid:]))

        def merge(left, right):
            out = []
            j, k = 0, 0
            while j < len(left) and k < len(right):
                if left[j] < right[k]:
                    out.append(left[j])
                    j += 1
                else:
                    out.append(right[k])
                    k += 1
            out += left[j:] + right[k:]
            return out

        return split(nums)

        