class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lm, rm = 0, len(matrix) - 1

        while lm <= rm:
            mm = (lm + rm) // 2
            row = matrix[mm]

            la, ra = 0, len(row) - 1
            while la <= ra:
                ma = (la + ra) // 2

                if row[ma] == target:
                    return True
                if row[ma] < target:
                    la = ma + 1
                else:
                    ra = ma - 1

            if target < row[0]:
                rm = mm - 1       # Search earlier rows
            else:
                lm = mm + 1       # Search later rows

        return False
