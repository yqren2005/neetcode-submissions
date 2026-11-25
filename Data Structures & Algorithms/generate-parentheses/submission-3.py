class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        curr = []
        def bt(open, close):
            if open == close == n:
                ans.append(''.join(curr))
                return
            if open < n:
                curr.append('(')
                bt(open+1, close)
                curr.pop()
            if open > close:
                curr.append(')')
                bt(open, close+1)
                curr.pop()
        bt(0, 0)
        return ans
