class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        i = 0
        ans = 0
        for j in range(len(s)):
            char = s[j]
            if char in d and d[char] >= i: #abba
                i = d[char] + 1
            d[char] = j
            ans = max(ans, j - i + 1)
        return ans