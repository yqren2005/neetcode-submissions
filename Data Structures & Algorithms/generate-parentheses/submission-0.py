class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def bt(curr, opens, closes):
            if len(curr) == 2 * n:
                ans.append(curr)
                return
            if opens < n:
                bt(curr+'(', opens+1, closes)
            if closes < opens:
                bt(curr+')', opens, closes+1)
        
        bt('', 0, 0)
        return ans
