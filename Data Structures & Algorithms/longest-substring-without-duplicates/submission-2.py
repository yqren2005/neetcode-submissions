class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        chars = {}
        ans = 0
        for i in range(len(s)):
            if s[i] in chars and chars[s[i]] >= start:
                start = chars[s[i]] + 1
            chars[s[i]] = i
            ans = max(ans, i - start + 1)
        return ans