class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        if n > 12:
            return ans

        def bt(i, dots, curr):
            if i == n and dots == 4:
                ans.append(curr[:-1])
                return
            if dots > 4:
                return
            for j in range(i, min(i+3, n)):
                if int(s[i:j+1]) <= 255 and (i==j or s[i]!='0'):
                    bt(j+1, dots+1, curr+s[i:j+1]+'.')

        bt(0, 0, '')
        return ans