class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def bt(curr, open, close):
            if open == close == n:
                ans.append(curr)
                return
            if open < n:
                bt(curr+'(', open+1, close)
            if open > close:
                bt(curr+')', open, close+1)

        bt('', 0, 0)
        return ans
        