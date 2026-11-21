class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                if num in row_set[i]:
                    return False
                if num in col_set[j]:
                    return False
                k = i // 3 * 3 + j // 3
                if num in box_set[k]:
                    return False
                row_set[i].add(num)
                col_set[j].add(num)
                box_set[k].add(num)
        
        return True
