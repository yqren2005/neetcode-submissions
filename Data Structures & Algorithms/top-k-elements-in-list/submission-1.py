class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        # print(d)
        freq = [[] for _ in range(len(nums)+1)]
        for key, val in d.items():
            freq[val].append(key)
        # print(freq)
        ans = []
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
