class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        curr = []
        def bt(opens, closes):
            if opens == closes == n:
                ans.append(''.join(curr))
                return
            if opens < n:
                curr.append('(')
                bt(opens+1, closes)
                curr.pop()
            if closes < opens:
                curr.append(')')
                bt(opens, closes+1)
                curr.pop()
        
        bt(0, 0)
        return ans
